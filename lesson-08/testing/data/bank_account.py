"""
This program is providing a class named BankAccount that has the following methods:
• __init__(balance, fname, lname, ssn)
• deposit(amount)
• withdraw(amount)
• get_balance()

The program should be able to test the methods in the BankAccount class using unittest.
"""


class BankAccount:
    """
    Represent a bank account

    ...

    Attributes
    ----------
    balance : float
        The account balance
    fname : str
        The account owner's first name
    lname : str
        The account owner's last name
    ssn : str
        The account owner's social security number

    Methods
    -------
    deposit(amount)
    withdraw(amount)
    get_balance()
    get_name()
    __str__()
    """

    def __init__(self, balance, fname, lname, ssn):
        """
        Constructs all the necessary attributes for the BankAccount object.

        Parameters
        ----------
        balance : float
            The account balance
        fname : str
            The account owner's first name
        lname : str
            The account owner's last name
        ssn : str
            The account owner's social security number
        """
        self.balance = float(balance)
        self.fname = fname
        self.lname = lname
        self.ssn = ssn

    def deposit(self, amount):
        """
        Add an amount to the balance

        Parameters
        ----------
        amount : float
            The amount to deposit
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Subtract an amount from the balance

        Parameters
        ----------
        amount : float
            The amount to withdraw
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self):
        """
        Return the account balance

        Returns
        -------
        float
            The account balance
        """

        return self.balance

    def get_name(self):
        """
        Return the account owner's full name

        Returns
        -------
        str
            The account owner's full name
        """
        return f"{self.fname} {self.lname}"

    def __str__(self):
        """
        Return the account owner's full name and account balance

        Returns
        -------
        str
            The account owner's full name, account owner's social security number and account balance
        """
        return f"{self.fname} {self.lname} ({self.ssn}): {self.balance}"


if __name__ == "__main__":
    bank_account1 = BankAccount(100, "John", "Doe", "123-45-6789")
    bank_account2 = BankAccount(200, "Jane", "Doe", "987-65-4321")

    print(bank_account1)
    print(bank_account2)

    bank_account1.deposit(50)
    bank_account2.withdraw(100)

    print(bank_account1)
    print(bank_account2)

    # assert values from init
    assert bank_account1.get_balance() == 150
    assert bank_account2.get_balance() == 100

    # assert values from methods
    assert bank_account1.get_name() == "John Doe"
    assert bank_account2.get_name() == "Jane Doe"

    # assert values from __repr__
    assert bank_account1 == "John Doe (123-45-6789): 150"
    assert bank_account2 == "Jane Doe (987-65-4321): 100"
