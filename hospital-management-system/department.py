import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

class Department():
    def __init__(self, department_name):
        self.department_name = department_name
    
    def show_department_details(self):
        print(f"Department Name:{self.department_name}")
    
    def validate_department_name(self,name):
        for letter in name:
            if not letter.isalpha() and letter != " ":
                return False
        return True
    
    def validate_id_input(self,number):
            if number <= 0:
                return False
            return True          

    def create_department(self):
        while True:
            self.department_name = input("Department Name:")
            if self.department_name == "":
                print("Do not leave blank!")
                continue 
            if not self.validate_department_name(self.department_name):
                print("Invalid Input")
                continue 
            break 

        dept = Department(
            self.department_name
        )

        cursor.execute("""
        INSERT INTO department(
                       department_name)
        VALUES(?)             
        """,(dept.department_name,))

        conn.commit()
        print("Department inserted at Medina Hospital successfully")
    
    def display_all_departments(self):
        cursor.execute("SELECT * FROM department")

        rows = cursor.fetchall()

        if not rows:
            print("No Departments found")
            return
        else:
            for row in rows: 
                new_dept = Department(
                row[1]
                )
                print(row[0])
                new_dept.show_department_details()
        return
    
    def search_department(self):
        while True:
            try:
                department_id = int(input("Department ID:"))
                if not self.validate_id_input(department_id):
                    print("Enter a positive integer for ID")
                    continue 
                break
            except ValueError:
                print("Enter ID using integers NO alaphabet")

        cursor.execute("""
        SELECT * FROM department
        WHERE department_id = ?
        """,(department_id,))

        row = cursor.fetchone()
        if not row:
            print ("No department found")
            return
        else:
            dept = Department(
                row[1]
            )
            print(row[0])
            dept.show_department_details()
            return
    
    def delete_department(self):
        while True:
            try:
                department_id = int(input("Department ID:"))
                if not self.validate_id_input(department_id):
                    print("Enter a positive integer for ID")
                    continue 
                break 
            except ValueError:
                print("ID, input only integers NOT alaphabet")
                continue
        
        cursor.execute("""
        SELECT * FROM department
        WHERE department_id = ?
        """,(department_id,))

        row = cursor.fetchone()
        if not row:
            print("No such department found")
            return
        else:
            dept = Department(
                row[1]
            )
            print(row[0])
            dept.show_department_details()

            delete = input("Are you sure you want to delete?")
            if delete == "y":
                cursor.execute("""
                DELETE FROM department
                WHERE department_id = ?
                """,(department_id,))

                conn.commit()

                print("Department deleted successfully")
                input("Press Enter to continue....")
            else:
                print("Delete process aborted")
    
    def update_department(self):
        while True:
            try:
                department_id = int(input("Department ID:"))
                if not self.validate_id_input(department_id):
                    print("ID must be positive integers only!")
                    continue 
                break 
            except ValueError:
                print("Id, enter integers only NOT alphabet")
                continue 
        
        cursor.execute("""
        SELECT * FROM department
        WHERE department_id = ?
        """,(department_id,))

        row = cursor.fetchone()
        if not row:
            print("No such department")
            return
        else:
            dept = Department(
                row[0]
            )
            print(row[0])
            dept.show_department_details()

            update = input("Are you sure you want to update?")
            if update == "y":
                while True:
                    new_dept_name = input("Department Name:")
                    if new_dept_name == "":
                        print("Do not leave blank!")
                        continue 
                    if not self.validate_department_name(new_dept_name):
                        continue 
                    break 

                dept.department_name = new_dept_name
                
                cursor.execute("""
                UPDATE department
                SET department_name = ?
                WHERE department_id = ?
                """,(dept.department_name,department_id))

                conn.commit()
                print("Department updated successfully")
                input("Press Enter to continue...")
            else:
                print("Update process aborted")
                return
                        
test = Department(
    "department"
    )

test.update_department()

            
