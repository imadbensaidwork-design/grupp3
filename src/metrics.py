
import pandas as pd


# 1. FILTRERA DATA
def filter_sales_period(df):
    """Filtrera försäljning januari–juni 2024."""

    # Kopiera data så att originalet inte ändras
    data = df.copy()

    # Konvertera datum från text till datumformat
    data["date"] = pd.to_datetime(data["date"])

    # Behåll endast januari–juni 2024
    data = data[
        (data["date"] >= "2024-01-01") &
        (data["date"] < "2024-07-01")
    ]

    return data


# 2. FÖRSÄLJNING PER MÅNAD
def monthly_sales(df):
    """Beräkna total försäljning per månad."""

    data = filter_sales_period(df)

    # Gruppera efter månad och summera revenue
    monthly = data.groupby(
        data["date"].dt.to_period("M")
    )["revenue"].sum()

    return monthly


# 3. FÖRSÄLJNING PER VECKA
def weekly_sales(df):
    """Beräkna total försäljning per vecka."""

    data = filter_sales_period(df)

    # Gör datum till index och gruppera per vecka
    weekly = (
        data.set_index("date")["revenue"]
        .resample("W-SUN")
        .sum()
    )

    return weekly


# 4. PROCENTUELL FÖRÄNDRING
def monthly_growth(df):
    """Beräkna procentuell förändring mellan månader."""

    monthly = monthly_sales(df)

    # Jämför varje månad med föregående månad
    growth = monthly.pct_change() * 100

    return growth


# 5. SAMMANFATTNING AV FÖRSÄLJNING
def sales_summary(df):
    """Beräkna totala nyckeltal."""

    data = filter_sales_period(df)

    total_revenue = data["revenue"].sum()
    total_orders = data["order_id"].nunique()
    total_units = data["units"].sum()

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_units": total_units
    }


# 6. IDENTIFIERA HÖGSTA OCH LÄGSTA MÅNAD
def sales_trends(df):
    """Identifiera månader med högst och lägst försäljning."""

    monthly = monthly_sales(df)

    if monthly.empty:
        return None

    highest_month = monthly.idxmax()
    lowest_month = monthly.idxmin()

    return {
        "highest_month": str(highest_month),
        "highest_sales": monthly.max(),
        "lowest_month": str(lowest_month),
        "lowest_sales": monthly.min()
    }


# 7. KÖR PROGRAMMET
if __name__ == "__main__":

    # Läs CSV-filen
    df = pd.read_csv("data/ecommerce_sales.csv")

    # Försäljning per månad
    print("\n=== FÖRSÄLJNING PER MÅNAD ===")
    print(monthly_sales(df))

    # Försäljning per vecka
    print("\n=== FÖRSÄLJNING PER VECKA ===")
    print(weekly_sales(df))

    # Procentuell förändring
    print("\n=== MÅNADSFÖRÄNDRING (%) ===")
    print(monthly_growth(df).round(2))

    # Totala nyckeltal
    print("\n=== FÖRSÄLJNINGSSAMMANFATTNING ===")

    summary = sales_summary(df)

    print(f"Total försäljning: {summary['total_revenue']:,.2f}")
    print(f"Antal ordrar: {summary['total_orders']}")
    print(f"Sålda enheter: {summary['total_units']}")

    # Högsta och lägsta försäljningsmånad
    print("\n=== FÖRSÄLJNINGSTRENDER ===")

    trends = sales_trends(df)

    if trends:
        print(
            f"Högsta försäljningsmånad: "
            f"{trends['highest_month']} "
            f"({trends['highest_sales']:,.2f})"
        )

        print(
            f"Lägsta försäljningsmånad: "
            f"{trends['lowest_month']} "
            f"({trends['lowest_sales']:,.2f})"
        )
    else:
        print("Ingen försäljningsdata för perioden.")

