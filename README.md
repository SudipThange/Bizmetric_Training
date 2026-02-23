# Bizmetric Assessments & Projects

This repository contains a collection of Python projects and assessments developed as part of Bizmetric training/assessments. It features two major systems: a **Hostel Management System** and a **Restaurant Management System**, along with various Python learning notebooks.

## Directory Structure

- **`py_projects/`**: Contains the main application projects.
    - **`Hostel/`**: A comprehensive Hostel Management System with SQL Server integration.
    - **`Restro/`**: A Restaurant Management System (Database-backed version in Jupyter Notebook).
- **`python/`**: Contains Python assessment notebooks and learning materials.
    - `Assessment.ipynb`: Basic Python exercises.
    - `List_compression_and_lambda.ipynb`: Advanced functional programming concepts.
    - `Restro.ipynb`: A standalone/prototype version of the Restaurant system.

---

## 1. Hostel Management System (`py_projects/Hostel`)

A robust console-based application designed to manage hostel operations, student registrations, and fee calculations.

### Features
*   **Admin Module (`admin.py`)**:
    *   **Authentication**: Admin registration and secure login.
    *   **Student Management**: Add new students to the database and view all registered students.
    *   **Fee Management**: Generate and print detailed fee receipts.
*   **Student Module (`student.py`)**:
    *   **Profile Management**: Captures Name, Age, Gender, and Address.
    *   **Course Selection**: Options include HR, Finance, Marketing, and Data Science (with sub-specializations).
    *   **Hostel & Transport**: Optional hostel facility with dynamic fee calculation based on duration (years).
*   **Database Integration (`db.py`)**:
    *   Powered by **Microsoft SQL Server**.
    *   Uses `pyodbc` for connectivity.
    *   **Tables**: `Admin`, `Student`.
*   **Advanced Validation (`decorators.py`)**:
    *   Custom decorators ensure data integrity:
        *   `@validate_username`: Ensures alphabetic characters.
        *   `@validate_password`: Enforces strong password policies (Upper, Lower, Digit, Special Char, Min 8 chars).
        *   `@validate_age`: Restricts age between 1 and 130.
        *   `@validate_gender`: Restricts input to 'Male'/'Female'.
        *   `@validate_admin_id`: Ensures IDs start with "ADM".
*   **Billing**:
    *   Generates text-based receipts in the `Bills/` directory (e.g., `student_name.txt`).
    *   Receipts include a breakdown of Course Fees, Hostel Fees, Food Charges, and Transport Charges.

### Usage
1.  Configure the database connection in `db.py` (Server: `DESKTOP-58V8UBA\SQLEXPRESS01`, DB: `Hostel`).
2.  Run the admin interface:
    ```bash
    cd py_projects/Hostel
    python admin.py
    ```
3.  Use `menu.ipynb` for testing or viewing execution logs.

---

## 2. Restaurant Management System (`py_projects/Restro`)

A database-driven Restaurant Management System implemented within a Jupyter Notebook (`RestroDB.ipynb`).

### Features
*   **Role-Based Access**:
    *   **Admin**: capabilities to Add Admins, Add Waiters, Add Tables, and Add Menu Items.
    *   **Waiter**: (Role implied in DB schema).
*   **Database Integration**:
    *   Connects to **SQL Server** (Database: `Restro`).
    *   **Tables**: `Users` (Admins/Waiters), `Tables`, `Menu`.
*   **Menu & Ordering**:
    *   Categories: Starters, Main Course, Dessert, Beverages.
    *   Dynamic menu management (stored in DB).
*   **Table Management**:
    *   Track table status (e.g., Booked/Available).
*   **Billing System**:
    *   Generates bill files stored in a structured format: `Bills/YYYY/Month/Day/OrderFile.txt`.

### Files
*   **`RestroDB.ipynb`**: The main application logic connecting to the SQL database.
*   **`Bills/`**: Organized storage for generated order receipts.

---

## 3. Python Assessments (`python/`)

A collection of Jupyter Notebooks demonstrating Python proficiency.

*   **`Assessment.ipynb`**:
    *   Covers fundamental Python concepts.
    *   **Topics**: String slicing (e.g., `name[::2]`), indexing, and basic data manipulation.
*   **`List_compression_and_lambda.ipynb`**:
    *   Focuses on pythonic one-liners and functional programming.
    *   **Topics**: List Comprehensions, Lambda functions, `map`, `filter`.
*   **`Restro.ipynb`**:
    *   A prototype or non-DB version of the Restaurant system.
    *   Uses in-memory dictionaries for Menu storage instead of SQL Server.

---

## Requirements

To run these projects, ensure you have the following installed:

*   **Python 3.x**
*   **Jupyter Notebook**
*   **Microsoft SQL Server** (Express or Standard)
*   **Libraries**:
    ```bash
    pip install pyodbc notebook
    ```

## Database Configuration

Both the Hostel and Restaurant projects require a running SQL Server instance. Update the connection strings in `py_projects/Hostel/db.py` and `py_projects/Restro/RestroDB.ipynb` if your server details differ from:
*   **Driver**: ODBC Driver 17 for SQL Server
*   **Server**: `DESKTOP-58V8UBA\SQLEXPRESS01`
*   **Trusted_Connection**: yes
