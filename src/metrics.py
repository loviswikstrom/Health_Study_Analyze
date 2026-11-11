import pandas as pd
import numpy as np


#Räkna ut medel, median, min och max för: age, weight, height, systolic_bp, cholesterol.

def age_mean(df: pd.DataFrame) -> float:
    return float(df["age"].mean())

def descriptive_statistics(df):
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    return df[columns].describe()



