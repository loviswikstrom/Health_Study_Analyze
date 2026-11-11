import pandas as pd
import matplotlib.pyplot as plt
import viz
import metrics

class HealthAnalyzer:
    """
    Metoder för att förbereda inför analys för
    de frågor vi vill svar på
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()