import sqlite3

conn = sqlite3.connect("shazia.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
               t_id INTEGER PRIMARY KEY AUTOINCREMENT,
               t_order_id INTEGER,
               t_date TEXT,
               t_operator TEXT,
               t_item TEXT,
               t_category TEXT,
               t_amount INTEGER
)
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
    order_id = int(input("Enter Customer Order ID:"))
    date = input("Date:")
    operator = input("Operator Name:")

    while True:
        item = input("Item:")

        while True:
            print("Please select a category:\nfood or clothing or electrics\nThankyou")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrics":
                print("Invalid Category! Re-Enter The Correct Category!")
                continue 
            else:
                break 
        
        total = 0

        while True:
            try:
                amount = int(input("Price:"))
                if category == "food":
                    if not food_validation(amount):
                        print("ERROR - Please Re-Enter The Correct Price")
                        continue
                    else:
                        total += amount
                        break 
                elif category == "clothing":
                    if not clothing_validation(amount):
                        print("ERROR - Please Re-Enter The Correct Price")
                        continue
                    else:
                        total += amount
                        break 
                elif category == "electrics":
                    if not electrical_validation(amount):
                        print("ERROR - Please Re-Enter The Correct Price")
                        continue
                    else:
                        total += amount
                        break

            except ValueError:
                print("ERROR Characters Not Allowed - For Price Re-Enter 'NUMBERS' Only")
                continue 
        
        cursor.execute("""
        INSERT INTO expenses(
                t_order_id,
                t_date,
                t_operator,
                t_item,
                t_category,
                t_amount)
        
        VALUES(?,?,?,?,?,?)
        """,(order_id,date,operator,item,category,amount))

        conn.commit()
        choice = input("Do you want to exit?").lower()
        if choice == "y":
            print("Order sucessfully Added onto System")
            break 
        else:
            continue

def display_all():
    print("All Customer Orders Displayed")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No Customer Orders found")
        return
    total = 0

    for i in range(len(rows)-1):
        previous_order = rows[i]
        current_order = rows[i+1]

        total += previous_order[6]
        
        if previous_order[1] != current_order[1]:
             print(f"Customer Order No.:{previous_order[1]} Total:{total}")

             total = 0
            
    total += rows[-1][6]
    print(f"Customer Order No.:{previous_order[1]} Total:{total}")
       


def search_order():
    print("Search For A Customer Order")
    while True:
        try:
            order_id = int(input("Enter Customer Order ID:"))
            break 
        except ValueError:
            print("ERROR - Enter Numbers Only")
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
        print(row)
        total += row[6]
    print("Customer Order Total = ",total)

def delete_order():
    print("Delete a Customer Order")
    while True:
        try:
            order_id = int(input("Enter Customer Order ID:"))
            break 
        except ValueError:
            print("Numbers only and not charcaters")
            continue 
    cursor.execute("""
    SELECT * FROM expenses
    WHERE t_order_id = ?
    """,(order_id,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Order not found")
        return
    
    option = input("Are you sure you want to delete this order?").lower()
    if option == "y":
        cursor.execute("""
        DELETE FROM expenses
        WHERE t_order_id = ?
        """,(order_id,))
        print("Order sucessfully deleted")
    else:
        print("Order not deleted")

        conn.commit()

def update_order():
    old_order_id = int(input("Enter Current Customer Order ID"))

    new_order_id = int(input("Enter New Customer Order ID:"))
    date = input("Date:")
    operator = input("Operator Name:")

    while True:
        item = input("Item:")

        while True:
            print("Please select a category:\nfood or clothing or electrics\nThankyou")
            category = input("Category:")
            if category != "food" and category != "clothing" and category != "electrics":
                print("Invalid Category! Re-Enter The Correct Category!")
                continue 
            else:
                break 
        
        total = 0

        while True:
            try:
                amount = int(input("Price:"))
                if category == "food":
                    if not food_validation(amount):
                        print("ERROR - Please Re-Enter The Correct Price")
                        continue
                    else:
                        total += amount
                        break 
                elif category == "clothing":
                    if not clothing_validation(amount):
                        print("ERROR - Please Re-Enter The Correct Price")
                        continue
                    else:
                        total += amount
                        break 
                elif category == "electrics":
                    if not clothing_validation(amount):
                        print("ERROR - Please Re-Enter The Correct Price")
                        continue
                    else:
                        total += amount
                        break

            except ValueError:
                print("ERROR Characters Not Allowed - For Price Re-Enter 'NUMBERS' Only")

        cursor.execute("""
        UPDATE expenses
                       
        SET t_order_id = ?,
            t_date = ?,
            t_operator = ?,
            t_item = ?,
            t_category = ?,
            t_amount = ?
                       
        WHERE t_order_id = ?
                  
        """,(new_order_id,date,operator,item,category,amount,old_order_id))

        conn.commit()

        choice = input("Do you want to exit?").lower()
        if choice == "y":
            if cursor.rowcount > 0:
                print("Customer Order sucessfully updated")
            else:
                print("Customer Order does not exist")
            break 
        else:
            continue

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
        
                
          


    



