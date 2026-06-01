import sqlite3

conn = sqlite3.connect("england.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
               t_id INTEGER PRIMARY KEY AUTOINCREMENT,
               t_order_id INTEGER,
               t_item TEXT,
               t_category TEXT,
               t_amount REAL)
""")

conn.commit()

def menu():
    print("\n" + "=" * 40)
    print("---TESCO----".center(40))
    print("=" * 40)
    from datetime import datetime
    now = datetime.now()
    print("\n",now)
    print("1.INSERT ORDER")
    print("2.DISPLAY ALL ORDERS")
    print("3.SEARCH ORDER")
    print("4.DELETE ORDER")
    print("5.UPDATE ORDER")
    print("6.EXIT")

def food_price(amount):
    if amount < 0 or amount > 50:
        return False
    return True

def clothing_price(amount):
    if amount < 0 or amount > 150:
        return False
    return True 

def electrics_price(amount):
    if amount < 0 or amount > 1500:
        return False 
    return True 

def insert_order():
    print("Insert An Order")
    order_id = int(input("ENTER ORDER ID:"))

    while True:
        item = input("Item:")

        while True:
            print("Choose either: food or clothing or electrics")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrics":
                print("Invalid choice made:")
                continue 
            else:
                break

        total = 0
        while True:
            try:
                amount = int(input("Amount:")) 
                if category == "food":
                    if not food_price(amount):
                        print("Wrong food price entered!")
                        continue 
                    else:
                        total += amount
                        break 
                elif category == "clothing":
                    if not clothing_price(amount):
                        print("Wrong clothing price entered!")
                        continue 
                    else:
                        total += amount
                        break 
                elif category == "electrics":
                    if not electrics_price(amount):
                        print("Wrong electrics price entered!")
                        continue 
                    else:
                        total += amount
                        break 
            except ValueError:
                print("Enter price in numbers! No characters!")
        
        cursor.execute("""
        INSERT INTO expenses(
                    t_order_id,
                    t_item,
                    t_category,
                    t_amount)
        VALUES(?,?,?,?)
        """,(order_id,item,category,amount))

        conn.commit()

        answer = input("Do you want to exit?").lower()
        if answer == "y":
            print("Order Sucessfully added onto database system")
            input("Press Enter to continue.......")
            break 
        else:
            print("Continue to add more orders...")
            input("Press Enter to continue.......")
            continue

def display_all_orders():
    print("Display All Orders")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    total = 0
    for i in range(len(rows)-1):

        previous_order = rows[i]
        current_order = rows[i+1]

        total += previous_order[4]
        if previous_order[1] != current_order[1]:
            print(f"Primary Key ID:{previous_order[0]} Order ID:{previous_order[1]} Total:{total}")
            total = 0
    total += rows[-1][4]
    print(f"Primary Key ID:{previous_order[0]} Order ID:{previous_order[1]} Total:{total}")
    input("Press Enter to continue.......")

def search_order():
    print("Search An Order")
    order_id = int(input("ENTER ORDER ID:"))

    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    total = 0
    for order in rows:
        print(order)
        total += order[4]
    print(f"Total:{total}")
    input("Press Enter to continue.......")

def delete_order():
    print("Delete An Order")
    order_id = int(input("ENTER ORDER ID:"))

    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    total = 0
    for order in rows:
        total += order[4]
    print(f"Total:{total}")

    answer = input("Are you sure you want to delete this order?").lower()
    if answer == "y":
        cursor.execute("""
        DELETE FROM expenses
        WHERE t_order_id = ?
        """,(order_id,))

        conn.commit()

        print("Order sucessfully deleted")
        input("Press Enter to continue.......")
    else:
        print("Delete cancelled - Order still exists")
        input("Press Enter to continue.......")

def update_order():
    print("Insert An Order")
    primary_key_id = int(input("Enter Original Primary Key ID:"))
    order_id = int(input("Enter Original Order ID:"))

    while True:
        item = input("Item:")

        while True:
            print("Choose either: food or clothing or electrics")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrics":
                print("Invalid choice made:")
                continue 
            else:
                break

        total = 0
        while True:
            try:
                amount = int(input("Amount:")) 
                if category == "food":
                    if not food_price(amount):
                        print("Wrong food price entered!")
                        continue 
                    else:
                        total += amount
                        break 
                elif category == "clothing":
                    if not clothing_price(amount):
                        print("Wrong clothing price entered!")
                        continue 
                    else:
                        total += amount
                        break 
                elif category == "electrics":
                    if not electrics_price(amount):
                        print("Wrong electrics price entered!")
                        continue 
                    else:
                        total += amount
                        break 
            except ValueError:
                print("Enter price in numbers! No characters!")
        
        cursor.execute("""
        UPDATE expenses
        SET t_order_id = ?,
            t_item = ?,
            t_category = ?,
            t_amount = ?
        WHERE t_id = ?             
        """,(order_id,item,category,amount,primary_key_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Order Sucessfully Updated")
            answer = input("Do you want to exit?").lower()
            if answer == "y":
                break 
            else:
                print("Update again the same item witin the same order...")
                input("Press Enter to continue.......")
                continue
        else:
            print("Order not found")
            return

        

def choices():
    while True:
        menu()
        answer = input("Enter a number from the menu to carryout a task:").lower()

        if answer == "1":
            insert_order()
        elif answer == "2":
            display_all_orders()
        elif answer == "3":
            search_order()
        elif answer == "4":
            delete_order()
        elif answer == "5":
            update_order()
        elif answer == "6":
            print("Goodbye")
            break 
        else:
            print("Invalid number entered")

choices()