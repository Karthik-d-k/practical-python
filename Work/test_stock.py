# test_stock.py

import stock
import unittest

class TestStock(unittest.TestCase):
    """
    Unit tests for `stock` module.
    """
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        old_shares = s.shares
        s.sell(20)
        self.assertEqual(s.shares, (old_shares - 20))

    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'

if __name__ == '__main__':
    unittest.main()
