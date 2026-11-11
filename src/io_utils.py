

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "health_study_dataset.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df




#import pandas as pd

#REQUIRED = [
    #"id", "age", "sex", "height", "weight",
    #"systolic_bp", "cholesterol", "smoker", "disease"
#]

#def load_data(file_path: str) -> pd.DataFrame:
    #"""
    #Läser in projektets CSV-fil och kontrollerar
    #att alla obligatoriska kolumner finns.
    #"""

    #try:
        #df = pd.read_csv(file_path)

        #missing = [c for c in REQUIRED if c not in df.columns]

        #if missing:
            #raise ValueError(f"Följande kolumner saknas: {missing}")

        #return df

    #except FileNotFoundError:
        #raise FileNotFoundError(f"Filen hittades inte: {file_path}"))