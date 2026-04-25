class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful:", amount)
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Current balance:", self.balance)


atm = ATM(1000)
atm.withdraw(500)
atm.withdraw(700)
atm.show_balance()