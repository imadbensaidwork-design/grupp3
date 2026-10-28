import pandas as pd
import numpy as np
import matplotlib as mplt

df = pd.read_csv("data/ecommerce_sales.csv")

# Beräkna total intäkt, totalt antal sålda enheter, antal ordrar och AOV (genomsnittligt ordervärde). 
# Undersök hur ordervärdena varierar (t.ex. median, lägsta och högsta värde). Skapa minst en egen beräkningsfunktion och skriv en kort slutsats. 
#  order_id        date       city     category   price  units  revenue
 
# Funktion för att plocka ut orderstatistik:
def order_stat(dataframe):
    order_tot = dataframe["order_id"].count()
    revenue_tot = dataframe["revenue"].sum()
    units_tot = dataframe["units"].sum()
    aov = (dataframe["revenue"].sum() / len(dataframe)).round(2)
    revenue_max = dataframe["revenue"].max()
    revenue_median = dataframe["revenue"].median()
    revenue_min = dataframe["revenue"].min()
    return order_tot, revenue_tot, units_tot, aov, revenue_max, revenue_median, revenue_min

# Plockar ut variablerna från funktionen, så kan de användas.
order_tot, revenue_tot, units_tot, aov, revenue_max, revenue_median, revenue_min = order_stat(df)

# Visar hur ordrarna fördelas i olika kostnadsintervall, överst de kostnadsintervall som flest ordrar finns inom:
# Tar man bort sort_values() visas ordnarna i intervallordning istället.
buckets = np.linspace(revenue_min, revenue_max, 20)

revenue_distr = pd.crosstab(
    df["order_id"],
    pd.cut(df["revenue"], bins=buckets, right=True, include_lowest=True)
).sum().sort_values(ascending=False)

# Beräkna och jämför intäkterna för de fem städerna. Visa vilka städer som säljer mest och minst

# FUNKTION 3: Beräknar den totala intäkten för varje stad och sorterar resultaten från högst till lägst.
def calculate_city_revenue(df):
    revenue_by_city = (
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )
    return revenue_by_city

city_revenue = calculate_city_revenue(df)

# FUNKTION 4: Jämför städernas totala intäkter.
def compare_city_revenue(city_revenue):

    highest_city = city_revenue.index[0] # Identifierar staden med högst intäkt.
    lowest_city = city_revenue.index[-1] # Identifierar staden med lägst intäkt.

    highest_revenue = city_revenue.iloc[0] 
    lowest_revenue = city_revenue.iloc[-1] 

    revenue_difference = highest_revenue - lowest_revenue # Beräknar skillnaden mellan den högsta och lägsta intäkten.
    revenue_ratio = highest_revenue / lowest_revenue # Beräknar hur många gånger högre den högsta intäkten är jämfört med den lägsta.

    return {
        "highest_city": highest_city,
        "highest_revenue": highest_revenue,
        "lowest_city": lowest_city,
        "lowest_revenue": lowest_revenue,
        "revenue_difference": revenue_difference,
        "revenue_ratio": revenue_ratio
    }

# Anropar funktionen och sparar resultatet.
comparison = compare_city_revenue(city_revenue)

# FUNKTION 5: Skriver ut en sammanfattning av intäkterna per stad.
def print_city_revenue_summary(comparison):

    def format_number(number):
        return f"{number:,.2f}".replace(",", "X").replace(".", ",").replace("X", " ")

    print(f"Staden med högst intäkt: {comparison['highest_city']}, {format_number(comparison['highest_revenue'])} kr")
    print(f"Staden med lägst intäkt: {comparison['lowest_city']}, {format_number(comparison['lowest_revenue'])} kr")
    print(f"Skillnad: {format_number(comparison['revenue_difference'])} kr")
    print(f"Förhållande: {format_number(comparison['revenue_ratio'])}")

print_city_revenue_summary(comparison)
