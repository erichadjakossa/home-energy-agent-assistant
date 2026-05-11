import streamlit as st

from src.config import APP_TITLE, DEFAULT_DATA_PATH, DEFAULT_PRICE_PER_KWH
from src.data_loader import load_energy_data
from agents.orchestrator_agent import run_orchestrator_agent


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Home Energy Multi-Agent Assistant")

st.write(
    "Ask questions about home appliance electricity consumption. "
    "The system uses specialized agents for analytics, visualization, and recommendations."
)

st.sidebar.header("Settings")

price_per_kwh = st.sidebar.number_input(
    "Electricity price per kWh",
    min_value=0.0,
    value=DEFAULT_PRICE_PER_KWH,
    step=0.01
)

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = load_energy_data(uploaded_file)
    st.sidebar.success("CSV uploaded successfully.")
else:
    df = load_energy_data(DEFAULT_DATA_PATH)
    st.sidebar.info("Using default dataset.")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.write(f"Rows: **{df.shape[0]}** | Columns: **{df.shape[1]}**")

question = st.text_input(
    "Ask a question",
    placeholder="Example: Show me the top consuming appliances and give recommendations."
)

if st.button("Run Agents") and question:
    with st.spinner("Orchestrating agents..."):
        response = run_orchestrator_agent(
            df=df,
            question=question,
            price_per_kwh=price_per_kwh
        )

    st.subheader("Agents Called")
    st.write(", ".join(response["agents_called"]))

    if response["analytics"] is not None:
        st.subheader("Analytics Agent Result")

        analytics_result = response["analytics"]["result"]

        if hasattr(analytics_result, "shape"):
            st.dataframe(analytics_result)
        else:
            st.write(analytics_result)

    if response["visualization"] is not None:
        st.subheader("Visualization Agent Result")

        st.write(response["visualization"]["description"])

        fig = response["visualization"]["figure"]

        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No visualization could be generated.")

    if response["recommendation"] is not None:
        st.subheader("Recommendation Agent Result")

        for i, recommendation in enumerate(
            response["recommendation"]["recommendations"],
            start=1
        ):
            st.write(f"**{i}.** {recommendation}")
else:
    st.info("Enter a question and click 'Run Agents'.")

