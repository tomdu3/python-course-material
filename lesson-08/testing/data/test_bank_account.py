import unittest

from bank_account import BankAccount


# Define a test class
class TestBankAccount(unittest.TestCase):

    # test creation of the account
    def test_init(self):
        account = BankAccount(1000, "John", "Doe", "123456789")
        self.assertEqual(account.balance, 1000)
        self.assertEqual(account.fname, "John")
        self.assertEqual(account.lname, "Doe")
        self.assertEqual(account.ssn, "123456789")

    def test_deposit(self):
        account = BankAccount(1000, "John", "Doe", "123456789")
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_withdraw(self):
        account = BankAccount(1000, "John", "Doe", "123456789")
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 500)

    def test_get_balance(self):
        account = BankAccount(1000, "John", "Doe", "123456789")
        self.assertEqual(account.get_balance(), 1000)

    def test_get_name(self):
        """
        Test the `get_name` method of the `BankAccount` class.

        This test case creates a `BankAccount` object with the name "John Doe" and checks if the `get_name` method returns the expected value.

        Parameters:
            self (TestCase): The current test case object.

        Returns:
            None
        """
        account = BankAccount(1000, "John", "Doe", "123456789")
        self.assertEqual(account.get_name(), "John Doe")

    def test_str(self):
        account = BankAccount(1000, "John", "Doe", "123456789")
        self.assertEqual(str(account), "John Doe (123456789): 1000.0")

    if __name__ == "__main__":
        unittest.main()
