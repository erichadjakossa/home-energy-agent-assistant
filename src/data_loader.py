import pandas as pd


def load_energy_data(file_path):
    """
    Load the home energy consumption dataset.

    Args:
        file_path: Path to the CSV file.

    Returns:
        pandas DataFrame.
    """
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

