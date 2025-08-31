# Import the random module to generate random account numbers
import random

# Define the BankAccount class to represent a single bank account
# Class attributes: account_number, name, balance
# Class methods: deposit, withdraw, check_balance, save_transaction
class BankAccount:
    # __init__ method: runs when a new account is created
    # Initializes account_number, name, and opening balance
    def __init__(self,account_number,name, balance):
        self.account_number =  account_number
        self.name =name
        self.balance = balance
    
    # deposit method: adds money to the account
    # Check that amount is greater than 0
    # Update balance
    # Call save_transaction to record this deposit

    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"Amount Deposited : {amount}\nAccount Balance : {self.balance}")
            self.save_transaction("Deposit",amount)
        else:
            print("Enter Valid Amount greater than 0.")
    
    # withdraw method: removes money from the account
    # Check that amount is greater than 0 and less than or equal to balance
    # Update balance
    # Call save_transaction to record this withdrawal
    # If insufficient funds, print a message

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Amount Withdrawn : {amount}\nAccount Balance : {self.balance}")
                self.save_transaction("Withdraw",amount)
            else:
                print("Insufficient funds.")
        else: 
            print("Enter Valid Amount greater than 0.")

    # check_balance method: prints the current balance for the account

    def check_balance(self):
        print(f"Account Balance : {self.balance}")

    # save_transaction method: logs transaction to a file
    # Open a file in append mode
    # Write account number, name, action (deposit/withdraw), amount, new balance

    def save_transaction(self,action,amt):
        with open("Accounts.txt",'a') as file:
            file.write(f"{self.account_number},{self.name},{action},{amt},{self.balance}\n")

# Create a dictionary named accounts to store all accounts
# Use account_number as the key and BankAccount object as the value

Accounts = {}

# Start an infinite loop to run the CLI menu
# Print a welcome message and menu options: Create, Deposit, Withdraw, Check Balance, Exit
in_app=True
while in_app:
    print("="*25)
    print("WELCOME TO DVS BANK")
    print("="*25)
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    print("="*25)
    
    # Use try-except to handle invalid input for menu choice (ValueError)
    try:
        choice = int(input("Enter Your Choice : "))
    except ValueError:
        print("Enter a valid Number.")
        continue

    # Option 1: Create Account
    # Ask for user's name
    # Ask for opening balance
    # Convert opening balance to float
    # Generate a random account number
    # Create a BankAccount object and store in accounts dictionary
    # Print confirmation message with account number

    if choice == 1:
        name =input("Enter Name : ")
        ob = input("Enter Opening Balance : ")
        try:
            ob= float(ob)
            account_number = random.randint(10000,99999)
            account = BankAccount(account_number,name,ob)
            Accounts[account_number]= account
            print(f"Account created successfully! Your account number is {account_number}")
        except:
            print("Invalid Opening balance")
            continue

    # Option 2: Deposit
    # Ask for account number and deposit amount
    # Convert inputs to correct types (int, float)
    # Check if account exists in accounts dictionary
    # Call deposit method on the account object
    # If account not found, print error message

    elif choice == 2:
        account_number = input("Enter Account Number : ")
        amt = input("Enter Amount to Deposit : ")
        try:
            account_number = int(account_number)
            amt = float(amt)
            if account_number in Accounts:
                Accounts[account_number].deposit(amt)
            else:
                print("Account Number Not found")
        except ValueError:
            print("Invalid input!")
            continue

    # Option 3: Withdraw
    # Ask for account number and withdrawal amount
    # Convert inputs to correct types (int, float)
    # Check if account exists in accounts dictionary
    # Call withdraw method on the account object
    # If account not found, print error message

    elif choice == 3:
        account_number = input("Enter Account Number : ")
        amt = input("Enter Amount to Withdraw : ")
        try:
            account_number = int(account_number)
            amt = float(amt)
            if account_number in Accounts:
                Accounts[account_number].withdraw(amt)
            else:
                print("Account Number Not found")
        except ValueError:
            print("Invalid input!")
            continue
    # Option 4: Check Balance
    # Ask for account number
    # Convert input to int
    # Check if account exists
    # Call check_balance method
    # If account not found, print error message

    elif choice == 4:
        try:
            account_number = int(input("Enter Account number : "))
            if account_number in Accounts:
                Accounts[account_number].check_balance()
            else:
                print("Account Number Not found")
        except:
            print("Invalid input!")
            continue

    # Option 5: Exit
    # Break the loop and end the program
    
    elif choice == 5:
        print("Thank you for banking with us!")
        in_app = False

    # Handle invalid menu choices (anything other than 1-5)
    # Print a message asking user to enter a valid option

    else:
        print("Invalid choice! Please select 1-5.")

