from decimal import Decimal

from app.billing import UsageRecord, average_unit_price, invoice_total


def test_invoice_total_sums_metered_lines():
    records = [UsageRecord("api_calls", 10, Decimal("0.5")), UsageRecord("seats", 2, Decimal("9"))]
    assert invoice_total(records) == Decimal("23")


def test_average_unit_price():
    assert average_unit_price([UsageRecord("api_calls", 4, Decimal("2"))]) == Decimal("2")
