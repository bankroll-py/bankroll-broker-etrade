from bankroll.model import (
    AccountBalance,
    Cash,
    Currency,
    Stock,
    Bond,
    Option,
    OptionType,
    Position,
    CashPayment,
    Trade,
    TradeFlags,
)
import bankroll.brokers.etrade as etrade
from datetime import date
from decimal import Decimal
from itertools import groupby
from pathlib import Path

# from tests import helpers
import unittest


class TestEtradePositions(unittest.TestCase):
    def setUp(self) -> None:
        return

    def test_positionValidity(self) -> None:
        self.assertEqual(1,0)

if __name__ == "__main__":
    unittest.main()
