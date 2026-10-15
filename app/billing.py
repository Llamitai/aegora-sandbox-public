"""Fixture derived from Aegora's billing core: metered usage to invoice lines."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class UsageRecord:
    metric: str
    quantity: int
    unit_price: Decimal


def invoice_total(records: list[UsageRecord]) -> Decimal:
    return sum((r.unit_price * r.quantity for r in records), Decimal("0"))


def average_unit_price(records: list[UsageRecord]) -> Decimal:
    quantity = sum(r.quantity for r in records)
    return invoice_total(records) / quantity
