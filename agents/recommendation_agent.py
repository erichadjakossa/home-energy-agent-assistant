from tools.analytics_tools import (
    get_top_consuming_appliances,
    get_consumption_by_season,
    get_total_consumption,
    estimate_total_cost
)


def run_recommendation_agent(df, question: str, price_per_kwh: float):
    """
    Recommendation Agent.

    This agent generates practical energy-saving recommendations
    based on consumption patterns.
    """

    top_appliances = get_top_consuming_appliances(df, top_n=5)
    seasonal_consumption = get_consumption_by_season(df)
    total_consumption = get_total_consumption(df)
    estimated_cost = estimate_total_cost(df, price_per_kwh)

    recommendations = []

    # Top-consuming appliances
    highest_appliance = top_appliances.iloc[0]["appliance_type"]
    highest_consumption = top_appliances.iloc[0]["energy_consumption_kwh"]

    recommendations.append(
        f"The appliance with the highest total consumption is "
        f"{highest_appliance}, with {highest_consumption:.2f} kWh. "
        f"This should be the first target for optimization."
    )

    # Seasonal recommendation
    highest_season = seasonal_consumption.iloc[0]["season"]
    highest_season_consumption = seasonal_consumption.iloc[0]["energy_consumption_kwh"]

    recommendations.append(
        f"Energy consumption is highest during {highest_season}, "
        f"with {highest_season_consumption:.2f} kWh. "
        f"Energy-saving actions during this season may have the strongest impact."
    )

    # Cost-aware recommendation
    recommendations.append(
        f"The estimated total electricity cost is {estimated_cost:.2f} "
        f"based on a price of {price_per_kwh:.2f} per kWh. "
        f"Reducing total consumption by 10% could save approximately "
        f"{estimated_cost * 0.10:.2f}."
    )

    # Generic practical advice
    recommendations.append(
        "Practical actions include prioritizing high-consumption appliances, "
        "using appliances during off-peak hours when possible, improving usage habits, "
        "and replacing inefficient appliances with energy-efficient models."
    )

    return {
        "agent": "Recommendation Agent",
        "type": "energy_saving_recommendations",
        "top_appliances": top_appliances,
        "seasonal_consumption": seasonal_consumption,
        "total_consumption": total_consumption,
        "estimated_cost": estimated_cost,
        "recommendations": recommendations
    }

