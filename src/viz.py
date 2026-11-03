from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "ecommerce_sales.csv" #skapar sökväg till csv-filen


def plot_revenue_by_category(data: pd.DataFrame) -> tuple[Figure, Axes]: #skapar ett diagram som visar intäkter för varje produktkategori
    revenue = (
        data.groupby("category")["revenue"] #grupperar data efter kategori
        .sum() # summerar intäkterna för varje kategori
        .sort_values(ascending=False) #sorterar från högst till lägst
    )

    fig, ax = plt.subplots() #skapar en figur
    ax.bar(revenue.index, revenue.values) # ritar ett stapeldiagram med kategorier på x-axeln och intäkter på y-axeln
    ax.set_title("Intäkt per produktkategori") #titel och etikett
    ax.set_xlabel("Kategori") #titel och etikett
    ax.set_ylabel("Total intäkt (kr)") #titel och etikett
    ax.grid(True, axis="y") #hjälplinjer för y-axeln
    fig.tight_layout() # ser till att allt får plats i figuren
    return fig, ax # returnerar figuren.


def plot_sales_over_time(data: pd.DataFrame) -> tuple[Figure, Axes]: #skapar ett diagram som visar försäljning över tid
    dated_data = data.assign(date=pd.to_datetime(data["date"], errors="coerce")) # konverterar kolumnen "date" till datetime-format och hanterar eventuella fel genom att sätta dem som NaT (Not a Time)
    monthly_revenue = (
        dated_data.dropna(subset=["date"]) #tar bort rader med NaT i kolumnen "date"
        .groupby(pd.Grouper(key="date", freq="MS"))["revenue"] #grupperar data efter månad
        .sum() #summerar intäkterna för varje månad
    )

    fig, ax = plt.subplots() #skapar en figur
    ax.plot(monthly_revenue.index, monthly_revenue.values, marker="o") #ritar en linje med punkter för varje månad och intäkter
    ax.set_title("Försäljning över tid") #titel och etikett
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt (kr)")
    ax.grid(True) #ritar ett rutnät i bakgrunden
    fig.tight_layout() # ser till att allt får plats i figuren
    return fig, ax # returnerar figuren.


def main() -> None: # huvudfunktionen som kör programmet
    data = pd.read_csv(DATA_FILE) #läser in csv-filen med pandas och lagrar den i variabeln data
    plot_revenue_by_category(data) # skapar ett diagram som visar intäkter för varje produktkategori
    plot_sales_over_time(data) # skapar ett diagram som visar försäljning över tid
    plt.show() # visar diagrammen i ett fönster


if __name__ == "__main__": # kör main-funktionen
    main() 
