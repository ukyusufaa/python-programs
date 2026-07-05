
def menu():
    print("\n" + "=" *40)
    print("---METRO BANK---".center(40))
    print("=" *40)
    print("Mercers Row, Northampton, NN1 3RT".center(40))
    print()
    from datetime import datetime
    now = datetime.now()
    print(now)
    print()
    print("1.Create Account")
    print("2.Search Account")
    
    print("3.Deposit Money")
    print("4.Withdraw Money")
    print("5.Delete Account")
    print("6.Display All Accounts")
    print("7.Exit")

def account_number(bank):
    present_account_no = 1001

    for next_account_no in bank:
        if present_account_no == 1001 or next_account_no > present_account_no:
            present_account_no = next_account_no + 1
    return present_account_no

def deposit_validation(deposit):
    if deposit < 50 or deposit != round(deposit,2):
        return False
    return True

def name_validation(customer_name):
    for letters in customer_name:
        if not letters.isalpha() and not letters == " ":
            return False
    return True

def create_account(bank):
    print("Insert A New Customer")
    while True:
        try:
            customer_name = input("Enter new customer name:").strip()
            if customer_name == "":
                print("Do not leave name field blank!")
                continue
            if not name_validation(customer_name):
                print("Incorrect new customer name entered - re-enter again! ")
                continue 
            break 
        except ValueError:
            print("No numbers! - Enter a new customer name in characters only")
            continue 

    while True:
        try:
            balance = float(input("Deposit:"))
            if not deposit_validation(balance):
                print("New Bank Account - A minumum deposit of £50 required!")
                continue 
            break 
        except ValueError:
            print("Deposit Amount - No characters! Numbers only!")
        continue

    account_no = account_number(bank)

    bank.append({
        "Customer Name":customer_name,
        "Account Balance":balance,
        "Account Number":account_no
    })

    print("\n" + "=" *40)
    print("METRO BANK".center(40))
    print("=" *40)
    print()
    from datetime import datetime
    now = datetime.now()
    print("\n",now)
    print()
    print("=" *100)
    print(f"Account Number:{account_no}")
    print(f"Account Holder Name:{customer_name}")
    print(f"Current Balance:£{balance:.2f}")
    print("=" *100)

def search_account(bank):
    print("Search An Account")
    account_no = int(input("Enter account number: "))

    for customer in bank:
        if account_no == customer["Account Number"]:
            print()
            print("=" *100)
            print(f"Account Number:{customer['Account Number']}")
            print(f"Account Holder Name:{customer['Customer Name']}")
            print(f"Current Balance:£{customer['Account Balance']:.2f}")
            print("=" *100)
            return
    
    print("\n" + "+" + "-" *40 + "+")
    print("Account not found".center(40))
    print("+" + "-" *40 + "+")
    return
        
def validate_deposit(deposit):
    if deposit <= 0:
        return False
    return True

def deposit_money(bank):
    print("Deposit Money")
    account_no = int(input("Enter account number: "))

    for customer in bank:
        if account_no == customer["Account Number"]:
            print()
            print("=" *100)
            print(f"Account Number:{customer['Account Number']}")
            print(f"Account Holder Name:{customer['Customer Name']}")
            print(f"Current Balance:£{customer['Account Balance']:.2f}")
            print("=" *100)
    
            answer = input("Do you want to deposit money?(y/n)").lower()
            if answer == "y":
                while True:
                    try:
                        deposit = float(input("Enter Deposit:"))
                        xyz = validate_deposit(deposit)
                        if xyz != False:
                            new_balance = customer["Account Balance"] + deposit
                            customer["Account Balance"] = new_balance
                            break 
                        else:
                            print("Re-Enter a deposit above £0.00!")
                            continue
                
                    except ValueError:
                        print("Enter a deposit in numbers & decimals NOT characters!")
                        continue
        
                print("\n" + "=" *40)
                print("METRO BANK".center(40))
                print("=" *40)
                print()
                from datetime import datetime
                now = datetime.now()
                print("\n",now)
                print()
                print("=" *100)
                print(f"Account Number:{customer['Account Number']}")
                print(f"Account Holder Name:{customer['Customer Name']}")
                print(f"Current Balance:£{new_balance:.2f}")
                print("=" *100)
                return
            else:
                print("\n" + "+" + "-" *40 + "+")
                print("No Money Deposited".center(40))
                print("+" + "-" *40 + "+")
                print()
                return
      
    print("\n" + "+" + "-" *40 + "+")
    print("Account not found".center(40))
    print("+" + "-" *40 + "+")
    return

def validate_withdraw(withdraw):
    if withdraw <= 0:
        return False
    return True

def validate_withdraw_amount(withdraw,balance):
        if withdraw > balance:
            return False
        return True

def withdraw_money(bank):
    print("Withdraw Money")
    account_no = int(input("Enter account number: "))

    for customer in bank:
        if account_no == customer["Account Number"]:
            print()
            print("=" *100)
            print(f"Account Number:{customer['Account Number']}")
            print(f"Account Holder Name:{customer['Customer Name']}")
            print(f"Current Balance:£{customer['Account Balance']:.2f}")
            print("=" *100)
    
            answer = input("Do you want to withdraw money?(y/n)").lower()
            if answer == "y":
                while True:
                    try:
                        amount_withdrawn = float(input("How much would you like to withdrawn?"))
                        xyz = validate_withdraw(amount_withdrawn)
                        abc = validate_withdraw_amount(amount_withdrawn,customer["Account Balance"])
                        if xyz != False and abc != False:
                            new_balance = customer["Account Balance"] - amount_withdrawn
                            customer["Account Balance"] = new_balance
                            break
                        else:
                            print("Minimum withdraw 1 pence and withdraw cannot exceed current balance")
                            continue
                    except ValueError:
                        print("Enter withdrawal amount in numbers & decimals NOT characters!")
                        continue
        
                print("\n" + "=" *40)
                print("METRO BANK".center(40))
                print("=" *40)
                print()
                from datetime import datetime
                now = datetime.now()
                print("\n",now)
                print()
                print("=" *100)
                print(f"Account Number:{customer['Account Number']}")
                print(f"Account Holder Name:{customer['Customer Name']}")
                print(f"Current Balance:£{new_balance:.2f}")
                print("=" *100)
                return
            else:
                print("\n" + "+" + "-" *40 + "+")
                print("No Money Withdrawn".center(40))
                print("+" + "-" *40 + "+")
                print()
                return
    
    print("\n" + "+" + "-" *40 + "+")
    print("Account not found".center(40))
    print("+" + "-" *40 + "+")
    return
    
def validate_delete_account(balance):
    if balance != 0:
        return False
    return True

def delete_account(bank):
    print("Delete Account")
    account_no = int(input("Enter account number: "))
    
    for customer in bank:
        if account_no == customer["Account Number"]:
            print("\n" + "=" *40)
            print("METRO BANK".center(40))
            print("=" *40)
            print()
            from datetime import datetime
            now = datetime.now()
            print("\n",now)
            print()
            print("=" *100)
            print(f"Account Number:{customer['Account Number']}")
            print(f"Account Holder Name:{customer['Customer Name']}")
            print(f"Current Balance:£{customer['Account Balance']:.2f}")
            print("=" *100)
    
            answer = input("Do you want to delete account?(y/n)").lower()
            if answer == "y":
                xyz = validate_delete_account(customer["Account Balance"])
                if xyz != False:
                    bank.remove(customer)
                    print("Account successfully deleted")
                    input("Press Enter to continue.....")
                    return
                else:
                    print("Withdrawn all money before deleting account!")
                    input("Press Enter to continue.....")
                    return
            else:
                print("\n" + "+" + "-" *40 + "+")
                print("Account Not Deleted".center(40))
                print("+" + "-" *40 + "+")
                print()
                return

def display_all_accounts(bank):
    if not bank:
        print("\n" + "+" + "-" *40 + "+")
        print("No accounts found".center(40))
        print("+" + "-" *40 + "+")
        print()
        return
    for customer in bank:
        print()
        print("=" *100)
        print(f"Account Number:{customer['Account Number']}")
        print(f"Account Holder Name:{customer['Customer Name']}")
        print(f"Current Balance:£{customer['Account Balance']:.2f}")
        print("=" *100)
    return
           
def choices(bank):
    while True:
        menu()
        answer = input("Enter:")
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
            print("Goodbye customer")
            break 
        else:
            print("Invalid")
all_clients = []
choices(all_clients)



