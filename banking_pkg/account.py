import os
""" 
write 4 functions, named show_balance, deposit, withdraw, and logout.

"""
def show_balance(balance):
    print("\nCurrent balance: $",balance)

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    total = balance + float(amount)
    return total

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Error: Withdrawal amount exceeds current balance.")
    else:
        balance -= amount
        print("Withdrawal successful. Current balance:", balance)
    return balance

def logout(name):
    print('Goodbye', name,"!")
    print("Clearing Screen")
    # clearing screen to remove pii 
    os.system('cls')