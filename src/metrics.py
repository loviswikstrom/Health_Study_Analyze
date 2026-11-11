import pandas as pd
import numpy as np


Räkna ut medel, median, min och max för: age, weight, height, systolic_bp, cholesterol.

def age_mean(df: pd.DataFrame) -> float:
    return float(df["age"].mean())

def descriptive_statistics(df):
    columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    return df[columns].describe()

# 1. total intäkt
def revenue_sum(data):
    total = round(data["revenue"].sum(), 2)
    return total


# 2. totalt antal enheter.
def units_sum(data):
    units_total = data["units"].sum()
    return units_total


# 3. Average Orde Value (aov)
def aov(data):
    total_revenue = data["revenue"].sum()
    total_orders = data["order_id"].nunique()
    average = round(total_revenue / total_orders, 2)
    return average


# 4. intäkt per kategori.
def category_revenue_table(data):
    category_revenue = (
    data.groupby("category")["revenue"]
    .agg(
        kronor = "sum",
        antal = "count",
        medelvärde = "mean",
        median = "median",
        std = "std"
        )
    .reset_index()
    )  
    return category_revenue









# 8. översikt över intäkt
def revenue_overview(data):
    median = data["revenue"].median()
    minsta = data["revenue"].min()
    hogsta = data["revenue"].max()
    standardavvikelse = data["revenue"].std()

    print("Median:", round(median, 2), "kr")
    print("Lägsta ordervärde:", round(minsta, 2), "kr")
    print("Högsta ordervärde:", round(hogsta, 2), "kr")
    print("Standardavvikelse:", round(standardavvikelse, 2), "kr")


# 9. avvikelser
def outliers_category(data):
    category_revenue = data.groupby("category")["revenue"].sum()
    cmax = category_revenue.idxmax() 
    cmin = category_revenue.idxmin() 
    rmax = round(category_revenue.max(), 2)
    rmin = round(category_revenue.min(), 2)
    return (f"Kategori med högst intäkt: {cmax} med {rmax} kr, \nKategori med lägst intäkt: {cmin} med {rmin} kr")

