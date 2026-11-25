import matplotlib.pyplot as plt
import metrics
import numpy as np


def scat_age_bp(df):
    """
    Skapar ett spridningsdiagram över ålder och systoliskt blodtryck
    med linjär regressionslinje.
    """

    plt.scatter(df["age"], df["systolic_bp"], alpha=0.5)
    plt.title("Samband mellan ålder och systoliskt blodtryck")
    plt.xlabel("Ålder")
    plt.ylabel("Systoliskt blodtryck")

    slope, intercept = metrics.age_bp_regression(df)

    x = df["age"]
    y = df["systolic_bp"]
    k, m = np.polyfit(x, y, 1).round(2)

    plt.plot(x, k*x + m, color="red", alpha=0.5)

    plt.show()
    print("Det förväntade systoliska blodtrycket ökar med cirka", k, "mmHg / år.")




def bar_disease_sex(df):
    """
    Visar andelen personer med sjukdom uppdelat på kön.
    """

    disease_rates = metrics.disease_by_sex(df)
    disease_rates = disease_rates.rename({
        "F": "Kvinnor",
        "M": "Män"
    }) *100
    disease_rates.plot(
    kind="bar",
    color="pink",
    edgecolor="red",
    figsize=(7,6)
    )

    plt.title("Sjukdomsförekomst per kön")
    plt.xlabel("Kön")
    plt.ylabel("Andel med sjukdom (%)")
    plt.xticks(rotation=0)
    plt.ylim(0, 10)
    plt.bar_label(plt.gca().containers[0], fmt="%.1f%%")
    plt.tight_layout()
    plt.grid(axis="y")
    plt.show()



def weight_by_sex(df):
    """
    Låddiagram som visar viktfördelningen mellan könen.
    """
    fig, ax = plt.subplots()
    df.boxplot(column="weight", by="sex", ax=ax, color="red")

    fig.suptitle("Viktfördelning per kön")
    ax.set_title("")
    ax.set_xlabel("Kön")
    ax.set_ylabel("Vikt (kg)")
    plt.show()




def hist_bp(df):
    """
    Histogram som visar fördelningen av
    systoliskt blodtryck bland deltagarna.
    Med linje för medelvärde.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df["systolic_bp"], bins=20, color="pink", edgecolor="red")
    mean_bp = df["systolic_bp"].mean()
    plt.axvline(mean_bp, color="red", linestyle="--", label=f"Medelvärde: {mean_bp:.2f}")
    plt.legend()
    plt.title("Fördelning av systoliskt blodtryck")
    plt.xlabel("Systoliskt blodtryck (mmHg)")
    plt.ylabel("Antal deltagare")
    plt.grid(axis="y")
    plt.show()




def bar_smoker(df):
    """
    Stapeldiagram som visar andelen rökare och icke-rökare,
    procentuellt.
    """
    smoker_percent = df["smoker"].value_counts(normalize=True) * 100
    smoker_percent = smoker_percent.rename({
    "No": "Icke-rökare",
    "Yes": "Rökare"
    })
    smoker_percent.plot(
    kind="bar",
    color="pink",
    edgecolor="red",
    figsize=(7,6)
    )
    plt.grid(axis="y")
    plt.title("Fördelning rökare/icke rökare")
    plt.xlabel("Rökvanor")
    plt.ylabel("Andel (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=0)
    plt.bar_label(plt.gca().containers[0], fmt="%.1f%%")
    plt.tight_layout()
    plt.show()



def scat_weight_bp(df):
    """
    Skapar ett spridningsdiagram för sambandet mellan
    vikt och systoliskt blodtryck med regressionslinje.
    """

    plt.scatter(df["weight"], df["systolic_bp"], alpha=0.5)
    plt.title("Samband mellan vikt och systoliskt blodtryck")
    plt.xlabel("Vikt (kg)")
    plt.ylabel("Systoliskt blodtryck")

    k, m = metrics.weight_bp_regression(df)

    x = df["weight"]
    plt.plot(x, k*x + m, color="red", alpha=0.5)

    plt.show()

    print("Det förväntade systoliska blodtrycket ökar med cirka", k, "mmHg / kg.")


def scat_bmi_bp(df):
    """
    Visar sambandet mellan BMI och systoliskt blodtryck.
    """

    bmi = metrics.calculate_bmi(df)

    plt.scatter(bmi, df["systolic_bp"], alpha=0.5)
    plt.title("Samband mellan BMI och systoliskt blodtryck")
    plt.xlabel("BMI")
    plt.ylabel("Systoliskt blodtryck")

    plt.axvline(25, color="red", linestyle="--", label="Gräns för övervikt")

    k, m = metrics.bmi_bp(df)

    plt.plot(bmi, k * bmi + m, color="red", alpha=0.5)
    plt.legend()
    plt.show()
    print("För varje ökning med 1 BMI-enhet förändras det förväntade systoliska blodtrycket med cirka", k, "mmHg.")