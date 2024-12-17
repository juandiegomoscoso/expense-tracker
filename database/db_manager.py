import sqlite3
from datetime import date

class DatabaseManager:
    def __init__(self, db_file="expenses.db"):
        # initialize database
        self.db_file = db_file
        self.init_database()

    def init_database(self):
        
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    descripcion TEXT,
                    date TEXT DEFAULT (date('now'))
                );
            ''')

            conn.commit()

