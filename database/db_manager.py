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
                CREATE IF NOT EXISTS TABLE Categeries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                )
            ''')

            default_categories = ['Food', 'Transport', 'Rent', 'Entertainment', 'Others']
            for category in default_categories:
                cursor.execute("INSERT OR IGNORE INTO Categories (name)", (category,))

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    descripcion TEXT,
                    date TEXT DEFAULT (date('now'))
                    category_id INTEGER,
                    CONTRAINT FOREIGN KEY category_id REFERENCES Categories(id)
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
        

    def update_expense(self, id, description=None, amount=None):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            if description:
                cursor.execute('''
                    UPDATE Expenses SET description=?
                    WHERE id=?
                ''', (description, id))

            if amount:
                cursor.execute('''
                    UPDATE Expenses SET amount=?
                ''', (amount, id))
            
            conn.commit()


    def delete_expense(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE * FROM Expenses WHERE id=?
            ''', (id,))

            conn.commit()

    
    def get_summary_all_expenses(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT SUM(amount) FROM Expenses
            ''')

            return cursor.fetchone()

    
    def get_summary_expenses_of_month(self, month, year):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT SUM(amount)
                FROM Expenses
                WHERE CAST(strftime('%m', date) AS INTEGER) = ? 
                    AND CAST(strftime('%Y', date) AS INTEGER) = ?
            ''', (month, year))

            return cursor.fetchone()

            