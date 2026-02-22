import re

# ------------- Validate Username Decorator ------------------
def validate_username(func):
    def wrapper(*values, **kvalues):
        while True:
            username = func(*values, **kvalues)
            
            if not username.replace(" ", "").isalpha():
                print("Please, enter characters only!!")
            else:
                return username.strip().lower()
    return wrapper

# ------------- Validate Password Decorator ------------------
def validate_password(func):
    def wrapper(*values, **kvalues):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        while True:
            password = func(*values, **kvalues)
            
            if not re.fullmatch(pattern, password):
                print("Must contain atleast one uppercase, lowercase, special symbol & digit!!")
            else:
                return password
    return wrapper

def validate_age(func):
    def wrapper(*values, **kvalues):
        while True:
            age = func(*values, **kvalues)
            
            if not age.isdigit():
                print("Please enter number only...")
            elif int(age) <= 0 or int(age) >= 130:
                age = int(age)
                print("Please enter age between 1 to 130...")
            else:
                return int(age)                
    return wrapper

def validate_gender(func):
    def wrapper(*values, **kvalues):
        while True:
            gender = func(*values, **kvalues).lower()
            
            if not gender.isalpha():
                print("Please enter chars only...") 
            elif gender not in ('male', 'female'):
                print("Plese enter only from ('male', 'female')")
            else:
                return gender.capitalize()
    return wrapper

def validate_address(func):
    def wrapper(*values, **kvalues):
        while True:
            address = func(*values, **kvalues)
            
            if len(address) > 200:
                print("Address is too long...")
            else:
                return address
    return wrapper

def validate_admin_id(func):
    def wrapper(*values, **kvalues):
        while True:
            id = func(*values, **kvalues)
            
            if not id[:3] == "ADM":
                print("Please enter the correct id?: ")
            else:
                return id
    return wrapper

def check_hostel_input(func):
    def wrapper(*values, **kvalues):
        while True:
            status = func(*values, **kvalues).lower()
            
            if status not in ('yes', 'no'):
                print("Please only enter yes / no...")
                
            return status
    return wrapper