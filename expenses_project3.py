import sqlite3

conn = sqlite3.connect("zebra.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
               t_id INTEGER PRIMARY KEY AUTOINCREMENT,
               t_order_id INTEGER,
               t_operator TEXT,
               t_item TEXT,
               t_category TEXT,
               t_amount INTEGER)
""")

conn.commit()

def menu():
    print("---TESCOS---")
    print("1.Insert Customer Order")
    print("2.Display All Customer Orders")
    print("3.Search Customer Order")
    print("4.Delete Customer Order")
    print("5.Update Customer Order")
    print("6.EXIT")

def food_validation(amount):
    if amount < 0 or amount > 40:
        return False
    return True

def clothing_validation(amount):
    if amount < 0 or amount > 150:
        return False
    return True

def electrical_validation(amount):
    if amount < 0 or amount > 1000:
        return False
    return True

def insert_order():
    print("Insert a customer order carefully")
    order_id = input("Enter Order ID:")
    operator = input("Operator Name:")

    while True:
        item = input("Item:")

        while True:
            print("Enter a category\nfood or clothing or electrical:")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrical":
                print("Invalid category, e-select again")
                continue 
            else:
                break

        total = 0
        while True:
            try:
                amount = int(input("Price:"))
                if category == "food":
                    if not food_validation(amount):
                        print("Invalid price, re-enter correct price")
                        continue 
                    else:
                        total += amount
                        break
                elif category == "clothing":
                    if not clothing_validation(amount):
                        print("Invalid price, re-enter correct price")
                        continue 
                    else:
                        total += amount
                        break 
                elif category == "electrical":
                    if not electrical_validation(amount):
                        print("Invalid price, re-enter correct price")
                        continue 
                    else:
                        total += amount
                        break
            except ValueError:
                print("Enter a price, NUMBERS only, NO CHARACTERS")
                continue 

            choice = input("Do you want to exit?").lower()
            if choice == "y":
                print("Order successfully added onto system")
                break
            else:
                continue 
        
        cursor.execute("""
        INSERT INTO expenses(
                t_order_id,
                t_operator,
                t_item,
                t_category,
                t_amount)
        VALUES(?,?,?,?,?)
        """,(order_id,operator,item,category,amount))

        conn.commit()
        
        choice = input("Do you want to exit?").lower()
        if choice == "y":
            print("Order successfully added onto system")
            break
        else:
            continue 

def display_all():
    print("Display All Customer Orders")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    total = 0
    for i in range(len(rows)-1):
        previous_order = rows[i]
        current_order = rows[i+1]

        total += previous_order[5]

        if previous_order[1] != current_order[1]:
            print(f"Order Number:{previous_order[1]} Total:{total}")

    previous_order = rows[-1]
    total += previous_order[5]
    print(f"Order Number:{previous_order[1]} Total:{total}")

def search_order():
    print("Search For A Customer Order")
    while True:
        try:
            order_id = int(input("Order ID:"))
            break 
        except ValueError:
            print("Enter a price, NUMBERS only, NO CHARACTERS")
            continue 

    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    total = 0
    for row in rows:
        print("Customer Order", row)
        total += row[5]
    print("Total: ",total)

def delete_order():
    
    print("Search For A Customer Order")
    while True:
        try:
            order_id = int(input("Order ID:"))
            break 
        except ValueError:
            print("Enter a price, NUMBERS only, NO CHARACTERS")
            continue 
    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return

    choice = input("Are you sure you want to delete, customer order?").lower()
    if choice == "y":
        cursor.execute("""
        DELETE FROM expenses
        WHERE t_order_id = ?
        """,(order_id,))
        print("Order sucessfully deleted")
    else:
        print("Delete cancelled, order still exists")
        
    conn.commit()

def update_order():
    print("Insert a customer order carefully")

    pri_row_id = input("Enter OLD PRIMARY Row ID - (SAME EXISTING PRIMARY KEY NUMBER):")

    old_id = input("Enter OLD Order ID - (SAME EXISTING ORDER ID NUMBER):")
    operator = input("Operator Name:")

    while True:
        item = input("Item:")

        while True:
            print("Enter a category\nfood or clothing or electrical:")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrical":
                print("Invalid category, e-select again")
                continue 
            else:
                break

        total = 0
        while True:
            try:
                amount = int(input("Price:"))
                if category == "food":
                    if not food_validation(amount):
                        print("Invalid price, re-enter correct price")
                        continue 
                    else:
                        total += amount
                        break
                elif category == "clothing":
                    if not clothing_validation(amount):
                        print("Invalid price, re-enter correct price")
                        continue 
                    else:
                        total += amount
                        break 
                elif category == "electrical":
                    if not electrical_validation(amount):
                        print("Invalid price, re-enter correct price")
                        continue 
                    else:
                        total += amount
                        break 
            
            except ValueError:
                print("Enter a price, NUMBERS only, NO CHARACTERS")
        
        cursor.execute("""
        UPDATE expenses
        SET t_order_id = ?,
            t_operator = ?,
            t_item = ?,
            t_category = ?,
            t_amount = ?
        WHERE t_id = ?
        """,(old_id,operator,item,category,amount,pri_row_id))
        
        conn.commit()
        if cursor.rowcount > 0:
            print("Order sucessfully updated")
            break 
        else:
            print("Order not found")
            break 
    
def main():
    while True:
        menu()
        choices = input("Enter a choice: ")
        
        if choices == "1":
            insert_order()
        elif choices == "2":
            display_all()
        elif choices == "3":
            search_order()
        elif choices == "4":
            delete_order()
        elif choices == "5":
            update_order()
        elif choices == "6":
            print("Goodbye")
            break 
        else:
            print("Invalid Choice")

main()
        
                
          


    



