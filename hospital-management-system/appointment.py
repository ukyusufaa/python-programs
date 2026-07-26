import sqlite3
from datetime import datetime

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

class Appointment():

    def __init__(self, patient_id, appointment_date, 
                 appointment_time, consultant_id):
        
        self.patient_id = patient_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.consultant_id = consultant_id

    def show_details_appointment(self):
        print(f"Patient ID:{self.patient_id}")
        print(f"Appointment Date:{self.appointment_date}")
        print(f"Appointment Time:{self.appointment_time}")
        print(f"Consultant ID:{self.consultant_id}")

    def validate_user_login(self,number):
        if number < 1:
            return False
        return True

    def validate_yes_no(self,option):
        if option != 'y' and option != 'n':
            return False
        return True
    
    def create_appointment(self):
        while True:
            try:
                self.patient_id = int(input("Patient ID:"))
                if not self.validate_user_login(self.patient_id):
                    print("Invalid input")
                    continue
                break

            except ValueError:
                print("Invalid input - Enter Patient ID using numerics")
                continue
        try:
            cursor.execute("""
            SELECT * FROM patient
            WHERE patient_id = ?
            """,(self.patient_id,))

        except sqlite3.Error as e:
            print("Database error:", e)
            return
            
        row = cursor.fetchone()
        if not row:
            print("Patient not found")
            return
            
        while True:
            try:
                self.consultant_id = int(input("Consultant ID:"))
                if not self.validate_user_login(self.consultant_id):
                    print("Invalid input")
                    continue
                break

            except ValueError:
                print("Invalid input - Enter Consultant ID using numerics")
                continue
        try:
            cursor.execute("""
            SELECT * FROM consultant
            WHERE consultant_id = ?
            """,(self.consultant_id,))

        except sqlite3.Error as e:
            print("Database Error", e)
            return
                    
        row = cursor.fetchone()
        if not row:
            print("Consultant not found")
            return
    
        while True:
            self.appointment_date = (input("Appointment Date(MM/DD/YYYY):"))
            if self.appointment_date == "":
                print("Do not leave blank")
                continue 
            if len(self.appointment_date) != 10:
                print("Invalid input - Date invalid")
                continue
            if self.appointment_date[2] != "/" or self.appointment_date[5] != "/":
                print("Invalid input - Enter the correct separators")
                continue

            not_number = False
            for value in self.appointment_date:
                if value == "/":
                    continue 
                if not value.isdigit():
                    not_number = True
                    continue

            if not_number == True:
                print("Re_Enter date of birth using the correct format (MM/DD/YYYY)")
                continue

            if(int(self.appointment_date[0:2]) < 1
                or int(self.appointment_date[0:2])) > 31:
                print("Invalid input - Incorrect day")
                continue
            if(int(self.appointment_date[3:5]) < 1 
               or int(self.appointment_date[3:5])) > 12:
                print("Invalid input - Incorrect month")
                continue 
            if(int(self.appointment_date[6:10]) < 1900 
            or int(self.appointment_date[6:10])) > datetime.now().year:
                print("Invalid input - Incorrect year")
                continue

            if(int(self.appointment_date[0:2]) > 30 
               and int(self.appointment_date[3:5])) in [4,6,9,11]:
                print("Invalid input - Incorrect day for this month")
                continue

            if(
                int(self.appointment_date[0:2]) > 29 
                and int(self.appointment_date[3:5]) == 2
                and
                (
                    int(self.appointment_date[6:10]) % 400 == 0
                    or
                    (
                        int(self.appointment_date[6:10]) % 4 == 0
                        and
                        int(self.appointment_date[6:10]) % 100 != 0
                    )
                )
            ):
                print("Invalid input - Incorrect February leap year")
                continue 

            if(
                int(self.appointment_date[0:2]) > 28
                and int(self.appointment_date[3:5]) == 2
                and
                (
                    int(self.appointment_date[6:10]) % 400 != 0
                    and
                    (
                        int(self.appointment_date[6:10]) % 4 != 0
                        or 
                        int(self.appointment_date[6:10]) % 100 == 0
                    )
                )
            ):
                print("Invalid input -Incorrect February")
                continue

            appointment_date = datetime.strptime(self.appointment_date,"%d/%m/%Y")
            if appointment_date.date() <= datetime.now().date():
                print("Appointment date must be tommorrow or later.")
                continue
            break

        while True:
            self.appointment_time = input("Appointment Time(HH:MM):")
            if len(self.appointment_time) != 5:
                print("Invalid input - Time entry digits too short")
                continue
            if(not self.appointment_time[0:2].isdigit() 
            or not self.appointment_time[3:5].isdigit()):
                print("Invalid input - Cannot use alphabet for time")
                continue
            if self.appointment_time[2] != ":":
                print("Invalid input - Incorrect time separator used ")
                continue
            if(int(self.appointment_time[0:2]) < 8 
            or int(self.appointment_time[0:2]) > 18):
                print("Invalid input -Incorrect appointment hour")
                continue
            minutes = int(self.appointment_time[3:5])
            if(
                minutes < 0 or minutes >= 60
                    or
                    (
                        minutes != 00
                        and minutes != 15
                        and minutes != 30
                        and minutes != 45
                    )
                ):
                    print("Invalid input - Incorrect appointment minutes")
                    continue
            break

        try:
            cursor.execute("""
            SELECT * FROM appointment
            WHERE consultant_id = ? 
                AND appointment_date = ? 
                AND appointment_time = ?
            
            """,(self.consultant_id,
                self.appointment_date,
                self.appointment_time))

        except sqlite3.Error as e:
            print("Database Error", e)
            return

        row = cursor.fetchone()
        if row:
            print("Appointment unavailable - Please Re-book!")
        else:
            print("Appointment available")

            try:
                cursor.execute("""
                INSERT INTO appointment(
                        patient_id,
                        consultant_id,
                        appointment_date,
                        appointment_time
                        )
                VALUES(?,?,?,?)
                """,(self.patient_id,
                    self.consultant_id,
                    self.appointment_date,
                    self.appointment_time))

                conn.commit()

            except sqlite3.Error as e:
                print("Database Error", e)
                return

            print("Appointment successfully booked")
            row = cursor.lastrowid
            print(f"Appointment ID:{row}")
            self.show_details_appointment

    def display_all_appointments(self):
        try:
            cursor.execute("SELECT * FROM appointment")

        except sqlite3.Error as e:
            print("Database Error", e)
            return

        rows = cursor.fetchall()
        if not rows:
            print("No appointments found")
            return
        else:
            for row in rows:
                patient_appointment = Appointment(
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                    )
                print(f"Appointment ID:{row[0]}")
                patient_appointment.show_details_appointment()

    def search_appointment(self):
        while True:
            try:
                appointment_id = int(input("Appointment ID:"))
                if not self.validate_user_login(appointment_id):
                    print("Invalid input - incorrect appointment ID")
                    continue
                break
        
            except ValueError:
                print("Invalid input - Enter Appointment ID using numerics")
                continue

        try:
            cursor.execute("""
            SELECT * FROM appointment
            WHERE appointment_id = ?
            """,(appointment_id,))

        except sqlite3.Error as e:
            print("Database Error", e)
            return

        row = cursor.fetchone()
        if not row:
            print("Appointment not found")
            return
        else:
            patient_appointment = Appointment(
                row[1],
                row[2],
                row[3],
                row[4]
                )
            print(f"Appointment ID:{row[0]}")
            patient_appointment.show_details_appointment()
            return

    def update_appointment(self):
        while True:
            try:
                appointment_id = int(input("Appointment ID:"))
                if not self.validate_user_login(appointment_id):
                    print("Invalid input - incorrect appointment ID")
                    continue
                break
        
            except ValueError:
                print("Invalid input - Enter Appointment ID using numerics")
                continue

        try:
            cursor.execute("""
            SELECT * FROM appointment
            WHERE appointment_id = ?
            """,(appointment_id,))

        except sqlite3.Error as e:
            print("Database Error", e)
            return

        row = cursor.fetchone()
        if not row:
            print("Appointment not found")
            return
        else:
            patient_appointment = Appointment(
                row[1],
                row[2],
                row[3],
                row[4]
                )
            print(f"Appointment ID:{row[0]}")
            patient_appointment.show_details_appointment()

            while True:
                update = input("Do you want to update appointment?(y/n)").lower()
                if not self.validate_yes_no(update):
                    print("Invalid input - Enter y or n")
                    continue
                if update == "n":
                    print("Appointment update aborted")
                    break 
                else:
                    while True:
                        try:
                            updated_patient_id = int(input("Patient ID:"))
                            if not self.validate_user_login(updated_patient_id):
                                print("Invalid input - Patient ID - Error")
                                continue
                            break 
                        except ValueError:
                            print("Enter Patient ID numerically only")
                            continue

                    while True:
                        try:
                            updated_consultant_id = int(input("Consultant ID:"))
                            if not self.validate_user_login(updated_consultant_id):
                                print("Invalid input - Patient ID - Error")
                                continue
                            break 
                        except ValueError:
                            print("Enter Consultant ID numerically only")
                            continue

                    while True:
                        updated_appointment_date = input("Date(DD/MM/YYYY):")
                        not_number = False
                        for user_input in updated_appointment_date:
                            if user_input == "/":
                                continue
                            if not user_input.isdigit():
                                not_number = True
                                continue
                        if not_number == True:
                            print("Invalid input - Date must be in this format(DD/MM/YYYY)")
                            continue
                        if updated_appointment_date == "":
                            print("Do not leave blank!")
                            continue
                        if len(updated_appointment_date) != 10:
                            print("Invalid input - Date input incorrect")
                            continue
                        if(updated_appointment_date[2] != "/" 
                           or updated_appointment_date[5] != "/"):
                            print("Invalid input - wrong character used")
                            continue
                        if(int(updated_appointment_date[0:2]) < 1
                           or int(updated_appointment_date[0:2]) > 31):
                            print("Invalid input - incorrect day")
                            continue
                        if(int(updated_appointment_date[3:5]) < 1
                            or int(updated_appointment_date[3:5]) > 12):
                            print("Invalid input - incorrect month")
                            continue
                        if(int(updated_appointment_date[6:10]) < 1900
                            or int(updated_appointment_date[6:10]) > datetime.now().year):
                            print("Invalid input - incorrect month")
                            continue
                  
                        if(
                            int(updated_appointment_date[0:2]) > 29 
                            and int(updated_appointment_date[3:5]) == 2
                            and
                            (
                                int(updated_appointment_date[6:10]) % 400 == 0
                                or
                                (
                                    int(updated_appointment_date[6:10]) % 4 == 0
                                    and
                                    int(updated_appointment_date[6:10]) % 100 != 0
                                )
                            )
                        ):
                            print("Invalid input - Incorrect February leap year")
                            continue 
            
                        if(
                            int(updated_appointment_date[0:2]) > 28
                            and int(updated_appointment_date[3:5]) == 2
                            and
                            (
                                int(updated_appointment_date[6:10]) % 400 != 0
                                and
                                (
                                    int(updated_appointment_date[6:10]) % 4 != 0
                                    or 
                                    int(updated_appointment_date[6:10]) % 100 == 0
                                )
                            )
                        ):
                            print("Invalid input -Incorrect February")
                            continue

                        appointment_date = datetime.strptime(
                            patient_appointment.appointment_date,"%d/%m/%Y")
                        if appointment_date.date() <= datetime.now().date():
                            print("Appointment date must be tommorrow or later.")
                            continue 
                        break
                

                    while True:
                        updated_appointment_time = input("Appointment Time(HR:MM):")
                        if updated_appointment_time == "":
                            print("Do not leave blank!")
                            continue
                        if len(updated_appointment_time) != 5:
                           print("Invalid input - Time digit length incorrect")
                           continue
                        if(not updated_appointment_time[0:2].isdigit() 
                        or not updated_appointment_time[3:5].isdigit()):
                           print("Invalid input - Enter time using correct format (HR:MM)")
                           continue
                        if updated_appointment_time[2] != ":":
                           print("Invalid input - Wrong separator used between hour and mins")
                           continue
                        if(int(updated_appointment_time[0:2]) < 8 
                        or int(updated_appointment_time[0:2]) > 18):
                           print("Invalid input -Incorrect appointment hour")
                           continue
                        minutes = int(updated_appointment_time[3:5])
                        if(
                           minutes < 0 or minutes >= 60
                               or
                               (
                                   minutes != 00
                                   and minutes != 15
                                   and minutes != 30
                                   and minutes != 45
                               )
                           ):
                               print("Invalid input - Incorrect appointment minutes")
                               continue
                        break 
                
                patient_appointment.patient_id = updated_patient_id
                patient_appointment.consultant_id = updated_consultant_id
                patient_appointment.appointment_date = updated_appointment_date
                patient_appointment.appointment_time = updated_appointment_time

                try:
                    cursor.execute("""
                    SELECT * FROM appointment
                    WHERE consultant_id = ?
                    AND appointment_date = ?
                    AND appointment_time = ?
                    """,(patient_appointment.consultant_id,
                        patient_appointment.appointment_date,
                        patient_appointment.appointment_time))

                except sqlite3.Error as e:
                    print("Database Error", e)
                    return

                row = cursor.fetchone()
                if row:
                    print("Appointment unavailable - choose another appointment time/date")
                else:
                    try:
                        cursor.execute("""
                        UPDATE appointment
                        SET patient_id = ?,
                        consultant_id = ?,
                        appointment_date = ?,
                        appointment_time = ?
                        """,(patient_appointment.patient_id,
                         patient_appointment.consultant_id,
                         patient_appointment.appointment_date,
                         patient_appointment.appointment_time))

                        conn.commit()

                    except sqlite3.Error as e:
                        print ("Database Error", e)
                        return

                    print("Appointment successfully updated")

        
test = Appointment(
    "patient_id",
    "consultant_id",
    "appointment_date",
    "appointment_time"
    )
test.display_all_appointments()





        
            



            



        



    
        