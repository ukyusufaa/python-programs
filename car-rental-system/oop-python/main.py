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

def customer_id_num(clients):
    highest_cust_id = 1000

    for client in clients:
        if client.customer_id > highest_cust_id:
            highest_cust_id = client.customer_id
    return highest_cust_id + 1

def create_customer(clients):
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

    customer_id = customer_id_num(clients)
    
    new_customer = Customer(
        customer_id,
        name,
        address,
        phone,
        email
    )

    clients.append(new_customer)
    new_customer.show_customer()

def search_customer(clients):
    found = False
    customer_id = int(input("SEARCH, Customer ID:"))

    for client in clients:
        if customer_id == client.customer_id:
            found = True
            client.show_customer()
            break
    if found == False:
        print("Customer not found")
        return

def display_all_customers(clients):
    if len(clients) == 0:
        print("No customers found")
        return
    
    for client in clients:
        client.show_customer()
    return

def update_customer(clients):
    found = False
    customer_id = int(input("UPDATE, Customer ID:"))

    for client in clients:
        if customer_id == client.customer_id:
            found = True
            client.show_customer()
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
                client.name = name
                client.address = address
                client.phone = phone
                client.email = email
                print()
                client.show_customer()
                print("Customer sucessfully updated")
                return
            else:
                print("Details not updated")
    if found == False:
        print("Customer not found")
        return
    
def delete_customer(clients):
    found = False
    customer_id = int(input("DELETE, Customer ID:"))

    for client in clients:
        if customer_id == client.customer_id:
            found = True
            client.show_customer()
            delete = input("Do you want to delete customer?").lower()
            if delete == "y":
                clients.remove(client)
                print("Customer sucessfully deleted")
                for individual in clients:
                    individual.show_customer()
                    break 
            else:
                print("Delete process cancelled - customer still on system")
    if found == False:
        print("Customer not on system, try again")

class Car:
    def __init__(self,car_id,make,model,colour,reg,daily_rental_price,availability):
        self.car_id = car_id
        self.make = make
        self.model = model 
        self.colour = colour 
        self.reg = reg
        self.daily_rental_price = daily_rental_price
        self.availability = availability

    def show_car(self):
        print(f"Car ID:{self.car_id}")
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Colour:{self.colour}")
        print(f"Registration Number:{self.reg}")
        print(f"Daily Rental Price:{self.daily_rental_price}")
        print(f"Availability:{self.availability}")

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
    
def car_id_num(cars):
    highest_car_id = 1000

    for car in cars:
        if car.car_id > highest_car_id:
            highest_car_id = car.car_id
    return highest_car_id + 1

def create_car(cars):

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
    car_id = car_id_num(cars)
    
    new_car = Car(
        car_id,
        make,
        model,
        colour,
        reg,
        daily_rental_price,
        availability
    )

    cars.append(new_car)
    new_car.show_car()

def rent_car(cars):
    car_found = False
    car_id = int(input("Car ID:"))
    for car in cars:
        if car_id == car.car_id:
            car_found = True
            if car.availability == "Available":
                car.show_car()
                
                customer_found = False
                renting_customer = None
                customer_id = int(input("Customer ID:"))
                for client in clients:
                    if customer_id == client.customer_id:
                        customer_found = True
                        renting_customer = client
                        print("Customer Found")
                        client.show_customer()

                if customer_found == False:
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
                        customer_id,
                        name,
                        address,
                        phone,
                        email
                    ) 

                    clients.append(new_customer)
                    renting_customer = new_customer
                    renting_customer.show_customer()

                while True:
                    try:
                        rent_days = int(input("Rent car, how many days"))
                        if rent_days == "":
                            print("Do not leave field blank")
                            continue
                        break
                    except ValueError:
                        print("Error - Enter days in 'Numbers' only")
                        continue

                print("Car is now rented")
                total_rent = car_rental_rates(car.make) * rent_days
                print(total_rent)
                car.availability = "Unavailable"
                car.show_car()
                renting_customer.show_customer()
            
            else:
                print("Car Unavailable")
                return
                    
    if car_found == False:
        print("Car not found")
              
def search_car(cars):
    found = False
    car_id = int(input("Car ID:"))

    for car in cars:
        if car_id == car.car_id:
            found = True
            print("Car found")
            car.show_car()

    if found == False:
        print("Car not found")

def display_all_cars(cars):
    if len(cars)== 0:
        print("No cars found")
        return
    for car in cars:
        car.show_car()
    return
   
def return_car(cars):
    found = False
    car_id = int(input("Return Car, Car ID:"))

    for car in cars:
        if car_id == car.car_id:
            print("Car found")
            found = True
            car.show_car()
            car_returned = input("Return car?").lower()
            if car_returned == "y":
                car.availability = "AVAILABLE"
                print("Car has been returned to fleet")
                car.show_car()
                return
            else:
                print("Car is Unavailable")
                car.show_car()
                return
    if found == False:
        print("Car not found on system")
        return

def delete_car(cars):
    found = False
    car_id = int(input("Car ID:"))

    for car in cars:
        if car_id == car.car_id:
            found = True
            car.show_car()
            if car.availability == "Available":
                cars.remove(car)
                print("Car sucessfully deleted")
            else:
                print("Cannot delete a rented out car!")
    
    if found == False:
        print("Car not found on system")

def choices(clients,cars):
  
    while True:
        menu()
        answer = input("Select a numbered option from the menu:")
        if answer == "1":
            create_customer(clients)
        elif answer == "2":
            search_customer(clients)
        elif answer == "3":
            display_all_customers(clients)
        elif answer == "4":
            update_customer(clients)
        elif answer == "5":
            delete_customer(clients)
        elif answer == "6":
            create_car(cars)
        elif answer == "7":
            search_car(cars)
        elif answer == "8":
            display_all_cars(cars)
        elif answer == "9":
            rent_car(cars)
        elif answer == "10":
            return_car(cars)
        elif answer == "11":
            delete_car(cars)
        elif answer == "0":
            print("Good Bye")
            break
        else:
            print("Invalid Option")

clients = []
cars = []
choices(clients,cars)







            



        







                    
        

