import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

class Consultant():
    def __init__(self,first_name,surname,department_id):
        self.first_name = first_name
        self.surname = surname
        self.department_id = department_id
    
    def show_details_consultant(self):
        print(f"First Name:{self.first_name}")
        print(f"Last Name:{self.surname}")
        print(f"Department ID:{self.department_id}")
    
    def validate_login_id(self,number):
        if number < 1:
            return False
        return True
    
    def validate_name(self,name):
        for letter in name:
            if not letter.isalpha() and not letter == " ":
                return False
        return True
    
    def validate_yes_no(self,selected):
        if selected != 'y' and selected != 'n':
            return False
        return True
    
    def create_consultant(self):
        while True:
            self.first_name = input("First Name:")
            if self.first_name == "":
                print("Invalid input")
                continue 
            if not self.validate_name(self.first_name):
                print("Invalid input")
                continue 
            break 

        while True:
            self.surname = input("Last Name:")
            if self.surname == "":
                print("Invalid input")
                continue 
            if not self.validate_name(self.surname):
                print("Invalid input")
                continue 
            break 
        
        while True:
            try:
                self.department_id = int(input("Department ID:"))
                if not self.validate_login_id(self.department_id):
                    continue 
                break 
            except ValueError:
                print("Invalid input - Enter Department ID numerically only!")
                continue
        
        specialist = Consultant(
            self.first_name,
            self.surname,
            self.department_id
        )
        
        try:
            cursor.execute("""
            INSERT INTO consultant(
                       first_name,
                       surname,
                       department_id)
            VALUES(?,?,?)
            """,(specialist.first_name,specialist.surname,specialist.department_id))

            conn.commit()
            print("Consultant inserted successfully")

        except sqlite3.IntegrityError:
            print("Department ID non existant - Consultant not inserted")
            return

        row = cursor.lastrowid
        print(row)
        self.show_details_consultant()
        return
    
    def display_all_consultants(self):
        cursor.execute("SELECT * FROM consultant")
        
        rows = cursor.fetchall()
        if not rows:
            print("No consultants found")
            return
        else:
            for row in rows:
                specialist = Consultant(
                    row[1],
                    row[2],
                    row[3]
                )
                print(row[0])
                specialist.show_details_consultant()
            return

    def search_consultant(self):
        while True:
            try:
                consultant_id = int(input("Consultant ID:"))
                if not self.validate_login_id(consultant_id):
                    continue 
                break 
            except ValueError:
                print("Invalid input - Enter Consultant ID in numerics")
                continue 

        cursor.execute("""
        SELECT * FROM consultant
        WHERE consultant_id = ?
        """,(consultant_id,))

        row = cursor.fetchone()
        if not row:
            print("Consultant not found")
            return
        else:
            specialist = Consultant(
                row[1],
                row[2],
                row[3]
            )
            print(row[0])
            specialist.show_details_consultant()
            return

    def update_consultant(self):
        while True:
            try:
                consultant_id = int(input("Consultant ID:"))
                if not self.validate_login_id(consultant_id):
                    continue 
                break 
            except ValueError:
                print("Invalid input - Enter Consultant ID in numerics")
                continue 
        
        cursor.execute("""
        SELECT * FROM consultant
        WHERE consultant_id = ?
        """,(consultant_id,))
        
        row = cursor.fetchone()
        if not row:
            print("Consultant not found")
            return
        else:
            specialist = Consultant(
                row[1],
                row[2],
                row[3]
            )
        print(row[0])
        specialist.show_details_consultant()

        while True:
            update = input("Are you sure you want to update consultant?").lower()
            if not self.validate_yes_no(update):
                print("Invalid input")
                continue
            if update == "n":
                print("Consultant update aborted")
                return
            else:
                while True:
                    updated_first_name = input("First Name:")
                    if updated_first_name == "":
                        print("Invalid input")
                        continue 
                    if not self.validate_name(updated_first_name):
                        print("Invalid input")
                        continue
                    break

                while True:
                    updated_surname = input("Last Name:")
                    if updated_surname == "":
                        print("Invalid input")
                        continue 
                    if not self.validate_name(self.surname):
                        print("Invalid input")
                        continue 
                    break 
                    
                while True:
                    try:
                        updated_department_id = int(input("Department ID:"))
                        if not self.validate_login_id(updated_department_id):
                            continue
                        break
    
                    except ValueError:
                        print("Invalid input - Enter Department ID numerically only!")
                        continue
            
                self.first_name = updated_first_name
                self.surname = updated_surname
                self.department_id = updated_department_id

                cursor.execute("""
                UPDATE consultant
                SET first_name = ?,
                    surname = ?,
                    department_id = ?
                WHERE consultant_id = ?
                """,(self.first_name,self.surname,self.department_id, consultant_id))

                conn.commit()
                print("Consultant successfully updated")
                return

    def delete_consultant(self):
        while True:
            try:
                consultant_id = int(input("Consultant ID:"))
                if not self.validate_login_id(consultant_id):
                    continue 
                break 
            except ValueError:
                print("Invalid input - Enter Consultant ID in numerics")
                continue 
        
        cursor.execute("""
        SELECT * FROM consultant
        WHERE consultant_id = ?
        """,(consultant_id,))
        
        row = cursor.fetchone()
        if not row:
            print("Consultant not found")
            return
        else:
            specialist = Consultant(
            row[1],
            row[2],
            row[3]
            )
            print(row[0])
            specialist.show_details_consultant()

            while True:
                delete = input("Are you sure you want to delete?").lower()
                if not self.validate_yes_no(delete):
                    continue 
                if delete == "n":
                    print("Consultant deletion aborted")
                    return
                else:
                    cursor.execute("""
                    DELETE FROM consultant
                    WHERE consultant_id = ?
                    """,(consultant_id,))

                    conn.commit()
                    print("Consultant sucesssfully deleted")
                    return
        
test = Consultant(
    "first_name",
    "surname",
    "department_id"
)
test.create_consultant()
    
        
