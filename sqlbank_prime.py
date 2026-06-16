import sqlite3

conn = sqlite3.connect("yusuf.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS barclays(
               b_id INTEGER PRIMARY KEY AUTOINCREMENT,
               b_name TEXT,
               b_balance REAL,
               b_account_no INTEGER)
""")

conn.commit()

def menu():
    print("=" *40)
    print("Barclays Bank".center(40))
    print("=" *40)
    print("1.Create Account")
    print("2.Search Account")
    print("3.Deposit Money")
    print("4.Withdraw Money")
    print("5.Delete Money")
    print("6.Display All Accounts")
    print("7.EXIT")
    from datetime import datetime
    now = datetime.now()
    print("*" *40 )
    print(now)
    print("*" *40)

def account_number(rows):
    account_no = 1001

    for customer in rows:
        if account_no == 1001 or customer[3] +1 > account_no:
            account_no = customer[3] +1
    return account_no
    
def name_validation(name):
    for letters in name:
        if not letters.isalpha() and letters != " ":
            return False
    return True

def opening_deposit_validation(deposit):
    if deposit < 50 or deposit != round(deposit, 2):
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

    #if row[3] != 0:
        #return False
    #return True

def minimum_withdraw(withdraw):
    if withdraw <=0:
        return False
    return True

def create_account():
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
            deposit = float(input("Deposit:£"))
            if not opening_deposit_validation(deposit):
                print("Deposit no less than £50 to open an account")
                continue 
            break
        except ValueError:
            print("Enter a deposit amount numerically only!")
            continue
    
    cursor.execute("""
    SELECT * FROM barclays
    """)
    rows = cursor.fetchall()
    
    account_no = account_number(rows)

    cursor.execute("""
    INSERT INTO barclays(
                b_name,
                b_balance,
                b_account_no)
    VALUES(?,?,?)
    """,(name,deposit,account_no))

    print(f"Name:{name}")
    print(f"Deposit:£{deposit:.2f}")
    print(f"Account Number:{account_no}")
    return

def search_account():
    print("Search Account")
    account_no = int(input("Account Number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    rows = cursor.fetchone()

    if not rows:
        print("Customer Not Found")
        return
    else:
        print(f"Name:{rows[1]}")
        print(f"Balance:{rows[2]}")
        print(f"Account Number:{rows[3]}")
    return
    
def deposit_money():
    account_no = int(input("Account Number:"))
    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    rows = cursor.fetchone()

    if not rows:
        print("Account not found")
        return

    print(f"Name:{rows[1]}")
    print(f"Balance:{rows[2]}")
    print(f"Account Number:{rows[3]}")
    
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
    
    new_balance = rows[2] + deposit
    cursor.execute("""
    UPDATE barclays
    SET b_balance = ?
    WHERE b_account_no = ?
    """,(new_balance,account_no))

    conn.commit()

    print(f"Name:{rows[1]}")
    print(f"Balance:{new_balance}")
    print(f"Account Number:{rows[3]}")

def withdraw_money():
    account_no = int(input("Account Number:"))
    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    rows = cursor.fetchone()

    if not rows:
        print("Account not found")
        return

    print(f"Name:{rows[1]}")
    print(f"Balance:{rows[2]}")
    print(f"Account Number:{rows[3]}")

    while True:
        try:
            withdraw = float(input("Withdrawal amount:"))
            if not maximum_withdraw(withdraw,rows[2]):
                print("You cannot withdraw more than the balance")
                continue 
            if not minimum_withdraw(withdraw):
                print("You cannot withdraw 0p or less")
                continue 
            break
        except ValueError:
            print("Enter a deposit amount numerically only!")
            continue

    new_balance = rows[2] - withdraw
    cursor.execute("""
    UPDATE barclays
    SET b_balance = ?
    WHERE b_account_no = ?
    """,(new_balance,account_no))

    conn.commit()

    print(f"Name:{rows[1]}")
    print(f"Balance:{new_balance}")
    print(f"Account Number:{rows[3]}")

def delete_account():
    account_no = int(input("Account Number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))
    
    rows = cursor.fetchone()

    if not rows:
        print("Account Not Found")
    else:
        print(f"Name:{rows[1]}")
        print(f"Balance:{rows[2]}")
        print(f"Account Number:{rows[3]}")
    answer = input("Are you sure you want to delete the bank account?").lower()
    if answer == "y":
        if not full_withdrawal(rows[2]):
            print("Credits in Bank so cannot delete account")
            return
        else:
            cursor.execute("""
            DELETE FROM barclays
            WHERE b_account_no = ?
            """,(account_no,))

            conn.commit()

            print("Bank Account has been sucessfully deleted")
            return
    else:
        print("Bank Account not deleted")
        return

def display_all_accounts():
    
    cursor.execute("SELECT * FROM barclays")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No Bank Accounts Exist")
        return
    
    for customer in rows:
        print(f"Name:{customer[1]}")
        print(f"Balance:{customer[2]}")
        print(f"Account Number:{customer[3]}")
    return

def choices():
    while True:
        menu()
        answer = input("Select a number from the menu:")
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
            display_all_accounts()
        elif answer == "7":
            print("Good Bye")
            break
        else:
            print("Invalid Choice")

choices()

    













        


