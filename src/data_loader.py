import pandas as pd
from pathlib import Path

def load_energy_data(file_path):
    """
    Load the home energy consumption dataset.

    Args:
        file_path: Path to the CSV file.

    Returns:
        pandas DataFrame.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Data file not found: {file_path}. "
            "Please download the CSV file here: 
https://www.kaggle.com/datasets/mexwell/smart-home-energy-consumption?select=smart_home_energy_consumption_large.csv"
        )

    df = pd.read_csv(file_path)

    # Clean column names for easier handling
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("°", "", regex=False)
    )

    return df

