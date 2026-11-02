
import unittest
import pandas as pd

from src.io_utils import process_data
from src.metrics import (
    monthly_sales,
    weekly_sales,
    monthly_growth,
    sales_trends
)


class TestSalesMetrics(unittest.TestCase):

    def setUp(self):
        """Skapa testdata före varje test."""
        raw_df = pd.DataFrame({
            "order_id": [1, 2, 3],
            "date": [
                "2024-01-05",
                "2024-01-06",
                "2024-02-10"
            ],
            "revenue": [100, 200, 600],
            "units": [1, 2, 3]
        })

        self.df = process_data(raw_df)

    def test_monthly_sales(self):
        """Testa försäljning per månad."""
        result = monthly_sales(self.df)

        self.assertEqual(result.loc["2024-01"], 300)
        self.assertEqual(result.loc["2024-02"], 600)

    def test_weekly_sales(self):
        """Testa försäljning per vecka."""
        result = weekly_sales(self.df)

        self.assertEqual(result.loc["2024-01-07"], 300)

    def test_monthly_growth(self):
        """Testa procentuell förändring per månad."""
        result = monthly_growth(self.df)

        self.assertAlmostEqual(
            result.loc["2024-02"],
            100.0
        )

    def test_sales_trends(self):
        """Testa högsta och lägsta försäljningsmånad."""
        result = sales_trends(self.df)

        self.assertEqual(result["highest_month"], "2024-02")
        self.assertEqual(result["highest_sales"], 600)

        self.assertEqual(result["lowest_month"], "2024-01")
        self.assertEqual(result["lowest_sales"], 300)


if __name__ == "__main__":
    unittest.main()
