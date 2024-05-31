'''
Displays a welcome message and goodbye message for the banking system.
'''

import pyfiglet

def welcome():
    """
    Display welcome message
    """
    print(pyfiglet.figlet_format("Welcome to the Bank!", font="slant"))
    print()
    print()


def print_accounts(accounts):
    """
    Prints accounts
    
    Parameters
    ----------
    accounts: list
        List of BankAccount objects

    """
    print(">" * 15, "Accounts", "<" * 15)
    print()
    print("Here's the list of accounts in the bank:")
    print("--" * 20)
    for account in accounts:
        print(account)
        print("--" * 20)


def goodbye():
    """
    Display goodbye message
    """
    print(pyfiglet.figlet_format("Goodbye!", font="slant"))
    print("Have a nice day!")
