

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "health_study_dataset.csv"

def load_data():
    """
    Läser in hälsodata från health_study_dataset.csv
    och returnerar dataset som en DataFrame.
    """
    df = pd.read_csv(DATA_PATH)
    return df

