import pandas as pd
import numpy as np


#Räkna ut medel, median, min och max för: age, weight, height, systolic_bp, cholesterol.

def age_mean(df: pd.DataFrame) -> float:
    """
    Beräknar medelåldern i datasetet.
    """
    return float(df["age"].mean())

def descriptive_statistics(df):
    """
    Beräknar beskrivande statistik för utvalda kolumner.
    """
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    return df[columns].describe()

def disease_amount(df):
    """
    Räknar antalet personer med sjukdom.
    """
    return df["disease"].sum()

def disease_probability(df): 
    """
    Beräknar andelen personer med sjukdom.
    """
    amount = df["disease"].sum()
    return amount / len(df)

def probability_simulation(df):
    """
    Simulerar sjukdomsförekomst för 1000 personer.
    """
    people = 1000
    prob = disease_probability(df)
    disease_sim = np.random.choice(
        [0, 1],
        size=people,
        p=[1 - prob, prob]
        )
    return disease_sim
    
def age_bp_regression(df: pd.DataFrame):
    """
    Beräknar linjär regression mellan ålder
    och systoliskt blodtryck.

    Args:
        df: Dataset med hälsodata.

    Returns:
        Lutning och intercept för regressionslinjen.
    """
    slope, intercept = np.polyfit(
        df["age"],
        df["systolic_bp"],
        1
    )

    return slope, intercept

def disease_by_sex(df: pd.DataFrame):
    """
    Beräknar andelen personer med sjukdom uppdelat på kön.

    Args:
        df: Dataset med hälsodata.

    Returns:
        Andelen personer med sjukdom för varje kön.
    """
    return df.groupby("sex")["disease"].mean()


def weight_bp_regression(df: pd.DataFrame):
    """
    Beräknar linjär regression mellan vikt
    och systoliskt blodtryck.
    """
    x = df["weight"]
    y = df["systolic_bp"]

    k, m = np.polyfit(x, y, 1).round(2)

    return k, m



def calculate_bmi(df: pd.DataFrame):
    """
    Beräknar BMI utifrån vikt och längd.
    Längden anges i centimeter.
    """
    height_m = df["height"] / 100
    bmi = df["weight"] / (height_m ** 2)

    return bmi

def bmi_bp(df: pd.DataFrame):
    """
    Beräknar linjär regression mellan BMI
    och systoliskt blodtryck.
    """
    x = calculate_bmi(df)
    y = df["systolic_bp"]

    k, m = np.polyfit(x, y, 1).round(2)

    return k, m