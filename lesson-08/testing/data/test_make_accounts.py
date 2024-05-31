import unittest

from make_accounts import make_accounts
from bank_account import BankAccount

# test the function that makes a list of BankAccount objects
class TestMakeAccounts(unittest.TestCase):
    def test_make_accounts(self):
        accounts = make_accounts("data/customers.json")
        self.assertIsInstance(accounts, list)
        self.assertIsInstance(accounts[0], BankAccount)

        for account in accounts:
            self.assertIsInstance(account, BankAccount)
    def test_make_accounts_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            make_accounts("data/customers_not_found.json")

if __name__ == "__main__":
    unittest.main()