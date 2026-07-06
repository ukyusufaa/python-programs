import sqlite3

conn = sqlite3.connect("car.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS client(
               c_id INTEGER PRIMARY KEY AUTOINCREMENT,
               c_name TEXT,
               c_address TEXT,
               c_phone TEXT,
               c_email TEXT
               )
""")

conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS car_rental(
               cr_id INTEGER PRIMARY KEY AUTOINCREMENT,
               cr_make TEXT,
               cr_model TEXT,
               cr_colour TEXT,
               cr_reg TEXT,
               cr_daily_price REAL,
               cr_availability TEXT,
               c_id INTEGER )
""")

conn.commit()

def menu():
    print("--- CAR RENTAL SYSTEM ---")
    print("1. Create Customer")
    print("2. Search Customer")
    print("3. Display All Customers")
    print("4. Update Customer")
    print("5. Delete Customer")
    print()
    print("6. Create Car")
    print("7. Search Car")
    print("8. Display All Cars")
    print("9. Rent Car")
    print("10. Return Car")
    print("11. Delete Car")
    print()
    print("0. Exit")

class Customer:
    def __init__(self,customer_id,name,address,phone,email):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    
    def show_customer(self):
        print(f"Customer ID:{self.customer_id}")
        print(f"Customer Name:{self.name}")
        print(f"Address & Post Code:{self.address}")
        print(f"Telephone or Mobile:{self.phone}")
        print(f"Email Address:{self.email}")

def validate_name(name):
    for letters in name:
        if not letters.isalpha() and not letters == " ":
            return False 
    return True

def create_customer():
    while True:
        name = input("Name:").strip()
        if name == "":
            print("Fill in a name please!")
            continue 
        if not validate_name(name):
            print("Enter full name with space!")
            continue 
        break

    while True:
        address = input("Address:").strip()
        if address == "":
            print("Fill in address please!")
            continue 
        break
    
    while True:
        phone = input("Phone or Mobile:").strip()
        if phone == "":
            print("Fill in contact numbers please!")
            continue
        break 
    
    while True:
        email = input("Email Address:")
        if email == "":
            print("Fill in email address please!")
            continue 
        break 
    
    new_customer = Customer(
        None,
        name,
        address,
        phone,
        email
    )

    cursor.execute("""
    INSERT INTO client(
                   c_name,
                   c_address,
                   c_phone,
                   c_email)
    values(?,?,?,?)
    """,(new_customer.name,
         new_customer.address,
         new_customer.phone,
         new_customer.email))
    
    conn.commit()
    
    new_customer.show_customer()

def search_customer():
    customer_id = int(input("SEARCH, Customer ID:"))

    cursor.execute("""
    SELECT * FROM client
    WHERE c_id = ?
    """,(customer_id,))

    row = cursor.fetchone()

    if not row:
        print("Customer not found")
    else:
        new_customer = Customer(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )
        new_customer.show_customer()
    
def display_all_customers():
    cursor.execute("SELECT * FROM client")

    rows = cursor.fetchall()

    if not len(rows):
        print("No customers found")
        return
    else:
        for row in rows:
            new_customer = Customer(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )
            new_customer.show_customer()
        return
    
def update_customer():
    customer_id = int(input("UPDATE, Customer ID:"))

    cursor.execute("""
    SELECT * FROM client
    WHERE c_id = ?
    """,(customer_id,))

    row = cursor.fetchone()

    if not row:
        print("Customer not found")
        return
    else:
        new_customer1 = Customer(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )
        new_customer1.show_customer()
    
    update = input("Do you want to update details?").lower()
    if update == "y":
        while True:
            name = input("Name:").strip()
            if name == "":
                print("Fill in a name please!")
                continue 
            if not validate_name(name):
                print("Enter full name with space!")
                continue 
            break

        while True:
            address = input("Address:").strip()
            if address == "":
                print("Fill in address please!")
                continue 
            break
    
        while True:
            phone = input("Phone or Mobile:").strip()
            if phone == "":
                print("Fill in contact numbers please!")
                continue
            break 
    
        while True:
            email = input("Email Address:")
            if email == "":
                print("Fill in email address please!")
                continue 
            break

        new_customer2 = Customer(
            customer_id,
            name,
            address,
            phone,
            email
        )
        
        cursor.execute("""
        UPDATE client
        SET c_name = ?,
            c_address = ?,
            c_phone = ?,
            c_email = ?
        WHERE c_id = ?
        """,(new_customer2.name,
             new_customer2.address,
             new_customer2.phone,
             new_customer2.email,
             new_customer1.customer_id))
        
        conn.commit()

        print("Customer sucessfully updated")
        new_customer2.show_customer()
        return
    else:
        print("Details not updated")
        return
    
def delete_customer():
    customer_id = int(input("DELETE, Customer ID:"))

    cursor.execute("""
    SELECT * FROM client
    WHERE c_id = ?
    """,(customer_id,))

    row = cursor.fetchone()

    if not row:
        print("Customer not found")
    else:
        new_customer = Customer(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )
    new_customer.show_customer()
    
    delete = input("Do you want to delete customer?").lower()
    if delete == "y":
        cursor.execute("""
        DELETE FROM client
        WHERE c_id = ?
        """,(customer_id,))

        conn.commit()
        print("Customer sucessfully deleted")
        return
        
    else:
        print("Delete process cancelled - customer still on system")
        return

class Car:
    def __init__(self,car_id,make,model,colour,reg,daily_rental_price,availability,cust_id):
        self.car_id = car_id
        self.make = make
        self.model = model 
        self.colour = colour 
        self.reg = reg
        self.daily_rental_price = daily_rental_price
        self.availability = availability
        self.cust_id = cust_id

    def show_car(self):
        print(f"Car ID:{self.car_id}")
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Colour:{self.colour}")
        print(f"Registration Number:{self.reg}")
        print(f"Daily Rental Price:{self.daily_rental_price}")
        print(f"Availability:{self.availability}")
        print(f"Customer ID:{self.cust_id}")

def validate_make(make):
    for letters in make:
        if not letters.isalpha():
            return False 
    return True

def validate_model(model):
    for letters in model:
        if not letters.isalpha():
            return False 
    return True

def validate_colour(colour):
    for letters in colour:
        if not letters.isalpha():
            return False 
    return True

def validate_reg(reg):
    if len(reg) !=7 or not reg.isalnum():
        return False
    return True

def car_rental_rates(make):
        if make == "Mercedes":
            return 100
        elif make == "BMW":
            return 95
        elif make == "Lexus":
            return 90
        elif make == "Audi":
            return 85
        elif make == "VW":
            return 80
        elif make == "Toyota":
            return 75
        elif make == "Volvo":
            return 50
        elif make == "Honda":
            return 45
        elif make == "Ford":
            return 40
        elif make == "Vauxhall":
            return 33
        elif make == "Suzuki":
            return 30
        elif make == "Nissan":
            return 25
        elif make == "Hyundai":
            return 20
        elif make == "Proton":
            return 13
        else:
            print("Invalid choice made")
            return
    
def create_car():

    while True:
        make = input("Make:").strip()
        if make == "":
            print("Error - Don't leave this field blank!")
            continue 
        if not validate_make(make):
            print("Error - Re-enter car make in one word using letters only!")
            continue 
        break
    while True:
        model = input("Model:").strip()
        if model == "":
            print("Error - Don't leave this field blank!")
            continue 
        if not validate_model(model):
            print("Error - Re-enter car model in one word using letters only!")
            continue 
        break
    while True:
        colour = input("Colour:").strip()
        if colour == "":
            print("Error - Don't leave this field blank!")
            continue 
        if not validate_colour(colour):
            print("Error - Re-enter car colour in one word using letters only!")
            continue 
        break
    while True:
        reg = input("Registration Number:").strip()
        if reg == "":
            print("Error - Don't leave this field blank!")
            continue 
        if not validate_reg(reg):
            print("Error - Re-enter car reg using 7 letters and numbers only!")
            continue 
        break
    
    daily_rental_price = car_rental_rates(make)
    availability = "Available"

    new_car = Car(
        None,
        make,
        model,
        colour,
        reg,
        daily_rental_price,
        availability,
        None
    )
    
    cursor.execute("""
    INSERT INTO car_rental(
            cr_make,
            cr_model,
            cr_colour,
            cr_reg,
            cr_daily_price,
            cr_availability
            )
    VALUES(?,?,?,?,?,?)
    """,(new_car.make,
         new_car.model,
         new_car.colour,
         new_car.reg,
         new_car.daily_rental_price,
         new_car.availability))
    
    conn.commit()
    new_car.show_car()
    return

def rent_car():
    renting_customer = None
    car_id = int(input("Car ID:"))

    cursor.execute("""
    SELECT * FROM car_rental
    WHERE cr_id = ?
    """,(car_id,))
    
    row = cursor.fetchone()

    if not row:
        print("car not found")
    else:
        the_car = Car(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7]
    )
    
        if row[6] != "Available":
            print("Car is unavailable")
            return
        else:
            the_car.show_car()
                
            customer_id = int(input("Customer ID:"))
            cursor.execute("""
            SELECT * FROM client
            WHERE c_id = ?
            """,(customer_id,))

            row = cursor.fetchone()

            if not row:
                print("Customer not found --- Add customer details to continue!")
                while True:
                    name = input("Name:").strip()
                    if name == "":
                        print("Fill in a name please!")
                        continue 
                    if not validate_name(name):
                        print("Enter full name with space!")
                        continue 
                    break
                while True:
                    address = input("Address:").strip()
                    if address == "":
                        print("Fill in address please!")
                        continue 
                    break
                while True:
                    phone = input("Phone or Mobile:").strip()
                    if phone == "":
                        print("Fill in contact numbers please!")
                        continue
                    break 
                while True:
                    email = input("Email Address:")
                    if email == "":
                        print("Fill in email address please!")
                        continue 
                    break 
                print("Customer details added sucessfully - now lets rent the car!")

                new_customer = Customer(
                    None,
                    name,
                    address,
                    phone,
                    email
                ) 
                cursor.execute("""
                INSERT INTO client(
                c_name,
                c_address,
                c_phone,
                c_email)
                values(?,?,?,?)
                """,(new_customer.name,
                new_customer.address,
                new_customer.phone,
                new_customer.email))
                
                conn.commit()

                renting_customer = new_customer
            else:
                existing_customer = Customer(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
                )
                renting_customer = existing_customer

        generated_id = cursor.lastrowid
        renting_customer.customer_id = generated_id

        cursor.execute("""
        UPDATE car_rental
        SET c_id = ?
        WHERE cr_id = ?
        """,(generated_id, car_id))

        renting_customer.show_customer()

        while True:
            try:
                rent_days = int(input("Rent car, how many days"))
                break
            except ValueError:
                print("Error - Enter days in 'Numbers' only")
                continue

        print("Car is now rented")
        total_rent = car_rental_rates(the_car.make) * rent_days
        print(total_rent)
        the_car.availability = "Unavailable"
        the_car.cust_id = generated_id
        
        cursor.execute("""
        UPDATE car_rental
        SET cr_availability = ?,
            c_id = ?
        WHERE cr_id = ?
        """,(the_car.availability,the_car.cust_id,car_id))

        conn.commit()

        the_car.show_car()
        renting_customer.show_customer()
        return
    
              
def search_car():
    car_id = int(input("Car ID:"))

    cursor.execute("""
    SELECT * FROM car_rental
    WHERE cr_id = ?
    """,(car_id,))

    row = cursor.fetchone()

    if not row:
        print("Car not found")
    else:
        new_car = Car(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7]
        )
        new_car.show_car()

def display_all_cars():
    cursor.execute("""
    SELECT * FROM car_rental
    """)

    rows = cursor.fetchall()

    if not len(rows):
        print("No cars found")
    else:
        for row in rows:
            new_car = Car(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7])
            new_car.show_car()
        return

def return_car():
    car_id = int(input("Return Car, Car ID:"))

    cursor.execute("""
    SELECT * FROM car_rental
    WHERE cr_id = ?
    """,(car_id,))

    row = cursor.fetchone()

    if not row:
        print("No car found")
    else:
        the_car = Car(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7]
        )
        the_car.show_car()
    
        car_returned = input("Return car?").lower()
        if car_returned == "y":
            the_car.availability = "AVAILABLE"

            cursor.execute("""
            UPDATE car_rental
            SET cr_availability = ?
            WHERE cr_id = ?
            """,(the_car.availability,car_id))

            conn.commit()

            print("Car has been returned to fleet")
            the_car.show_car()
            return
        else:
            print("Car is Unavailable")
            the_car.show_car()
            return

def delete_car():
    car_id = int(input("Car ID:"))

    cursor.execute("""
    SELECT * FROM car_rental
    WHERE cr_id = ?
    """,(car_id,))

    row = cursor.fetchone()

    if not row:
        print("No car not found")
    else:
        existing_car = Car(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        )

        existing_car.show_car()

        delete = input("Are you sure you want to delete this car?").lower()
        if delete == "y":
            if existing_car.availability == "Unavailable":
                print("This car is rented out - Delete not allowed")
            else:
                cursor.execute("""
                DELETE FROM car_rental
                WHERE cr_id = ?
                """,(car_id,))

                conn.commit()
                print("This car has sucessfully been deleted")
        else:
            print("Car is still here - delete has been cancelled")

def choices():
  
    while True:
        menu()
        answer = input("Select a numbered option from the menu:")
        if answer == "1":
            create_customer()
        elif answer == "2":
            search_customer()
        elif answer == "3":
            display_all_customers()
        elif answer == "4":
            update_customer()
        elif answer == "5":
            delete_customer()
        elif answer == "6":
            create_car()
        elif answer == "7":
            search_car()
        elif answer == "8":
            display_all_cars()
        elif answer == "9":
            rent_car()
        elif answer == "10":
            return_car()
        elif answer == "11":
            delete_car()
        elif answer == "0":
            print("Good Bye")
            break
        else:
            print("Invalid Option")

choices()







            



        







                    
        

