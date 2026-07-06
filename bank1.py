import sqlite3

conn = sqlite3.connect("bank.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
            b_id INTEGER PRIMARY KEY AUTOINCREMENT,
            b_account_number INTEGER,
            b_customer_name TEXT,
            b_balance REAL)
""")

conn.commit()

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
    print("6.Exit")

def account_number(rows):
    present_account_no = 1001

    for next_account_no in rows:
        if present_account_no == 1001 or next_account_no[0] > present_account_no:
            present_account_no = next_account_no[0]+ 1
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

def create_account():
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

    cursor.execute("SELECT b_account_number FROM accounts")
    rows = cursor.fetchall()
    account_no = account_number(rows)
   
    cursor.execute("""
    INSERT INTO accounts(
                b_account_number,
                b_customer_name,
                b_balance)
    VALUES(?,?,?)
    """,(account_no,customer_name,balance))

    conn.commit()

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

def search_account():
    print("Search An Account")
    account_no = int(input("Enter account number: "))

    cursor.execute("""
    SELECT * FROM accounts
    WHERE b_account_number = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("\n" + "+" + "-" *40 + "+")
        print("Account not found".center(40))
        print("+" + "-" *40 + "+")
        return

    if row:
        print()
        print("=" *100)
        print(f"Account Number:{row[1]}")
        print(f"Account Holder Name:{row[2]}")
        print(f"Current Balance:£{row[3]:.2f}")
        print("=" *100)

def validate_deposit(deposit):
    if deposit <= 0:
        return False
    return True

def deposit_money():
    print("Deposit Money")
    account_no = int(input("Enter account number: "))

    cursor.execute("""
    SELECT * FROM accounts
    WHERE b_account_number = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("\n" + "+" + "-" *40 + "+")
        print("Account not found".center(40))
        print("+" + "-" *40 + "+")
        return
    
    answer = input("Do you want to deposit money?(y/n)").lower()
    if answer == "y":
        while True:
            try:
                deposit = float(input("Enter Deposit:"))
                xyz = validate_deposit(deposit)
                if xyz != False:
                    break 
                else:
                    print("Re-Enter a deposit above £0.00!")
                    continue
                
            except ValueError:
                print("Enter a deposit in numbers & decimals NOT characters!")
                continue 
    else:
        print("\n" + "+" + "-" *40 + "+")
        print("No Money Deposited".center(40))
        print("+" + "-" *40 + "+")
        print()
        return
    
    new_balance = row[3] + deposit

    cursor.execute("""
    UPDATE accounts
    SET b_balance = ?
    WHERE b_account_number = ?
    """,(new_balance,account_no))

    conn.commit()

    print("\n" + "=" *40)
    print("METRO BANK".center(40))
    print("=" *40)
    print()
    from datetime import datetime
    now = datetime.now()
    print("\n",now)
    print()
    print("=" *100)
    print(f"Account Number:{row[1]}")
    print(f"Account Holder Name:{row[2]}")
    print(f"Current Balance:£{new_balance:.2f}")
    print("=" *100)

def validate_withdraw(withdraw):
    if withdraw <= 0:
        return False
    return True

def validate_withdraw_amount(withdraw,row):
        if withdraw > row[3]:
            return False
        return True

def withdraw_money():
    print("Withdraw Money")
    account_no = int(input("Enter account number: "))

    cursor.execute("""
    SELECT * FROM accounts
    WHERE b_account_number = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("\n" + "+" + "-" *40 + "+")
        print("Account not found".center(40))
        print("+" + "-" *40 + "+")
        return
    
    answer = input("Do you want to withdraw money?(y/n)").lower()
    if answer == "y":
        while True:
            try:
                amount_withdrawn = float(input("How much would you like to withdrwaw?"))
                xyz = validate_withdraw(amount_withdrawn)
                abc = validate_withdraw_amount(amount_withdrawn,row)
                if xyz != False and abc != False:
                    new_balance = row[3] - amount_withdrawn
                    break
                else:
                    print("Minimum withdraw 1 pence and withdraw cannot exceed current balance")
                    continue
            except ValueError:
                print("Enter withdrawal amount in numbers & decimals NOT characters!")
                continue
    else:
        print("\n" + "+" + "-" *40 + "+")
        print("No Money Withdrwan".center(40))
        print("+" + "-" *40 + "+")
        print()
        return

    new_balance = row[3] - amount_withdrawn
    
    cursor.execute("""
    UPDATE accounts
    SET b_balance = ?
    WHERE b_account_number = ?
    """,(new_balance,account_no))

    conn.commit()

    print("\n" + "=" *40)
    print("METRO BANK".center(40))
    print("=" *40)
    print()
    from datetime import datetime
    now = datetime.now()
    print("\n",now)
    print()
    print("=" *100)
    print(f"Account Number:{row[1]}")
    print(f"Account Holder Name:{row[2]}")
    print(f"Current Balance:£{new_balance:.2f}")
    print("=" *100)

def validate_delete_account(row):
    if row[3] != 0:
        return False
    return True

def delete_account():
    print("Delete Account")
    account_no = int(input("Enter account number: "))

    cursor.execute("""
    SELECT * FROM accounts
    WHERE b_account_number = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("\n" + "+" + "-" *40 + "+")
        print("Account not found".center(40))
        print("+" + "-" *40 + "+")
        return
    else:
        print("\n" + "=" *40)
        print("METRO BANK".center(40))
        print("=" *40)
        print()
        from datetime import datetime
        now = datetime.now()
        print("\n",now)
        print()
        print("=" *100)
        print(f"Account Number:{row[1]}")
        print(f"Account Holder Name:{row[2]}")
        print(f"Current Balance:£{row[3]:.2f}")
        print("=" *100)
    
    answer = input("Do you want to delete account?(y/n)").lower()
    if answer == "y":
        xyz = validate_delete_account(row)
        if xyz != False:
            cursor.execute("""
            DELETE FROM accounts
            WHERE b_account_number = ?
            """,(account_no,))

            conn.commit()

            print("Account sucessfully deleted")
            input("Press Enter to continue.....")
            return
        else:
            print("Withdraw all money before deleting account!")
            input("Press Enter to continue.....")
            return
        
def choices():
    while True:
        menu()
        answer = input("Enter:")
        if answer == "1":
            create_account()
        elif answer == "2":
            search_account()
        elif answer == "3":
            deposit_money()
        elif answer == "4":
            withdraw_money()
        elif answer == "5":
            delete_account()
        elif answer == "6":
            print("Goodbye customer")
            break
        else:
            print("Invalid")

choices()



