import sqlite3

conn = sqlite3.connect("sohawa.db")

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
    print("---TESCO---".center(50))
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
    print("Insert Order")
    order_id = int(input("Order ID:"))

    total = 0
    while True:
        item = input("Item:")

        while True:
            print("Enter either:\nfood or clothing or electrics")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrics":
                print("Invalid category!")
                continue 
            else:
                break 
        
        while True:
            try:
                amount = int(input("Enter amount:"))
                if category == "food":
                    if not food_price(amount):
                        print("Incorrect food price entered!")
                        continue 
                    else:
                        total += amount
                        break

                elif category == "clothing":
                    if not clothing_price(amount):
                        print("Incorrect clothing price entered!")
                        continue 
                    else:
                        total += amount
                        break 

                elif category == "electrics":
                    if not electrics_price(amount):
                        print("Incorrect electrics price entered!")
                        continue 
                    else:
                        total += amount
                        break 

            except ValueError:
                print("No Characters - For price enter only numbers!")
    
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
             print("Order sucessfully added onto Tesco database system")
             input("Press Enter to continue.....")
             break
        else:
            input("Press Enter to continue....")
            continue 


def display_all_orders():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("INSERT ORDERS - No orders saved on system")
    total = 0

    for i in range(len(rows)-1):
        previous_order = rows[i]
        current_order = rows[i+1]

        print(previous_order)
        if previous_order[1] != current_order[1]:
            total += previous_order[4]
            print(f"Amount:{total}")
            total = 0
    total += rows[-1][4]
    print(f"Amount{total}")

def search_order():
    print("Search for a Order")
    order_id = int(input("Order ID:"))

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
    print(f"Amount:{total}")


def delete_order():
    print("Delete Order")
    order_id = int(input("Order ID:"))

    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    answer = input("Are you sure you want to delete this order?").lower()
    if answer == "y":
        cursor.execute("""
        DELETE FROM expenses
        WHERE t_order_id = ?
        """,(order_id,))

        conn.commit()
        print("Order Sucessfully deleted")
    else:
        print("Order exists - Delete operation cancelled")
    

def update_order():
    print("Update Order")

    primary_key_id = int(input("Enter Original Primary Key ID:"))
    order_id = int(input("Enter Original Order ID:"))

    while True:
        item = input("Item:")

        while True:
            print("Enter either:\nfood or clothing or electrics")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrics":
                print("Invalid category!")
                continue 
            else:
                break 
        total = 0
        while True:
            try:
                amount = int(input("Enter amount:"))
                if category == "food":
                    if not food_price(amount):
                        print("Incorrect food price entered!")
                        continue 
                    else:
                        total += amount
                        break

                elif category == "clothing":
                    if not clothing_price(amount):
                        print("Incorrect clothing price entered!")
                        continue 
                    else:
                        total += amount
                        break 

                elif category == "electrics":
                    if not electrics_price(amount):
                        print("Incorrect electrics price entered!")
                        continue 
                    else:
                        total += amount
                        break 

            except ValueError:
                print("No Characters - For price enter only numbers!")
    
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
            print("Order sucessfully updated")
            break 
        else:
            print("Order not found")
            break 

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