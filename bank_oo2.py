def menu():
    print("---BARCLAYS---".center(40))
    print("1.Create account")
    print("2.Search account")
    print("3.Display all account")
    print("4.Delete account")
    print("5.Deposit")
    print("6.Withdraw")
    print("7.Transfer")
    print("8.EXIT")

class BankAccount:
    def __init__(self,name,account_no,balance,account):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.account = account
    
    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Account No:{self.account_no}")
        print(f"Balance:{self.balance}")
        print(f"Account:{self.account}")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def withdraw(self,amount):
        if self.account == "Current":
            if self.balance - amount < -100:
                print("Current Account Balance cannot go below -£100")
            else:
                self.balance = self.balance - amount
        elif self.account == "Savings":
            if self.balance - amount < 100:
                print("Savings Account  Balance cannot go below £100")
            else:
                self.balance = self.balance - amount


def validate_name(name):
    for letters in name:
        if not letters.isalpha() and not letters == " ":
            return False
    return True

def opening_deposit(deposit):
    if deposit < 50 or deposit != round (deposit,2):
        return False
    return True

def generate_account_no(bank):
    highest_acc_no = 1000

    for account in bank:
        if account.account_no > highest_acc_no:
            highest_acc_no = account.account_no
    return highest_acc_no + 1

def validate_delete(balance):
    if balance < 0 or balance > 0:
        return False
    return True

def account_type(account):
    if account == "1":
        return "Current"
    return "Savings"


def create_account(bank):
    while True:
        name = input("Name:").strip()
        if name == "":
            print("Do not leave name field blank")
            continue 
        if not validate_name(name):
            print("Enter a full name correctly!")
            continue 
        break 
    while True:
        try:
            deposit = float(input("Deposit:"))
            if not opening_deposit(deposit):
                print("Minumum deposit £50")
                continue 
            break 
        except ValueError:
            print("Use integers not letters to enter deposit!")
            continue

    answer = input("What type of account? (1 - current, 2 - savings)")
    account = account_type(answer)
    print(account)

    account_no = generate_account_no(bank) 

    new_account = BankAccount(
        name,
        account_no,
        deposit,
        account
    )
    bank.append(new_account)
    new_account.show_details()

def search_account(bank):
    found = False
    account_no = int(input("Account Number:"))
    for account in bank:
        if account_no == account.account_no:
            found = True
            account.show_details()
            input("Press ENTER to return to menu")
    if found == False:
        print("Acount not found")
        return

def display_all_accounts(bank):
    for account in bank:
        account.show_details()
    if not len(bank):
        print("No accounts found")
        return

def delete_account(bank):
    found = False
    account_no = int(input("Account Number:"))
    for account in bank:
        if account_no == account.account_no:
            found = True
            account.show_details()
            if not validate_delete(account.balance):
                print("Funds in account, cannot delete account!")
                continue
            else:
                delete = input("Are you sure you want to delete account").lower()
                if delete == "y":
                    bank.remove(account)
                    print("Account sucessfully deleted")
                else:
                    print("Account not deleted")
    if found == False:
        print("Account not found")

def deposit_account(bank):
    found = False
    account_no = int(input("Account Number:"))
    for account in bank:
        if account_no == account.account_no:
            found = True
            account.show_details()
            depositing = float(input("How much would you like to deposit?"))
            account.deposit(depositing)
            account.show_details()
    if found == False:
        print("Account not found")

def withdraw_account(bank):
    found = False
    account_no = int(input("Account Number:"))
    for account in bank:
        if account_no == account.account_no:
            found = True
            account.show_details()
            withdrawing = float(input("How much would you like to withdraw?"))
            account.withdraw(withdrawing)
            account.show_details()
    if found == False:
        print("Account not found")

def transfer_money(bank):
    account_noA = int(input("From account number:"))
    for account in bank:
        if account_noA == account.account_no:
            account.show_details()
            transfer = float(input("Transfer amount:"))
            account.withdraw(transfer)
        else:
            print("Account not found")

            account_noB = int(input("To account number:"))
            for account in bank:
                if account_noB == account.account_no:
                    account.deposit(transfer)
                else:
                    print("Account not found")
                
def choices(bank):
    while True:
        menu()
        decision = input("Select an option:")
        if decision == "1":
            create_account(bank)
        elif decision == "2":
            search_account(bank)
        elif decision == "3":
            display_all_accounts(bank)
        elif decision == "4":
            delete_account(bank)
        elif decision == "5":
            deposit_account(bank)
        elif decision == "6":
            withdraw_account(bank)
        elif decision == "7":
            transfer_money(bank)
        elif decision =="8":
            print("Goodbye")
        else:
            print("Invalid option")
bank = []
choices(bank)