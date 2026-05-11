from pathlib import Path

# Project paths
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

# Dataset
DEFAULT_DATA_PATH = DATA_DIR / "smart_home_energy_consumption_large.csv"

# App settings
APP_TITLE = "Home Energy Multi-Agent Assistant"

# Energy cost assumption
# You can update this later depending on the country/provider.
DEFAULT_PRICE_PER_KWH = 0.25

