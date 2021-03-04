'''
1: class for bank account
2: variable balance
3: method for withdrawing money, depositing money and displaying balance
'''

class bank_account(object):
    def __init__(self):
        self.balance = 0
    def withdraw(self,amount):
        if self.balance < amount:
            print(f"balance is less than the withdrawal amount.\
                    \nyour balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"withdrawal complete.\
                    \nyour balance is {self.balance}")
    def deposit(self,amount):
        self.balance += amount
        print(f"successfully deposited your money.\
                \nyour balance is {self.balance}")
    def disp_balance(self):
        print(f"your balance is {self.balance}")

ent_int = bank_account()

while True:
    entered = input("\nbalance or withdraw or deposit or exit?\n=> ")
    if entered == "balance":
        ent_int.disp_balance()
    elif entered == "withdraw":
        amount = int(input("enter amount to withdraw\n=> "))
        ent_int.withdraw(amount)
    elif entered == "deposit":
        amount = int(input("enter amount to deposit\n=> "))
        ent_int.deposit(amount)
    elif entered == "exit":
        break
    else:
        print("invalid input. please try again.")

