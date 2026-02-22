from db import DB
from user import User
from decorators import *
from student import Student
from datetime import datetime
import os

class Admin(DB, User):
    __isLogged = False
    __user_id = None
    __user_passwrd = None
    
    # ------------- Setters ----------------------
    def set_id(self):
        try:
            self.connect_db()
            cursor = self.create_cursor()
            
            query = "SELECT COUNT(*) FROM Admin;"
            
            cursor.execute(query)
            
            return cursor.fetchone()[0] + 1
        except Exception as e:
            print(e)
            return 1
        finally:
            self.close_cursor()
            self.close_db()
            
    @validate_username
    def set_username(self):
        return input("Enter the user name?: ")
    
    @validate_password
    def set_password(self):
        return input("Enter the password?: ")
    
    @validate_age
    def set_age(self):
        return input("Enter the age?: ")
    
    @validate_gender
    def set_gender(self):
        return input("Enter the gender?: ")
    
    @validate_address
    def set_address(self):
        return input("Enter the address?: ")
    
    # ------------- Getters ------------------------
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.name
    
    def get_password(self):
        return self.password
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_address(self):
        return self.address
    
    # ------------- Register ------------------------
    def register(self):
        self.id = "ADM" + str(self.set_id()).zfill(2)
        self.name = self.set_username()
        self.password = self.set_password()
        self.age = self.set_age()
        self.gender = self.set_gender() 
        self.address = self.set_address()
        
        try:
            self.connect_db()
            cursor = self.create_cursor()
            
            query = """
            INSERT INTO [Admin] (id, name, password, age, gender, address)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, (
                self.id,
                self.name,
                self.password,
                self.age,
                self.gender,
                self.address
            ))
            
            cursor.commit()
            
            if cursor.rowcount > 0:
                print("Admin added !! User ID: ", self.id)
            else:
                raise Exception("Admin is not added !!")
        except Exception as e:
            print(e)
        finally:
            self.close_cursor()
            self.close_db()
    
    # ----------------- Check ID ------------------
    @validate_admin_id
    def check_admin_id(self):
        return input("Enter the user id?: ")
    
    # ----------------- LOGIN ---------------------
    def login(self):
        try:
            admin_id = self.check_admin_id()
            password = self.set_password()
            
            self.connect_db()
            cursor = self.create_cursor()
            
            query = """
            SELECT name, password FROM [Admin]
            WHERE id = ? AND password = ?;
            """
            
            cursor.execute(query, (
                admin_id, 
                password
            ))
            
            if cursor.fetchone():
                print(f"Admin: {admin_id} has Logged In !!")
                Admin.__user_id = admin_id
                Admin.__user_passwrd = password
                Admin.__isLogged = True
            else:
                raise Exception("Something Wrong !!")
        except Exception as e:
            print(e)
        finally:
            self.close_cursor()
            self.close_db()
    
    # ----------------------- ADD Students ------------------
    def add_students(self):
        try:
            if not Admin.__isLogged:
                print("Please Login First !!")
                self.login()

            student = Student()
            
            self.connect_db()
            cursor = self.create_cursor() 
            
            query = """
            INSERT INTO Student (id, name, age, gender, address, selected_course, course_fees, hostel_status, hostel_fees, food_charges, transportation_charges, total_fees)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, (
                student.get_student_id(),
                student.get_name(),
                student.get_age(),
                student.get_gender(),
                student.get_address(),
                student.get_course(),
                student.get_course_fees(),
                student.get_hostel_status(),
                student.get_hostel_fees(),
                student.get_food_charges(),
                student.get_transportation_charges(),
                student.get_total_fees()
            ))
            
            cursor.commit()
            
            if cursor.rowcount > 0:
                print("Student added successfully !!")
            else:
                raise Exception("Something went wrong !!")
        except Exception as e:
            print(e)
        finally:
            self.close_cursor()
            self.close_db()
            
    # -------------------- SHOW ALL STUDENTS ----------------------
    def display_students(self, res):
        print()
        print("-" * 130)
        print("|{:^128}|".format("ALL STUDENTS"))
        print("-" * 130)
        
        print("{:<10} {:<20} {:<8} {:<10} {:<30} {:<20} {:>15}".format(
            "Id", "Name", "Age", "Gender", "Address", "Course", "Total Fees"
        ))
        
        print("=" * 130)
        
        for row in res:
            print("{:<10} {:<20} {:<8} {:<10} {:<30} {:<20} {:>15}".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            ))
            
        print("=" * 130)
    
    def show_all_students(self):
        try:
            if not Admin.__isLogged:
                print("Please Login First !!")
                self.login() 
                
            self.connect_db() 
            cursor = self.create_cursor() 
            
            query = "SELECT id, name, age, gender, address, selected_course, total_fees FROM Student;"

            cursor.execute(query)
            
            res = cursor.fetchall()
            if res:
                self.display_students(res)
        except Exception as e:
            print(e)
        finally:
            self.close_cursor() 
            self.close_db() 
            
    # ------------------- SHOW ALL ADMINS -------------------
    def display_admins(self, res):
        print()
        print("-" * 80)
        print("|{:^78}|".format("ALL ADMINS"))
        print("-" * 80)
        
        print("{:<10} {:<20} {:<8} {:<10} {:<50}".format(
            "Id", "Name", "Age", "Gender", "Address"
        ))
        
        print("=" * 80)
        
        for row in res:
            print("{:<10} {:<20} {:<8} {:<10} {:<50}".format(
                row[0], row[1], row[3], row[4], row[5]
            ))
            
        print("=" * 80)
        
    def show_all_admins(self):
        try:
            if not Admin.__isLogged:
                print("Please Login First !!")
                self.login() 
                
            self.connect_db() 
            cursor = self.create_cursor() 
            
            query = "SELECT * FROM Admin;"
            
            cursor.execute(query)
            
            res = cursor.fetchall()
            
            if res:
                self.display_admins(res)
        except Exception as e:
            print(e)
        finally:
            self.close_cursor()
            self.close_db() 
            
    # ----------------------- PRINT BILL --------------------
    def print_on_console(self):
        res = self.print_fees()
        
        if not res:
            print("Empty !!")
            return
        
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        current_time = now.strftime("%I:%M:%S %p")

        print("\n" + "=" * 110)
        print(f"|{'STUDENT FEES STRUCTURE':^108}|")
        print("=" * 110)

        print(f"{'Date':<15}: {current_date}")
        print(f"{'Time':<15}: {current_time}")
        print("-" * 110)

        print(f"{'Student ID':<15}: {res[0]}")
        print(f"{'Name':<15}: {res[1]}")
        print(f"{'Course':<15}: {res[2]}")
        print("-" * 110)

        print(f"\n{'FEES DETAILS':^110}")
        print("-" * 110)

        if res[4].lower() == "no":
            print(f"{'Course Fees':<25}{'Hostel Status':<25}{'Total Amount':>30}")
            print("-" * 110)
            print(f"{res[3]:<25}{res[4].capitalize():<25}{res[8]:>30}")
        else:
            print(f"{'Course Fees':<18}{'Hostel Status':<18}{'Hostel Fees':<18}"
                f"{'Food Charges':<18}{'Transport Charges':<18}{'Total Amount':>20}")
            print("-" * 110)
            print(f"{res[3]:<18}{res[4].capitalize():<18}{res[5]:<18}"
                f"{res[6]:<18}{res[7]:<18}{res[8]:>20}")

        print("=" * 110)
            
    
    def print_fees(self):
        try:
            if not Admin.__isLogged:
                print("PLEASE LOGIN FIRST !!")
                self.login() 
                
            name = self.set_username()
            
            self.connect_db()
            cursor = self.create_cursor()
            
            query = """
            SELECT id, name, selected_course, course_fees, hostel_status, hostel_fees, food_charges, transportation_charges, total_fees 
            FROM Student WHERE name = ?;
            """
            
            cursor.execute(query, (
                name
            ))
            
            res = cursor.fetchone()
            
            if res:
                return res
        except Exception as e:
            print(e)
        finally:
            self.close_cursor()
            self.close_db()      
    
    # ----------------------- SAVE TO FILE ------------------
   
    def save_to_file(self):
        try:
            res = self.print_fees()

            if not res:
                print("No Record is Found !!")
                return

            now = datetime.now()
            current_date = now.strftime("%d-%m-%Y")
            current_time = now.strftime("%I:%M:%S %p")

            folder_path = r"C:\Users\Sudip\Downloads\Bizmetric_assessments\py_projects\Hostel\Bills"
            file_name = res[1].replace(" ", "_") + ".txt"
            file_path = os.path.join(folder_path, file_name)

            if os.path.exists(file_path):
                print("File Already Present !!")
                print("File Path:", file_path)
                return

            with open(file_path, "w") as file:
                file.write("=" * 110 + "\n")
                file.write(f"{'STUDENT FEES STRUCTURE':^110}\n")
                file.write("=" * 110 + "\n")

                file.write(f"Date : {current_date}\n")
                file.write(f"Time : {current_time}\n")
                file.write("-" * 110 + "\n")

                file.write(f"Student ID : {res[0]}\n")
                file.write(f"Name       : {res[1]}\n")
                file.write(f"Course     : {res[2]}\n")
                file.write("-" * 110 + "\n")

                file.write("FEES DETAILS\n")
                file.write("-" * 110 + "\n")

                if res[4].lower() == "no":
                    file.write(f"Course Fees : {res[3]}\n")
                    file.write(f"Hostel      : {res[4]}\n")
                    file.write(f"Total Fees  : {res[8]}\n")
                else:
                    file.write(f"Course Fees           : {res[3]}\n")
                    file.write(f"Hostel Fees           : {res[5]}\n")
                    file.write(f"Food Charges          : {res[6]}\n")
                    file.write(f"Transport Charges     : {res[7]}\n")
                    file.write(f"Total Fees            : {res[8]}\n")

                file.write("=" * 110 + "\n")

            print("File Saved Successfully ✅")
            print("File Path:", file_path)

        except Exception as e:
            print("Error:", e)
            
        
    # ----------------------- LOG-OUT -----------------------
    def logout(self):
        try:
            if not Admin.__isLogged:
                print("Admin has not logged in yet !!")
                return
                
            if Admin.__user_id == self.check_admin_id() and Admin.__user_passwrd == self.set_password():
                Admin.__user_id = None
                Admin.__user_passwrd = None
                Admin.__isLogged = None
                print("Admin Logged Out !!")
            else:
                raise Exception("Invalid user Id & Password !!")
        except Exception as e:
            print(e)
