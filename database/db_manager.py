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


    def add_expense(self, description, amount, category_name='Others'):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM Categories WHERE name=?", (category_name,))
            result = cursor.fetchone()
            if result:
                category_id = result[0]
            else:
                raise ValueError(f"Category '{category_name}' not found in the database.")
            
            cursor.execute('''
                INSERT INTO Expenses (description, amount, category_id) 
                VALUES (?, ?, ?)
                ''', (description, amount, category_id))
            
            conn.commit()


    def get_expenses(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Expenses")
            return cursor.fetchall()
        

    def update_expense(self, id, description=None, amount=None, category_name=None):
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
                    WHERE id=?
                ''', (amount, id))
            
            if category_name:
                cursor.execute("SELECT id FROM Categories WHERE name=?", (category_name,))
                result = cursor.fetchone()
                if result:
                    category_id = result[0]
                else:
                    cursor.execute("INSERT INTO Categories (name) VALUES (?)", (category_name,))
                    category_id = cursor.lastrowid
                
                cursor.execute('''
                    UPDATE Expenses SET category_id=?
                    WHERE id=?
                ''', (category_id, id))
            
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

