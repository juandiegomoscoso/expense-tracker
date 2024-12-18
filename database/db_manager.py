import sqlite3
from datetime import date

class DatabaseManager:
    def __init__(self, db_file="expenses.db"):
        # initialize database
        self.db_file = db_file
        self.init_database()

    def init_database(self):
        # Create Expenses table is not exists
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    descripcion TEXT,
                    date TEXT DEFAULT (date('now'))
                )
            ''')

            conn.commit()


    def add_expense(self, description, amount):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Expenses (description, amount) 
                VALUES (?, ?)
                ''', (description, amount))
            
            conn.commit()


    def get_expenses(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Expenses")
            return cursor.fetchall()