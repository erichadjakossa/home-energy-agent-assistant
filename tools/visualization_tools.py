import pandas as pd
import plotly.express as px


def plot_consumption_by_appliance(df: pd.DataFrame):
    """
    Create a bar chart of total energy consumption by appliance type.
    """
    data = (
        df.groupby("appliance_type")["energy_consumption_kwh"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="appliance_type",
        y="energy_consumption_kwh",
        title="Total Energy Consumption by Appliance",
        labels={
            "appliance_type": "Appliance",
            "energy_consumption_kwh": "Energy Consumption (kWh)"
        }
    )

    return fig


def plot_consumption_by_season(df: pd.DataFrame):
    """
    Create a bar chart of total energy consumption by season.
    """
    data = (
        df.groupby("season")["energy_consumption_kwh"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="season",
        y="energy_consumption_kwh",
        title="Total Energy Consumption by Season",
        labels={
            "season": "Season",
            "energy_consumption_kwh": "Energy Consumption (kWh)"
        }
    )

    return fig


def plot_consumption_by_household_size(df: pd.DataFrame):
    """
    Create a line chart of average consumption by household size.
    """
    data = (
        df.groupby("household_size")["energy_consumption_kwh"]
        .mean()
        .sort_index()
        .reset_index()
    )

    fig = px.line(
        data,
        x="household_size",
        y="energy_consumption_kwh",
        markers=True,
        title="Average Energy Consumption by Household Size",
        labels={
            "household_size": "Household Size",
            "energy_consumption_kwh": "Average Energy Consumption (kWh)"
        }
    )

    return fig


def plot_consumption_over_time(df: pd.DataFrame):
    """
    Create a time series chart of total energy consumption over time.
    """
    data = df.copy()

    data["date"] = pd.to_datetime(data["date"])

    time_series = (
        data.groupby("date")["energy_consumption_kwh"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        time_series,
        x="date",
        y="energy_consumption_kwh",
        title="Energy Consumption Over Time",
        labels={
            "date": "Date",
            "energy_consumption_kwh": "Energy Consumption (kWh)"
        }
    )

    return fig

##########
def plot_temperature_vs_consumption(df: pd.DataFrame):
    """
    Create scatter plots of outdoor temperature vs energy consumption,
    separated by appliance type, with regression trend lines.
    """

    fig = px.scatter(
        df[::60],
        x="outdoor_temperature_c",
        y="energy_consumption_kwh",
        facet_col="appliance_type",
        facet_col_wrap=3,
        trendline="ols",
        color="season",
        title="Outdoor Temperature vs Energy Consumption by Appliance",
        labels={
            "outdoor_temperature_c": "Outdoor Temperature (°C)",
            "energy_consumption_kwh": "Energy Consumption (kWh)",
            "appliance_type": "Appliance"
        }
    )

    fig.update_layout(height=900)

    return fig

