import pandas as pd


def get_dataset_summary(df: pd.DataFrame) -> dict:
    """
    Return a basic summary of the dataset.
    """
    return {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "columns": df.columns.tolist(),
        "missing_values": df.isna().sum().to_dict()
    }


def get_total_consumption(df: pd.DataFrame) -> float:
    """
    Compute total energy consumption in kWh.
    """
    return df["energy_consumption_kwh"].sum()


def get_average_consumption(df: pd.DataFrame) -> float:
    """
    Compute average energy consumption in kWh.
    """
    return df["energy_consumption_kwh"].mean()


def get_consumption_by_appliance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute total energy consumption by appliance type.
    """
    result = (
        df.groupby("appliance_type")["energy_consumption_kwh"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return result


def get_top_consuming_appliances(
    df: pd.DataFrame,
    top_n: int = 5
) -> pd.DataFrame:
    """
    Return the top N appliances by energy consumption.
    """
    return get_consumption_by_appliance(df).head(top_n)


def estimate_total_cost(
    df: pd.DataFrame,
    price_per_kwh: float
) -> float:
    """
    Estimate total electricity cost.
    """
    total_consumption = get_total_consumption(df)
    return total_consumption * price_per_kwh


def get_consumption_by_season(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute total energy consumption by season.
    """
    result = (
        df.groupby("season")["energy_consumption_kwh"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return result


def get_consumption_by_household_size(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute average energy consumption by household size.
    """
    result = (
        df.groupby("household_size")["energy_consumption_kwh"]
        .mean()
        .sort_index()
        .reset_index()
    )

    return result

