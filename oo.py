def menu():
    print("1.Create Account")
    print("2.Search Account")
    print("3.Display All Accounts")
    print("4.Deposit")
    print("5.Withdraw")
    print("6.Delete Account")
    print("7.EXIT")

class BankAccount:

    def __init__(self,customer_name,account_no,balance,account_type):
        self.customer_name = customer_name
        self.account_no = account_no
        self.balance = balance
        self.account_type = account_type
    
    def display_details(self):
        print(f"Name:{self.customer_name}")
        print(f"Account Number:{self.account_no}")
        print(f"Balance:{self.balance}")
        print(f"Account Type:{self.account_type}")
    
    def deposit_calculation(self,amount):
        self.balance = self.balance + amount
    
    def withdraw_calculation(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            
def generate_account_no(bank):
    highest_account_no = 101
    for account in bank:
        if account.account_no > highest_account_no:
            highest_account_no = account.account_no
    return highest_account_no + 1

def validate_deposit(deposit):
    if deposit < 50 or deposit != round(deposit,2):
        return False
    return True

def validate_name(customer_name):
    for letters in customer_name:
        if not letters.isalpha() and not letters == " ":
            return False
    return True

def validate_delete(balance):
    if balance < 0 or balance > 0:
        return False
    return True

def create_account(bank):
    while True:
        name = input("Enter new customer name:").strip()
        if name == "":
            print("Do not leave name field blank")
            continue 
        if not validate_name(name):
            print("Enter a fullname correctly using letters and spacebar!")
            continue 
        break 
    while True:
        try:
            deposit = float(input("Enter a deposit"))
            if not validate_deposit(deposit):
                print("A minimum £50 deposit!")
                continue 
            break 
        except ValueError:
            print("No alphabet, enter a deposit numerically only!")
            continue 

    account_no = generate_account_no(bank)
    account_type = "Current"

    new_account = BankAccount(
        name,
        account_no,
        deposit,
        account_type
    )
    bank.append(new_account)
    new_account.display_details()

def search_account(bank):
    found = False
    user_entry = int(input("To search, enter an account number:"))
    for account in bank:
        if user_entry != account.account_no:
            continue 
        else:
            found = True
            account.display_details()
            print("Account found")
            break 
    if found == False:
        print("Account not found")

def display_every_account(bank):
    for account in bank:
            account.display_details()

def deposit(bank):
    found = False
    account_number = int(input("To deposit, enter account_number:"))
    for account in bank:
        if account_number == account.account_no:
            found = True
            account.display_details()
            answer = input("Do you want to deposit?").lower()
            if answer == "y":
                deposit = float(input("Enter Deposit:"))
                account.deposit_calculation(deposit)
                account.display_details()
    if found == False:
        print("Account not found")

def withdraw(bank):
    found = False
    account_number= int(input("To withdraw, enter account number:"))
    for account in bank:
        if account_number == account.account_no:
            found = True
            account.display_details()
            answer = input("Are you sure you want to withdraw:").lower()
            if answer == "y":
                withdraw = float(input("Enter withdrawal?"))
                account.withdraw_calculation(withdraw)
                account.display_details()
    if found == False:
        print("Account not Found")

def delete_account(bank):
    account_number = int(input("To delete account, enter account number:"))
    for account in bank:
        if account_number == account.account_no:
            account.display_details()
            answer = input("Are you sure you want to delete:").lower()
            if answer == "y":
                if not validate_delete(account.balance):
                    print("Balance must £0.00 to delete account")
                    return
                else:
                    bank.remove(account)
                    print("Account sucessfully deleted")
            else:
                print("Account not deleted")
            
             
def choice(bank):
    while True:
        menu()
        answer = input("Please choose an option:")
        if answer == "1":
            create_account(bank)
        elif answer == "2":
            search_account(bank)
        elif answer == "3":
            display_every_account(bank)
        elif answer == "4":
            deposit(bank)
        elif answer == "5":
            withdraw(bank)
        elif answer == "6":
            delete_account(bank)
        elif answer == "7":
            print("Goodbye")
            break 
        else:
            print("Invalid option")

bank = []
print(len(bank))
choice(bank)
