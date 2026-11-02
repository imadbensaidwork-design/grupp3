from src.io_utils import load_data, process_data

def monthly_sales(df):
    """Beräkna försäljning per månad."""

    monthly = df.groupby(
        df["date"].dt.to_period("M")
    )["revenue"].sum()

    return monthly


def weekly_sales(df):
    """Beräkna försäljning per vecka."""

    weekly = (
        df.set_index("date")["revenue"]
        .resample("W-SUN")
        .sum()
    )

    return weekly


def monthly_growth(df):
    """Beräkna procentuell förändring per månad."""

    monthly = monthly_sales(df)

    growth = monthly.pct_change() * 100

    return growth


def sales_trends(df):
    """Identifiera högsta och lägsta försäljningsmånad."""

    monthly = monthly_sales(df)

    if monthly.empty:
        return None

    return {
        "highest_month": str(monthly.idxmax()),
        "highest_sales": monthly.max(),
        "lowest_month": str(monthly.idxmin()),
        "lowest_sales": monthly.min()
    }


if __name__ == "__main__":

    # Läs in CSV-filen via io_utils.py
    df = load_data("data/ecommerce_sales.csv")

    # Förbered datumkolumnen via io_utils.py
    df = process_data(df)

    print("\n=== FÖRSÄLJNING PER MÅNAD ===")
    print(monthly_sales(df))

    print("\n=== FÖRSÄLJNING PER VECKA ===")
    print(weekly_sales(df))

    print("\n=== MÅNADSFÖRÄNDRING (%) ===")
    print(monthly_growth(df).round(2))

    print("\n=== FÖRSÄLJNINGSTRENDER ===")
    print(sales_trends(df))
