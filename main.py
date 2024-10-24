from Accounts import CheckingAccount,SavingsAccount
from Customers import Customer


if __name__ == "__main__":
    customer1 = Customer("John Doe", "john@example.com")
    
    checking_account = CheckingAccount(account_number="CHK001", balance=1000,)
    savings_account = SavingsAccount(account_number="SAV001", balance=500)

    customer1.add_account(checking_account)
    customer1.add_account(savings_account)

    print("Accounts and Balances:", customer1.view_accounts())

    checking_account.deposit(200)
    print("Checking Account Balance after deposit:", checking_account.balance)

    savings_account.withdraw(100)
    print("Savings Account Balance after withdrawal:", savings_account.balance)

    customer1.transfer_funds(checking_account, savings_account, 150)
    print("After transfer:")
    print("Checking Account Balance:", checking_account.balance)
    print("Savings Account Balance:", savings_account.balance)

    print("Checking Account Transactions:")
    for transaction in checking_account.transcation:
        print(transaction)

    print("Savings Account Transactions:")
    for transaction in savings_account.transcation:
        print(transaction)
