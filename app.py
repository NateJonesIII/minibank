from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    
    
print("    === Automated Teller Machine ===    ")

# Loop until the name fits the requirements
while True:
    name = input("Enter name to register: ")
    if len(name) >= 1 and len(name) <= 10:
        print("Name registered successfully!")
        break
    else:
        print("Error: Name must be between 1 and 10 characters.")


pin = input("Enter PIN: ")
balance = 0
print(name, "has been registered with a starting balance of $",balance)

while True:
    # checking to see if entries match entered variables
    name_to_validate = input("Enter Name: ")
    pin_to_validate  = input("Enter PIN: ")
    
    """
    Then, use an if statement that uses the and logical operator to check both conditions: Is the name to validate equal to the name variable, and is the PIN to validate equal to the pin variable?
    """
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
        
while True:
    # display the ATM menu 
    atm_menu(name)
    # variable declaration
    option = input("Choose an option:")
    
    if int(option) == 1:
        account.show_balance(balance)
    elif int(option) == 2:
        dep = account.deposit(balance)
        balance = dep
     
        account.show_balance(balance)
    elif int(option) == 3:
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif int(option) == 4:
        account.logout(name)
        break