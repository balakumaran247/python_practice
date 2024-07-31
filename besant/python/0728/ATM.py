"""
Problem: Simulate a simple ATM machine where a user can perform multiple transactions until they choose to exit.
"""

balance = float(input("enter the initial amount in the account: "))

while True:
    choice = input("deposit / withdraw / balance / exit: ").lower()
    if choice == "deposit":
        option = float(input("please enter the amount to deposit: "))
        balance += option
        print(f"Amount of Rs.{option} deposited in account, balance: {balance}")
    elif choice == "withdraw":
        option = float(input("please enter the amount to withdraw: "))
        balance -= option
        print(f"Amount of Rs.{option} withdrawn from account, balance: {balance}")
    elif choice == "balance":
        print(f"Account balance: {balance}")
    elif choice == "exit":
        break
    else:
        print("Invalid operation")
