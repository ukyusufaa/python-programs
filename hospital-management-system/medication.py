import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

class Medication():
    def __init__(self,medication_name,cost):
        self.medication_name = medication_name
        self.cost = cost
    
    def show_medication_details(self):
        print(f"Medication Name:{self.medication_name}")
        print(f"Cost:{self.cost}")
    
    def validate_login_id(self,number):
        if number <= 0:
            return False
        return True
    
    def validate_medication_name(self,name):
        for letter in name:
            if not letter.isalpha() and not letter == " ":
                return False
        return True
    
    def validate_medication_cost(self,cost):
        if cost <=0 or cost != round(cost,2):
            return False
        return True

    def create_medication(self):
        while True:
            self.medication_name = input("Medication Name:")
            if self.medication_name == "":
                print("Do not leave blank!")
                continue
            if not self.validate_medication_name(self.medication_name):
                print("Invalid input")
                continue 
            break

        while True:
            try:
                self.cost = float(input("Cost:"))
                if not self.validate_medication_cost(self.cost):
                    continue 
                break 
            except ValueError:
                print("Invalid cost - Enter the cost numerically")
                continue

        meds = Medication(
        self.medication_name,
        self.cost
        )

        cursor.execute("""
        INSERT INTO medication(
                    medication_name,
                    cost)
        VALUES(?,?)
        """,(meds.medication_name, meds.cost))

        conn.commit()
    
    def display_all_medications(self):
        cursor.execute("SELECT * FROM medication")

        rows = cursor.fetchall()
        if not rows:
            print("No Medications found")
            return 
        else:
            for row in rows:
                meds = Medication(
                    row[1],
                    row[2]
                )
                print(row[0])
                meds.show_medication_details()
            input("Press Enter to return....")
    
    def search_medication(self):
        while True:
            try:
                medication_id = int(input("Medication ID:"))
                if not self.validate_login_id(medication_id):
                    print("Invalid ID")
                    continue 
                break 
            except ValueError:
                print("Invalid entry - use integers for ID")
                continue 
        
        cursor.execute("""
        SELECT * FROM medication
        WHERE medication_id = ?
        """,(medication_id,))

        row = cursor.fetchone()
        if not row:
            print("Search failed - no medication found")
            return
        else:
            meds = Medication(
                row[1],
                row[2]
            )
            print(row[0])
            meds.show_medication_details()
            input("Press Enter to exit...")
    
    def delete_medication(self):
        while True:
            try:
                medication_id = int(input("Medication ID:"))
                if not self.validate_login_id(medication_id):
                    print("Invalid input")
                    continue 
                break 
            except ValueError:
                print("Invalid input! - Enter ID in numeric format")
                continue 
        
        cursor.execute("""
        SELECT * FROM medication
        WHERE medication_id = ?
        """,(medication_id,))

        row = cursor.fetchone()
        if not row:
            print("No medication found")
            return
        else:
            meds = Medication(
                row[1],
                row[2]
                )
            print(row[0])
            meds.show_medication_details()

            delete = input("Are you sure you want to delete?")
            if delete == "y":
                cursor.execute("""
                DELETE FROM medication
                WHERE medication_id = ?
                """,(medication_id,))

                conn.commit()
                print("Medication deleted sucessfully")
                input("Press Enter to return")
            else:
                print("Delete process aborted!")

    def update_medication(self):
        while True:
            try:
                medication_id = int(input("Medication ID:"))
                if not self.validate_login_id(medication_id):
                    print("Invalid input")
                    continue 
                break 
            except ValueError:
                print("Invalid input! Enter ID in numeric format")
                continue 
        
        cursor.execute("""
        SELECT * FROM medication
        WHERE medication_id = ?
        """,(medication_id,))

        row = cursor.fetchone()
        if not row:
            print("No medication listed")
            return 
        else:
            meds = Medication(
                row[1],
                row[2]
            )
            print(row[0])
            meds.show_medication_details()
            
            update = input("Are you sure you want to update?")
            if update == "y":
                while True:
                    new_medication_name = input("Updated Medication Name:")
                    if new_medication_name == "":
                        print("Do not leave blank!")
                        continue
                    if not self.validate_medication_name(new_medication_name):
                        print("Invalid input")
                        continue 
                    break

                while True:
                    try:
                        new_cost = float(input("Updated Cost:"))
                        if not self.validate_medication_cost(new_cost):
                            print("Invalid input")
                            continue 
                        break 
                    except ValueError:
                        print("Invalid input - Enterthe cost in numerics only")
                        continue
                
                meds.medication_name = new_medication_name
                meds.cost = new_cost

                cursor.execute("""
                UPDATE medication
                SET medication_name = ?,
                    cost = ?
                WHERE medication_id = ?
                """,(meds.medication_name,meds.cost,medication_id))

                conn.commit()
                print("Medication updated successfully")
                input("Press enter to continue...")
            else:
                print("Medication update process aborted!")
                return

test = Medication(
    "medication",
    "cost"
)
test.display_all_medications()
        
    