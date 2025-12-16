class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        elif amount > self.__balance:
            print(f"Insufficient funds! Available: ${self.__balance:.2f}")
            return False
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
    
    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print(f"Initial balance: ${account.get_balance():.2f}")

account.deposit(500)
account.withdraw(-2000) 
print(f"Final balance: ${account.get_balance():.2f}")