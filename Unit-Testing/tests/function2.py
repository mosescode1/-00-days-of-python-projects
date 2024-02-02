class InsufficientFund(Exception):
    pass

class BankAccount:
    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be less than 0 naira")
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("You can't Deposit 0 Naira")
        self._balance += amount
        
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdraw amount must be more than 0")
        if self._balance < amount:
            raise InsufficientFund("You have Insufficient Fund")
        self._balance -= amount
        return self._balance
        
