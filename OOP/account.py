class Account:
    def __init__(self, name):
        self.name= name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self, amount):
        self.deposits.append(amount)
        balance = self.get_balance() 
        return f"Confirmed, you have received {amount} new balance is {balance}" 

    def get_balance(self, withdraws):
        self.withdrawals.append(withdraws)
        balance = self.deposits - self.withdraws
        return  balance    