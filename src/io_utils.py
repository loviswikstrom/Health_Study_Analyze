
import pandas as pd

REQUIRED = [
    "id", "age", "sex", "height", "weight",
    "systolic_bp", "cholesterol", "smoker", "disease"
]

def load_data(file_path: str) -> pd.DataFrame:
    """
    Läser in projektets CSV-fil och kontrollerar
    att alla obligatoriska kolumner finns.
    """

    try:
        df = pd.read_csv(file_path)

        missing = [c for c in REQUIRED if c not in df.columns]

        if missing:
            raise ValueError(f"Följande kolumner saknas: {missing}")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"Filen hittades inte: {file_path}")