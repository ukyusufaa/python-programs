import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

class GpSurgery:
    def __init__(self,surgery_name,address):
        self.surgery_name = surgery_name
        self.address = address 
    
    def show_gpsurgery_details(self):
        print(f"Surgery Name:{self.surgery_name}")
        print(f"Address:{self.address}")
    
    def validate_surgeryname(self,name):
        for letter in name:
            if not letter.isalpha() and not letter == " ":
                return False
        return True
    
    def validate_id_input(self,number):
        if number <= 0:
            return False
        return True
    
    def create_gpsurgery(self):
        while True:
            self.surgery_name = input("Surgery Name:")
            if self.surgery_name == "":
                print("Do not leave blank!")
                continue
            if not self.validate_surgeryname(self.surgery_name):
                print("Invalid input")
                continue 
            break

        self.address = input("Address:")
        while True:
            if self.address == "":
                print("Do not leave blank!")
                continue 
            break

        cursor.execute("""
        INSERT INTO gp_surgery(
                       surgery_name,
                       address)
        VALUES(?,?)
        """,(self.surgery_name,self.address))

        conn.commit()

        print("GP Surgery created successfully")
        row = cursor.lastrowid
        print(f"Surgery ID:{row}")
        self.show_gpsurgery_details()
       
        input("Press Enter to continue.....")

    def display_all_gpsurgery(self):
        cursor.execute("SELECT * FROM gp_surgery")

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No GP surgeries found")
            return
        else:
            for row in rows:
                clinic = GpSurgery(
                    row[1],
                    row[2]
                )
                print(row[0])
                clinic.show_gpsurgery_details()
        return
    
    def search_gpsurgery(self):
        surgery_id = int(input("ID:"))
        while True:
            try:
                department_id = int(input("Department Name:"))
                if not self.validate_id_input(department_id):
                    continue 
                break
            except ValueError:
                print("Do not enter alphabet, enter ID using integers")
        
        cursor.execute("""
        SELECT * FROM gp_surgery
        WHERE surgery_id = ?
        """,(surgery_id,))

        row = cursor.fetchone()

        if not row:
            print("No GP surgery found")
            return
        else:
            clinic = GpSurgery(row[1],row[2])
            print(row[0])
            clinic.show_gpsurgery_details()
        return
    
    def delete_gpsurgery(self):
        surgery_id = int(input("ID:"))
        while True:
            try:
                if surgery_id == "":
                    print("Do not leave blank!")
                    continue 
                break
            except ValueError:
                print("Do not enter alphabet, enter ID using integers")
        
        cursor.execute("""
        SELECT * FROM gp_surgery
        WHERE surgery_id = ?
        """,(surgery_id,))

        row = cursor.fetchone()

        if not row:
            print("No GP surgery found")
            return
        else:
            gpsurgery = GpSurgery(row[1],row[2])
            print(row[0])
            gpsurgery.show_gpsurgery_details()

            delete = input("Are you sure you want to delete?")
            if delete == "y":
                cursor.execute("""
                DELETE FROM gp_surgery
                WHERE surgery_id = ?
                """,(surgery_id,))

                conn.commit()
                print("GP Surgery deleted sucessfully!")

            else:
                print("Deletion process aborted!")
    
    def update_gpsurgery(self):
        surgery_id = int(input("ID"))

        cursor.execute("""
        SELECT * FROM gp_surgery
        WHERE surgery_id = ?
        """,(surgery_id,))

        row = cursor.fetchone()

        if not row:
            print("GP Surgery not found")
            return 
        else:
            gpsurgery = GpSurgery(row[1],row[2])
            print(row[0])
            gpsurgery.show_gpsurgery_details()

            update = input("Are you sure you want to update?")
            if update == "y":
                while True:
                    new_surgery_name = input("Name:")
                    if new_surgery_name == "":
                        print("Do not leave blank!")
                        continue 
                    if not self.validate_surgeryname(new_surgery_name):
                        print("Invalid input")
                        continue 
                    break
               
                while True:
                    new_address = input("Address:")
                    if new_address == "":
                        print("Do not leave blank!")
                        continue 
                    break

                gpsurgery.surgery_name = new_surgery_name
                gpsurgery.address = new_address
                    
                cursor.execute("""
                UPDATE gp_surgery
                SET surgery_name = ?,
                    address = ?
                WHERE surgery_id = ?
                """,(gpsurgery.surgery_name,gpsurgery.address,surgery_id))

                conn.commit()
                print("GP Surgery updated sucessfully!")
                return
            else:
                print("Update process aborted!")
                return 

test = GpSurgery(
        "surgery_name",
        "address"
    )
test.create_gpsurgery()






