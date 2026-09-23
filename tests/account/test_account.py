import unittest
from src.account.account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.acc = Account("winifred")

    def test_account_creation(self):
        # acc = Account("winifred")
        self.assertEqual(self.acc.name, "winifred")
        self.assertEqual(self.acc.balance, 0)

    def test_account_can_receive_deposit(self):
        # acc = Account("winifred")
        self.acc.deposit(2500)
        self.assertEqual(self.acc.balance, 2500)

    def test_account_cannot_receive_negative_deposit(self):
        self.assertRaises(ValueError, self.acc.deposit, -2500)

    def test_account_cannot_receive_yet_another_negative_deposit(self):
        # acc = Account("winifred")
        self.assertRaises(ValueError, self.acc.deposit, -500)

    def test_account_cannot_withdraw_more_than_balance(self):
        # acc = Account("winifred")
        self.acc.deposit(2500)
        self.assertRaises(ValueError, self.acc.withdraw, 3500)

    def test_account_cannot_withdraw_from_zero_balance(self):
        # acc = Account("winifred")
        self.assertRaises(ValueError, self.acc.withdraw, 500)

    if __name__ == "__main__":
        unittest.main()


