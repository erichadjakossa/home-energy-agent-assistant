from tools.visualization_tools import (
    plot_consumption_by_appliance,
    plot_consumption_by_season,
    plot_consumption_by_household_size,
    plot_consumption_over_time,
    plot_temperature_vs_consumption
)


def run_visualization_agent(df, question: str):
    """
    Visualization Agent.

    This agent decides which chart to generate based on the user question.
    """

    question_lower = question.lower()

    if "temperature" in question_lower:
        return {
            "agent": "Visualization Agent",
            "type": "temperature_vs_consumption",
            "figure": plot_temperature_vs_consumption(df),
            "description": "Scatter plot of outdoor temperature vs energy consumption by appliance."
        }

    if "season" in question_lower:
        return {
            "agent": "Visualization Agent",
            "type": "season_consumption",
            "figure": plot_consumption_by_season(df),
            "description": "Bar chart of total energy consumption by season."
        }

    if "household" in question_lower or "household size" in question_lower:
        return {
            "agent": "Visualization Agent",
            "type": "household_size_consumption",
            "figure": plot_consumption_by_household_size(df),
            "description": "Line chart of average energy consumption by household size."
        }

    if "time" in question_lower or "trend" in question_lower or "over time" in question_lower:
        return {
            "agent": "Visualization Agent",
            "type": "consumption_over_time",
            "figure": plot_consumption_over_time(df),
            "description": "Time series chart of total energy consumption over time."
        }

    if "appliance" in question_lower or "top" in question_lower or "most" in question_lower:
        return {
            "agent": "Visualization Agent",
            "type": "appliance_consumption",
            "figure": plot_consumption_by_appliance(df),
            "description": "Bar chart of total energy consumption by appliance."
        }

    return {
        "agent": "Visualization Agent",
        "type": "unknown",
        "figure": None,
        "description": "The Visualization Agent could not identify which chart to generate."
    }

