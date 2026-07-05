import sqlite3

conn = sqlite3.connect("yusuf.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS barclays(
               b_id INTEGER PRIMARY KEY AUTOINCREMENT,
               b_name TEXT,
               b_account_no INTEGER,
               b_balance REAL,
               b_account TEXT)
""")

conn.commit()

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
                print("Savings Account Balance cannot go below £100")
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

def generate_account_no(rows):
    highest_acc_no = 1000

    for row in rows:
        if row[2] > highest_acc_no:
            highest_acc_no = row[2]
    return highest_acc_no + 1

def validate_delete(balance):
    if balance < 0 or balance > 0:
        return False
    return True

def account_type(account):
    if account == "1":
        return "Current"
    return "Savings"

def create_account():
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
            balance = float(input("Deposit:"))
            if not opening_deposit(balance):
                print("Minumum deposit £50")
                continue 
            break 
        except ValueError:
            print("Use integers not letters to enter deposit!")
            continue

    answer = input("What type of account? (1 - current, 2 - savings)")
    account = account_type(answer)
    print(account)

    cursor.execute("""
    SELECT * FROM barclays
    """)

    rows = cursor.fetchall()
    account_no = generate_account_no(rows) 

    new_account = BankAccount(
        name,
        account_no,
        balance,
        account
    )

    cursor.execute("""
    INSERT INTO barclays(
                b_name,
                b_account_no,
                b_balance,
                b_account)
    VALUES(?,?,?,?)
    """,(new_account.name,
         new_account.account_no,
         new_account.balance,
         new_account.account))

    conn.commit()

    new_account.show_details()
    return
 
def search_account():

    account_no = int(input("Account Number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("Acount not found")
        return
    else:
        data = BankAccount(
        row[1],
        row[2],
        row[3],
        row[4],
    )
    data.show_details()
    return

def display_all_accounts():
    cursor.execute("SELECT * FROM barclays")

    rows = cursor.fetchall()

    if not len(rows):
        print("No accounts found")
        return
    else:
        for row in rows:
            data = BankAccount(
            row[1],
            row[2],
            row[3],
            row[4]
        )
            data.show_details()
        return

def delete_account():
    account_no = int(input("Account Number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("Account not found")
    else:
        data = BankAccount(
            row[1],
            row[2],
            row[3],
            row[4]
        )
        data.show_details()

        delete = input("Are you sure you want to delete account").lower()
        if delete == "y":
            if not validate_delete(row[3]):
                print("Funds in account, cannot delete account!")
                return
            else:
                cursor.execute("""
                DELETE FROM barclays
                WHERE b_account_no = ?
                """,(account_no,))

                conn.commit()
            
                print("Account sucessfully deleted")
        else:
            print("Account not deleted")

def deposit_account():
    account_no = int(input("Account Number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    row = cursor.fetchone()

    if not row:
        print("Account not found")
    else:
        data = BankAccount(
            row[1],
            row[2],
            row[3],
            row[4]
        )
        data.show_details()

        depositing = float(input("How much would you like to deposit?"))
        data.deposit(depositing)

        cursor.execute("""
        UPDATE barclays
        SET b_balance = ?
        WHERE b_account_no = ?
        """,(data.balance,account_no))

        conn.commit()

        print("Money sucessfully deposited")
        data.show_details()        
    
def withdraw_account():
    account_no = int(input("Account Number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_no,))

    row = cursor.fetchone()
    if not row:
        print("Account not found")
    else:
        data = BankAccount(
            row[1],
            row[2],
            row[3],
            row[4]
        )
        data.show_details()

        withdrawing = float(input("How much would you like to withdraw?"))
        data.withdraw(withdrawing)

        cursor.execute("""
        UPDATE barclays
        SET b_balance = ?
        WHERE b_account_no = ?
        """,(data.balance,account_no))

        conn.commit()

        print("Money sucessfully withdrawn")

        data.show_details()

def transfer_money():
    account_noA = int(input("From account number:"))

    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_noA,))

    row = cursor.fetchone()

    if not row:
        print("Account not found")
    else:
        data1 = BankAccount(
            row[1],
            row[2],
            row[3],
            row[4]
        )
        data1.show_details()
        transfer = float(input("Transfer amount:"))
        data1.withdraw(transfer)

        cursor.execute("""
        UPDATE barclays
        SET b_balance = ?
        WHERE b_account_no = ?
        """,(data1.balance,account_noA,))

        conn.commit()

        data1.show_details()

    account_noB = int(input("To account number:"))
    cursor.execute("""
    SELECT * FROM barclays
    WHERE b_account_no = ?
    """,(account_noB,))

    row = cursor.fetchone()

    if not row:
        print("Account not found")
    else:
        data2 = BankAccount(
            row[1],
            row[2],
            row[3],
            row[4]
        )
        data2.show_details()
        data2.deposit(transfer)

        cursor.execute("""
        UPDATE barclays
        SET b_balance = ?
        WHERE b_account_no = ?
        """,(data2.balance,account_noB,))
               
def choices():
    while True:
        menu()
        decision = input("Select an option:")
        if decision == "1":
            create_account()
        elif decision == "2":
            search_account()
        elif decision == "3":
            display_all_accounts()
        elif decision == "4":
            delete_account()
        elif decision == "5":
            deposit_account()
        elif decision == "6":
            withdraw_account()
        elif decision == "7":
            transfer_money()
        elif decision =="8":
            print("Goodbye")
            break 
        else:
            print("Invalid option")
choices()
