
import unittest
import pandas as pd

from src.metrics import (
    monthly_sales,
    weekly_sales,
    monthly_growth,
    sales_summary
)


class TestSalesMetrics(unittest.TestCase):

    def setUp(self):
        # Testdata med kända försäljningsbelopp
        self.df = pd.DataFrame({
            "order_id": [1, 2, 3, 4],
            "date": [
                "2024-01-05",
                "2024-01-06",
                "2024-02-10",
                "2024-07-01"
            ],
            "revenue": [100, 200, 600, 900],
            "units": [1, 2, 3, 4]
        })

    def test_monthly_sales(self):
        result = monthly_sales(self.df)

        self.assertEqual(result.loc["2024-01"], 300)
        self.assertEqual(result.loc["2024-02"], 600)

    def test_weekly_sales(self):
        result = weekly_sales(self.df)

        self.assertEqual(result.loc["2024-01-07"], 300)

    def test_monthly_growth(self):
        result = monthly_growth(self.df)

        self.assertAlmostEqual(
            result.loc["2024-02"], 100.0
        )

    def test_sales_summary(self):
        result = sales_summary(self.df)

        self.assertEqual(result["total_revenue"], 900)
        self.assertEqual(result["total_orders"], 3)
        self.assertEqual(result["total_units"], 6)


if __name__ == "__main__":
    unittest.main()
