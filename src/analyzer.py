import pandas as pd
import metrics
import viz

class HealthAnalyzer:
    """
    En klass som samlar metoder för att förbereda och genomföra analys för de frågor vi vill svar på i hälsodata.
    Använder funktioner från metrics.py samt viz.py för beräkningar och visualiseringar.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Sparar en kopia av datasetet i klassen.
        """
        self.data = data.copy()

    def get_summary(self):
        """
        Hämtar beskrivande statistik från datasetet.
        """
        return metrics.descriptive_statistics(self.data)

    def scat_age_bp(self):
        """
        Visar sambandet mellan ålder och systoliskt blodtryck.
        """
        viz.scat_age_bp(self.data)

    def bar_disease_sex(self):
        """
        Visar sjukdomsförekomst uppdelat på kön.
        """
        viz.bar_disease_sex(self.data)