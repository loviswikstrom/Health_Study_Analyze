import pandas as pd
import numpy as np


#Räkna ut medel, median, min och max för: age, weight, height, systolic_bp, cholesterol.

def age_mean(df: pd.DataFrame) -> float:
    return float(df["age"].mean())

def descriptive_statistics(df):
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    return df[columns].describe()



def disease_amount(df):
    return df["disease"].sum()

def disease_probability(df):
    amount = df["disease"].sum()
    return amount / len(df)

def probability_simulation(df):
    people = 1000
    prob = disease_probability(df)
    disease_sim = np.random.choice(
        [0, 1],
        size=people,
        p=[1 - prob, prob]
    )
    return disease_sim
    
