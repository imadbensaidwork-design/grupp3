from pathlib import Path
projektmapp = Path(__file__).resolve().parent.parent
csv_fil = projektmapp / "data" / "ecommerce_sales.csv"

from io_utils import load_data, process_data # importerar funktioner från io_ituls för att kunna läsa och processa data (source: io_utils.py)

# funktion för att beräkna intäkt per produktkategori, sortera kategorierna och ta fram de tre med högst intäkt

def revenue_by_category():

    df = load_data(csv_fil) # läser in csv-filen med funktionen load_data
    df = process_data(df) # konverterar värden i kolumnen "date" från str till datetime med funktionen process_data 

    revenue_by_category = (
    df.groupby("category") # grupperar raderna efter produktkategori
    .agg(totala_intäkter = ("revenue", "sum")) # summerar revenue i varje category, under nya kolumnen "intäkt per produktkategori"
    .reset_index() # gör category till kolumn istället för index
    .sort_values("totala_intäkter", ascending = False) # sorterar värderna under "intäkt per produktkategori i fallande ordning"
    .head(3) # visa första tre
    .reset_index(drop=True)# 
    )

    return revenue_by_category
