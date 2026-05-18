import sqlite3

conn = sqlite3.connect("ali.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
               t_id INTEGER PRIMARY KEY AUTOINCREMENT,
               t_order_id INTEGER,
               t_item TEXT,
               t_category TEXT,
               t_amount REAL,
               t_date TEXT,
               t_cashier TEXT
)
""")

conn.commit()

def menu():
    print("---TESCOS---\nCustomer RECIPT")
    print("1.Insert Customer Order")
    print("2.Display All Orders")
    print("3.Search Order")
    print("3.EXIT")

def validate_food(amount):
    if amount < 0 or amount > 50:
        return False
    return True

def validate_clothing(amount):
    if amount < 0 or amount > 150:
        return False
    return True

def validate_electrics(amount):
    if amount< 0 or amount > 1000:
        return False
    return True

def insert_order():
    total = 0

    order_id = int(input("Order ID:"))
    cashier = input("Cashier Name:")
    date = input("Date")

    while True:
        item = input("Item:")

        while True:
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electric":
                print("Invalid choice")
                continue
            else:
                break
            
        while True:
            try:
                amount = int(input("Enter Price of Item:"))
                if category == "food":
                    if not validate_food(amount):
                        print("Invalid food price entered:")
                        continue
                    else:
                        total += amount
                        break
                elif category == "clothing":
                    if not validate_clothing(amount):
                        print("Invalid clothing price entered")
                        continue 
                    else:
                        total += amount
                        break
                elif category == "electric":
                    if not validate_electrics(amount):
                        print("Invalid electrics price entered")
                        continue 
                    else:
                        total += amount
                        break
            except ValueError:
                print("Do not enter characters only numbers")
                continue 
        
        cursor.execute("""
        INSERT INTO expenses(
            t_order_id,
            t_item,
            t_category,
            t_amount,
            t_date,
            t_cashier)
        VALUES(?,?,?,?,?,?)
        """,(order_id,item,category,amount,date,cashier))

        conn.commit()

        choice = input("Do you want to exit?").lower()
        if choice == "y":
            print("Goodbye")
            break 
        else:
            continue

def display_all():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No customer orders found")
        return

    total = 0

    for i in range(len(rows)-1):
        previous_order = rows[i]
        current_order = rows[i+1]

        if previous_order[1] == current_order[1]:
            total += previous_order[4]
        else:
            print(total)

def search_order():

    order_id = int(input("Enter Order ID:"))

    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))
    rows = cursor.fetchall()

    total = 0

    if len(rows) == 0:
        print("No Customer orders exist")
    else:
        for customer in rows:
            print(customer)
            total += customer[4]
        print(f"Total Customer Bill:{total}")

def main():
    while True:
        menu()
        select = input("Enter a choice from the menu:")

        if select == "1":
            insert_order()
        elif select == "2":
            display_all()
        elif select == "3":
            search_order()
        elif select == "4":
            print("Goodbye")
            break 
        else:
            print("Invalid choice")

main()


    



