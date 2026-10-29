# här tar vi fram funktion för att kunna läsa in csv-filen
import pandas as pd


# funktion för att kunna läsa in CSV-filen
def load_data(file_path):
    """
    Läser in en CSV-fil och returnerar en pandas DataFrame.

    Parametrar file_path är en str som anger sökvägen till CSV-filen.

    """
    df = pd.read_csv(file_path)
    return df


# Funktionen för att göra en copy av DataFrame och konverttera kolumner date
# från str till datetime format
def process_data(df):
    """
    Förbereda DataFrame med först att göra en copy så vi inte andrar orifinalet Dataset
    Sen konvertetra kolumnen date från str till datetime format.

    Parametrar df är en pandas DataFrame.
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df
