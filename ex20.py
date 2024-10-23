class  InsufficientFundsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.massage)

class BankAccount:
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self, message = "amount is more than balance")
        self.balance -= amount

    def check_balance(self):
        print(f"balance of your account ---> {self.balance}")

    def transfer_to(self, another_account, amount):
        if self.balance < amount:
            raise InsufficientFundsError(self, message = "amount is more than balance")
        self.withdraw(amount)
        another_account.deposit(amount)
        print(f"Transferred {amount} to {another_account.account_holder} .... New balance ---> {self.balance}")

if __name__ == "__main__":
    a1 = BankAccount("mahshad", 2000, "1")
    a1.check_balance()
    a1.deposit(200)
    print(a1.balance)


