# Function Tests Program
# Project 2: Barista Coffee Assistant
#
# Name: Tyler Baxter
# Section: 03
# Date: 01/24/22
#
from baristaCoffeeFuncs import *
import unittest


class MyTestCase(unittest.TestCase):

    def test_order_price(self):
        self.assertEqual(order_price("flat white", "n", "large"), 3.75)
        self.assertEqual(order_price("flat white", "n", "medium"), 3.00)
        self.assertEqual(order_price("flat white", "n", "small"), 2.95)

        self.assertEqual(order_price("americano", "n", "large"), 3.25)
        self.assertEqual(order_price("americano", "n", "medium"), 2.95)
        self.assertEqual(order_price("americano", "n", "small"), 2.75)
        self.assertEqual(order_price("americano", "y", "large"), 3.50)
        self.assertEqual(order_price("americano", "y", "medium"), 3.20)
        self.assertEqual(order_price("americano", "y", "small"), 3.00)

        self.assertEqual(order_price("espresso", "n", "large"), 3.25)
        self.assertEqual(order_price("espresso", "n", "medium"), 2.95)
        self.assertEqual(order_price("espresso", "n", "small"), 2.75)
        self.assertEqual(order_price("espresso", "y", "large"), 3.50)
        self.assertEqual(order_price("espresso", "y", "medium"), 3.20)
        self.assertEqual(order_price("espresso", "y", "small"), 3.00)

        self.assertEqual(order_price("latte", "n", "large"), 4.15)
        self.assertEqual(order_price("latte", "n", "medium"), 3.75)
        self.assertEqual(order_price("latte", "n", "small"), 2.85)


if __name__ == '__main__':
    unittest.main()
