from decorators import (
    validate_username,
    validate_age,
    validate_gender,
    validate_address,
    check_hostel_input
)
from db import DB


class Student(DB):

    def __init__(self):
        super().__init__()
        self.student_id = "STU" + str(self.set_student_id()).zfill(2)
        self.name = self.set_name()
        self.age = self.set_age()
        self.gender = self.set_gender()
        self.address = self.set_address()

        self.course = None
        self.course_fees = 0
        self.set_course()

        self.hostel_status = False
        self.hostel_fees = 0
        self.food_charges = 0
        self.transportation_charges = 0
        self.set_hostel()

        self.total_fees = self.calculate_total_fees()

    # --------------------- Setters ----------------------

    def set_student_id(self):
        try:
            self.connect_db()
            cursor = self.create_cursor()

            query = "SELECT COUNT(*) FROM Student;"
            cursor.execute(query)

            return cursor.fetchone()[0] + 1

        except Exception as e:
            print("Database Error:", e)
            return 1

        finally:
            self.close_cursor()

    @validate_username
    def set_name(self):
        return input("Enter the student's name: ")

    @validate_age
    def set_age(self):
        return input("Enter the student's age: ")

    @validate_gender
    def set_gender(self):
        return input("Enter the student's gender: ")

    @validate_address
    def set_address(self):
        return input("Enter the student's address: ")

    def set_course(self):
        course_fees = 200000

        while True:
            print("\nSelect Course:")
            print("1: HR")
            print("2: Finance")
            print("3: Marketing")
            print("4: Data Science")
            print("5: Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("1: HR Core")
                print("2: HR Analytics")
                optional = int(input("Enter choice: "))

                if optional == 1:
                    self.course = "HR Core"
                    self.course_fees = course_fees
                    break

                elif optional == 2:
                    self.course = "HR Analytics"
                    self.course_fees = course_fees * 1.20
                    break

            elif choice == 2:
                self.course = "Finance"
                self.course_fees = course_fees
                break

            elif choice == 3:
                print("1: Marketing Core")
                print("2: Marketing Analytics")
                optional = int(input("Enter choice: "))

                if optional == 1:
                    self.course = "Marketing Core"
                    self.course_fees = course_fees
                    break

                elif optional == 2:
                    self.course = "Marketing Analytics"
                    self.course_fees = course_fees * 1.20
                    break

            elif choice == 4:
                self.course = "Data Science"
                self.course_fees = course_fees
                break

            elif choice == 5:
                break

            else:
                print("Invalid choice. Try again.")

    @check_hostel_input
    def hostel_input(self):
        return input("Do you want Hostel Facilities? (yes/no): ")

    def set_hostel(self):
        self.hostel_status = self.hostel_input().lower()

        if self.hostel_status == 'yes':
            years = int(input("Enter number of years for hostel: "))

            self.hostel_fees = 200000 * years
            self.food_charges = 2000 * (years * 12)
            self.transportation_charges = 13000 * ((years * 12) // 6)
        else:
            self.hostel_fees = 0
            self.food_charges = 0
            self.transportation_charges = 0

    def calculate_total_fees(self):
        return (
            self.course_fees
            + self.hostel_fees
            + self.food_charges
            + self.transportation_charges
        )

    # --------------------- Getters ----------------------

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def get_course(self):
        return self.course

    def get_course_fees(self):
        return self.course_fees

    def get_hostel_status(self):
        return self.hostel_status

    def get_hostel_fees(self):
        return self.hostel_fees

    def get_food_charges(self):
        return self.food_charges

    def get_transportation_charges(self):
        return self.transportation_charges

    def get_total_fees(self):
        return self.total_fees