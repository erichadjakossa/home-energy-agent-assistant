from src.config import DEFAULT_DATA_PATH
from src.data_loader import load_energy_data


def main():
    df = load_energy_data(DEFAULT_DATA_PATH)

    print("Dataset loaded successfully!")
    print("\nShape:")
    print(df.shape)
    print(f"\nThis dataset contains {df.shape[0]} observations described by {df.shape[1]} features.")

    print("\nColumns or features that describe the data points are:")
    print(df.columns.tolist())

    print("\nFirst rows:")
    print(df.head())

    print(f"\nMissing values per feature:")
    print(df.isna().sum())


if __name__ == "__main__":
    main()

