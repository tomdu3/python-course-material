"""
This program reads a file containing bank account information of the clients and creates a list of BankAccount objects.
"""

import json
try:
    from data.bank_account import BankAccount
except ImportError:
    from bank_account import BankAccount
def make_accounts(file):
    """
    Reads a file containing bank account information of the clients and creates a list of BankAccount objects.

    Returns
    -------
    list
        List of BankAccount objects
    """
    accounts = []
    with open(file, "r") as f:
        data = json.load(f)
        for account in data:
            accounts.append(
                BankAccount(
                    account["balance"],
                    account["fname"],
                    account["lname"],
                    account["ssn"],
                )
            )
    return accounts


if __name__ == "__main__":
    bank = make_accounts("customers.json")

    for account in bank:
        print(account)