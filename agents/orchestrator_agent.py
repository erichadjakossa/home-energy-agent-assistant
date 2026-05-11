from agents.analytics_agent import run_analytics_agent
from agents.visualization_agent import run_visualization_agent
from agents.recommendation_agent import run_recommendation_agent


def route_question(question: str) -> list[str]:
    """
    Decide which agents should be called based on the user question.
    """

    question_lower = question.lower()

    agents_to_call = []

    visualization_keywords = [
        "plot", "chart", "visualize", "graph", "show me",
        "trend", "over time"
    ]

    recommendation_keywords = [
        "recommend", "recommendation", "advice", "reduce",
        "save", "saving", "optimize", "improve"
    ]

    analytics_keywords = [
        "total", "average", "mean", "top", "most", "highest",
        "cost", "price", "bill", "season", "household",
        "summary", "overview", "consume", "consumption"
    ]

    if any(keyword in question_lower for keyword in visualization_keywords):
        agents_to_call.append("visualization")

    if any(keyword in question_lower for keyword in recommendation_keywords):
        agents_to_call.append("recommendation")

    if any(keyword in question_lower for keyword in analytics_keywords):
        agents_to_call.append("analytics")

    # Default behavior
    if not agents_to_call:
        agents_to_call.append("analytics")

    return agents_to_call


def run_orchestrator_agent(df, question: str, price_per_kwh: float):
    """
    Orchestrator Agent.

    This agent decides which specialized agents to call and combines their outputs.
    """

    agents_to_call = route_question(question)

    outputs = {
        "question": question,
        "agents_called": agents_to_call,
        "analytics": None,
        "visualization": None,
        "recommendation": None
    }

    if "analytics" in agents_to_call:
        outputs["analytics"] = run_analytics_agent(
            df=df,
            question=question,
            price_per_kwh=price_per_kwh
        )

    if "visualization" in agents_to_call:
        outputs["visualization"] = run_visualization_agent(
            df=df,
            question=question
        )

    if "recommendation" in agents_to_call:
        outputs["recommendation"] = run_recommendation_agent(
            df=df,
            question=question,
            price_per_kwh=price_per_kwh
        )

    return outputs

