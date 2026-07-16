import sqlite3 
from datetime import datetime

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

class Patient():
    def __init__(self, first_name, surname, dob, address, gp_id):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.gp_id = gp_id
    
    def show_patient_details(self):
        print(f"First Name:{self.first_name}")
        print(f"Last Name:{self.surname}")
        print(f"Date of Birth:{self.dob}")
        print(f"Address:{self.address}")
        print(f"GP ID:{self.gp_id}")
    
    def validation_name(self,name):
        for letter in name:
            if not letter.isalpha() and not letter == " ":
                return False
        return True
    
    def validate_login_digits(self,number):
        if number <=0:
            return False
        return True
    
    def validate_dob(self,number):
        if number < 10:
            return False
        return True
    
    def validate_yes_no(self,choice):
        if choice != 'y' and choice != 'n':
            return False
        return True
    
    def create_patient(self):
        while True:
            self.first_name = input("First Name:")
            if self.first_name == "":
                print("Do not leave name blank!")
                continue
            if not self.validation_name(self.first_name):
                print("Invalid input")
                continue 
            break 

        while True:
            self.surname = input("Last Name:")
            if self.surname == "":
                print("Do not leave blank!")
                continue 
            if not self.validation_name(self.surname):
                print("Invalid input")
                continue 
            break 

        while True:
            
            invalid_dob = False

            self.dob = input("Date of Birth(DD/MM/YYYY):")
            if len(self.dob) != 10:
                print("Invalid input")
                continue 
            if self.dob[2] != "/" or self.dob[5] != "/":
                print("Invalid input")
                continue
            for value in self.dob:
                if value == "/":
                    continue
                if not value.isdigit():
                    invalid_dob = True
                    print("Invalid input")

            if invalid_dob == True:
                print("Re-enter the date of birth in correct format(DD/MM/YYYY)")
                continue

            if int(self.dob[0:2]) < 1 or int(self.dob[0:2]) > 31:
                print("Invalid input")
                continue 
            if int(self.dob[3:5]) < 1 or int(self.dob[3:5]) > 12:
                print("Invalid input")
                continue 
            if int(self.dob[6:10]) < 1900 or int(self.dob[6:10]) > datetime.now().year:
                print("Invalid input")
                continue 
            if int(self.dob[0:2]) > 30 and int(self.dob[3:5]) in [4,6,9,11]:
                print("Invalid input")
                continue 
            if(
                int(self.dob[0:2]) > 29 
                and int(self.dob[3:5]) == 2 
                and 
                (
                    int(self.dob[6:10]) % 400 == 0
                    or
                    (
                        int(self.dob[6:10]) % 4 == 0
                        and
                        int(self.dob[6:10]) % 100 != 0
                    )
                )
            ):
                print("Invalid input")
                continue
            
            if(
                int(self.dob[0:2]) > 28 
                and int(self.dob[3:5]) == 2 
                and 
                (
                    int(self.dob[6:10]) % 400 != 0
                    and
                    (
                        int(self.dob[6:10]) % 4 != 0
                        or
                        int(self.dob[6:10]) % 100 == 0
                    )
                )
            ):
                print("Invalid input")
                continue 
            break

        while True:
            self.address = input("Address:")
            if self.address == "":
                print("Do not leave blank!")
                continue

            invalid_char = False
            for character in self.address:
                if character.isalpha() or character.isdigit():
                    continue
                if character in [".", ",", "'", "-", "/", "&"]:
                    continue
                else:
                    invalid_char = True
                    break 
            if invalid_char == False:
                print("Please enter the correct address to proceed")
                continue
            
            digit_in_address = False
            for character in self.address:
                if character.isdigit():
                    digit_in_address = True
                    break
            if digit_in_address == False:
                print("Invalid address")
                continue
            break
    
        while True:
            gp = input("Does the patient have a GP").lower()
            if not self.validate_yes_no(gp):
                print("Invalid input")
                continue
            if gp == "y":
                try:
                    self.gp_id = int(input("GP ID:"))
                    if not self.validate_login_digits(self.gp_id):
                        print("Invalid input")
                        continue
                except ValueError:
                    print("Invalid input - Enter GP ID numerically only")
                    continue 

                cursor.execute("""
                SELECT * FROM gp
                WHERE gp_id = ?
                """,(self.gp_id,))

                row = cursor.fetchone()
                if not row:
                    print("No GP found")
                    continue 
                break
            
            else:
                self.gp_id = None 
                break

        cursor.execute("""
        INSERT INTO patient(
            first_name,
            surname,
            dob,
            address,
            gp_id)
        VALUES(?,?,?,?,?)
        """,(self.first_name,self.surname,self.dob,self.address,self.gp_id))

        conn.commit()
        print("Patient inserted sucessfully")
        row = cursor.lastrowid
        print(f"Patient ID:{row}")
        self.show_patient_details()

test = Patient(
    "first_name",
    "surname",
    "dob",
    "address",
    "gp_id"
    )
test.create_patient()
        
        


            
                

                    


                


        
            
            

                