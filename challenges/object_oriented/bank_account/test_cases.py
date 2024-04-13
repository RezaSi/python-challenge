import os
import sys
import unittest

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now you can import the BankAccount class from solution.py
from solution import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw(self):
        self.account.deposit(200)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 150)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

if __name__ == '__main__':
    unittest.main()
