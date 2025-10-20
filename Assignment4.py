# Python program to create a class BankAccount

class BankAccount:
    
    # Creating an account with an initial balance
    def __init__(self,name,initial):
        self.name = name
        self.balance = initial
        print(f'Bank account created for {name} with an initial balance of {initial}')
    
    # Depositing money
    def deposit(self,amount):
        self.balance += amount
        print(f'Deposited Rs.{amount}.. New  Balance: Rs.{self.balance}')
    
    # Withdrawing money (only if enough balance is available)
    def withdraw(self,draw):
        if draw <= self.balance:
            self.balance -= draw
            print(f'Withdrew Rs.{draw}..New  Balance: {self.balance}')
        else:
            print('Insufficient balance!!! Withdrawal failed')
    
    # Displaying the account balance
    def display(self):
        print('Available balance: ',self.balance)

# Creating an object and invoking methods

acc = BankAccount('Sajmiya',1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)
acc.display()
