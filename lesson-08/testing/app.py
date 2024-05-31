from data.bank_account import BankAccount
from data.make_accounts import make_accounts
from aux.welcome import welcome, print_accounts, goodbye


def main():
    """
    Main function
    """
    bank = make_accounts("data/customers.json")
    welcome()
    print_accounts(accounts=bank)
    goodbye()


if __name__ == "__main__":
    main()

