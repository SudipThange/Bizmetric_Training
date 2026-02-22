import pyodbc

class DB:
    def connect_db(self):
        try:
            self.conn = pyodbc.connect(
                        r"Driver={ODBC Driver 17 for SQL Server};"
                        r"Server=DESKTOP-58V8UBA\SQLEXPRESS01;"
                        r"Database=Hostel;"
                        r"Trusted_Connection=yes;"
            )
        except Exception as e:
            print(e)
        
    def create_cursor(self):
        try:
            return self.conn.cursor()
        except Exception as e:
            print(e)
            
    def close_cursor(self):
        try:
            self.cursor = None
        except Exception as e:
            print(e)
            
    def close_db(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)