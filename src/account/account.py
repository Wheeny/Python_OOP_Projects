class Account:
    def __init__(self, name:str) -> None:
        self.name = name.lower()
        self.balance = 0

    def deposit(self, amount) -> None:
        if amount < 0:
            raise ValueError("Deposit cannot be negative")
        self.balance += amount

    def withdraw(self, amount) -> None:
        if amount > self.balance:
            raise ValueError("Withdraw cannot be greater than balance")
        self.balance -= amount

