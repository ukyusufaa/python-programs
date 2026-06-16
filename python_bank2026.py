def menu():
    print("="*40)
    print("Barclays Bank".center(40))
    print("="*40)
    print("1.Create Account")
    print("2.Search Account")
    print("3.Deposit Money")
    print("4.Withdraw Money")
    print("5.Delete Money")
    print("6.Display All Accounts")
    print("7.EXIT")

def account_number(bank):
    account_no = 1001

    for customer in bank:
        if account_no == 1001 or customer["Account Number"] +1 > account_no:
            account_no = customer["Account Number"] +1
    return account_no
    

def name_validation(name):
    for letters in name:
        if not letters.isalpha() and letters != " ":
            return False
    return True

def opening_deposit_validation(deposit):
    if deposit < 50:
        return False
    return True

def minimum_deposit(depositing):
    if depositing <= 0:
        return False
    return True

def maximum_withdraw(withdrawal,balance):
    if withdrawal > balance:
        return False
    return True

def full_withdrawal(balance):
    if balance < 0 or balance > 0:
        return False
    return True

def create_account(bank):
    print("Create New Customer Account")

    while True:
        name = input("Name:").strip()
        if name == "":
            print("Do not leave name field blank!")
            continue
        if not name_validation(name):
            print("Enter a name correctly!")
            continue
        break

    while True:
        try:
            deposit = float(input("Deposit:"))
            if not opening_deposit_validation(deposit):
                print("Deopsit no less than £50 to open an account")
                continue 
            break
        except ValueError:
            print("Enter a deposit amount numerically only!")
            continue
    
    account_no = account_number(bank)

    bank.append({
        "Name":name,
        "Balance":deposit,
        "Account Number":account_no
    })
    
    print(f"Name:{name}")
    print(f"Deposit:{deposit}")
    print(f"Account Number:{account_no}")
    return

def search_account(bank):
    print("Search Account")

    account_no = int(input("Account Number:"))
    for customer in bank:
        if account_no == customer["Account Number"]:
            print(f"Name:{customer['Name']}")
            print(f"Balance:{customer['Balance']}")
            print(f"Account Number:{customer['Account Number']}")
            return
    print("Account not found")
    return

def deposit_money(bank):
    account_no = int(input("Account Number:"))
    for customer in bank:
        if account_no == customer["Account Number"]:
            print(f"Name:{customer['Name']}")
            print(f"Balance:{customer['Balance']}")
            print(f"Account Number:{customer['Account Number']}")
        while True:
            try:
                deposit = float(input("Deposit:"))
                if not minimum_deposit(deposit):
                    print("You cannot deposit less than 1p")
                    continue 
                break
            except ValueError:
                print("Enter a deposit amount numerically only!")
                continue
        new_balance = customer["Balance"] + deposit
        customer["Balance"] = new_balance
        print(f"Name:{customer['Name']}")
        print(f"Balance:{new_balance}")
        print(f"Account Number:{customer['Account Number']}")

def withdraw_money(bank):
    account_no = int(input("Account Number:"))
    for customer in bank:
        if account_no == customer["Account Number"]:
            print(f"Name:{customer['Name']}")
            print(f"Balance:{customer['Balance']}")
            print(f"Account Number:{customer['Account Number']}")
        while True:
            try:
                withdraw = float(input("Withdrawal amount:"))
                if not maximum_withdraw(withdraw,customer['Balance']):
                    print("You cannot withdraw more than the balance")
                    continue 
                break
            except ValueError:
                print("Enter a deposit amount numerically only!")
                continue
        new_balance = customer["Balance"] - withdraw
        customer["Balance"] = new_balance
        print(f"Name:{customer['Name']}")
        print(f"Balance:{new_balance}")
        print(f"Account Number:{customer['Account Number']}")

def delete_account(bank):
    account_no = int(input("Account Number:"))
    for customer in bank:
        if account_no == customer["Account Number"]:
            print(f"Name:{customer['Name']}")
            print(f"Balance:{customer['Balance']}")
            print(f"Account Number:{customer['Account Number']}")
            answer = input("Are you sure you want to delete the bank account?").lower()
            if answer == "y":
                if not full_withdrawal(customer['Balance']):
                    print("Credits in Bank so cannot delete account")
                    return
                else:
                    bank.remove(customer)
                    print("Bank Account has been sucessfully deleted")
                    return
            else:
                print("Bank Account not deleted")
                return

def display_all_accounts(bank):
    if not bank:
        print("No Accounts found")
        return
    for customer in bank:
        print(f"Name:{customer['Name']}")
        print(f"Balance:{customer['Balance']}")
        print(f"Account Number:{customer['Account Number']}")
    return

def choices(bank):
    while True:
        menu()
        answer = input("Select a number from the menu:")
        if answer == "1":
            create_account(bank)
        elif answer == "2":
            search_account(bank)
        elif answer == "3":
            deposit_money(bank)
        elif answer == "4":
            withdraw_money(bank)
        elif answer == "5":
            delete_account(bank)
        elif answer == "6":
            display_all_accounts(bank)
        elif answer == "7":
            print("Good Bye")
            break
        else:
            print("Invalid Choice")

barclays = []
choices(barclays)

    













        


