# Python program to create a class BankAccount

class BankAccount:
    def __init__(self,name):
        self.name =name
        self.initial = 1000
        self.balance = 1000

    def __str__(self):
        return self.name
    

class Bank:
    def __init__(self):
        self.accounts = []
        
    def create_account(self,name):
        self.accounts.append(BankAccount(name))
        print(f'Bank Account created for {name}')

    def deposit_money(self,n,money):
        self.accounts[n].balance += money
        print(f'Rs.{money} deposited successfully')

    def withdraw_money(self,n,money):
        if money < self.accounts[n].balance:
            self.accounts[n].balance -= money
            print(f'Rs.{money} withdrawn successfully')
        else:
            print('Insufficient balance!!! Withdrawal failed')

    def display_balance(self,n):
        print(f'Account No.{n + 1}\tAccount Holder : {self.accounts[n].name}\tAccount Balance : {self.accounts[n].balance}')
        

def main():
    acc = Bank()
    print('********Welcome to Banking System**********')
    while True:
        print('\n1.Create Account\n2.Deposit money\n3.Withdraw money\n4.Display Account balance\n5.Exit')
        c = int(input('Enter your choice :'))
        if c == 1:
            name = input('Enter your name : ')
            acc.create_account(name)
        elif c == 2:
            n = int(input('Enter the account number : ')) - 1
    
            while n < 0 or n > len(acc.accounts):
                print('Invalid account number')
                n = int(input('Enter a valid account number : ')) - 1
            money = int(input('Enter amount to deposit : '))
            acc.deposit_money(n,money)
        elif c == 3:
            n = int(input('Enter the account number : ')) - 1
            while n < 0 or n > len(acc.accounts):
                print('Invalid account number')
                n = int(input('Enter a valid account number : ')) - 1
            money = int(input('Enter amount to withdraw : '))
            acc.withdraw_money(n,money)
        elif c == 4:
            n = int(input('Enter the account number : ')) - 1
            while n < 0 or n > len(acc.accounts):
                print('Invalid account number')
                n = int(input('Enter a valid account number : ')) - 1 
            acc.display_balance(n)
        elif c == 5:
            break
        else:
            print('Invalid choice')
            
main()


