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
    max = dataframe["revenue"].max()
    median = dataframe["revenue"].median()
    min = dataframe["revenue"].min()
    return order_tot, revenue_tot, units_tot, aov, max, median, min

# Plockar ut variablerna från funktionen, så kan de användas.
order_tot, revenue_tot, units_tot, aov, max, median, min = order_stat(df)

# Visar hur ordrarna fördelas i olika kostnadsintervall, överst de kostnadsintervall som flest ordrar finns inom:
# Tar man bort sort_values() visas ordnarna i intervallordning istället.
buckets = np.linspace(min, max, 20)

revenue_distr = pd.crosstab(
    df["order_id"],
    pd.cut(df["revenue"], bins=buckets, right=True)
).sum().sort_values(ascending=False)

# print(revenue_distr)