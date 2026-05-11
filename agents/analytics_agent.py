from tools.analytics_tools import (
    get_dataset_summary,
    get_total_consumption,
    get_average_consumption,
    get_top_consuming_appliances,
    estimate_total_cost,
    get_consumption_by_season,
    get_consumption_by_household_size
)


def run_analytics_agent(df, question: str, price_per_kwh: float):
    """
    Analytics Agent.

    This agent handles numerical and statistical questions about
    electricity consumption.
    """

    question_lower = question.lower()

    if "summary" in question_lower or "overview" in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "summary",
            "result": get_dataset_summary(df)
        }

    if "total" in question_lower and "cost" not in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "total_consumption",
            "result": get_total_consumption(df)
        }

    if "average" in question_lower or "mean" in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "average_consumption",
            "result": get_average_consumption(df)
        }

    if "cost" in question_lower or "price" in question_lower or "bill" in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "estimated_cost",
            "result": estimate_total_cost(df, price_per_kwh)
        }

    if "top" in question_lower or "most" in question_lower or "highest" in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "top_appliances",
            "result": get_top_consuming_appliances(df)
        }

    if "season" in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "season_consumption",
            "result": get_consumption_by_season(df)
        }

    if "household" in question_lower or "household size" in question_lower:
        return {
            "agent": "Analytics Agent",
            "type": "household_size_consumption",
            "result": get_consumption_by_household_size(df)
        }

    return {
        "agent": "Analytics Agent",
        "type": "unknown",
        "result": "The Analytics Agent could not identify the requested analysis."
    }

