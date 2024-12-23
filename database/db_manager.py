import sqlite3

class DatabaseManager:
    def __init__(self, db_file="expenses.db"):
        # initialize database
        self.db_file = db_file
        self.init_database()


    def init_database(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE
                )
            ''')

            default_categories = ['Food', 'Transport', 'Rent', 'Entertainment', 'Others']
            for category in default_categories:
                cursor.execute("INSERT OR IGNORE INTO Categories (name) VALUES (?)", (category,))

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    description TEXT,
                    date TEXT DEFAULT (date('now')),
                    category_id INTEGER,
                    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES Categories(id)
                )
            ''')

            conn.commit()


    def add_expense(self, description, amount, category_name):
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

            return cursor.lastrowid


    def get_expenses(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT e.id, e.date, e.description, e.amount, c.name
                FROM Expenses e
                LEFT JOIN Categories c
                    ON c.id = e.category_id
                ''')
            return cursor.fetchall()
        

    def update_expense(self, id, description=None, amount=None, category_name=None):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            
            if category_name:
                cursor.execute("SELECT id FROM Categories WHERE name=?", (category_name,))
                result = cursor.fetchone()
                if result:
                    category_id = result[0]
                else:
                    raise ValueError(f"Category '{category_name}' not found in the database.")
                
                cursor.execute('''
                    UPDATE Expenses SET category_id=?
                    WHERE id=?
                ''', (category_id, id))
            
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
            
            conn.commit()


    def delete_expense(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM Expenses WHERE id=?
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


    def add_category(self, category_name):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO Categories (name) VALUES (?)", (category_name,))
            except sqlite3.IntegrityError:
                raise ValueError(f"Category '{category_name}' already exists")
            
            conn.commit()
            return cursor.lastrowid


    def delete_category(self, category_id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE Expenses 
                SET category_id = NULL
                WHERE category_id = ?
            ''', (category_id,))

            cursor.execute('''
                DELETE FROM Categories 
                WHERE id = ?
            ''', (category_id,))

            conn.commit()


    def get_categories(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Categories
            ''')
            return cursor.fetchall()
        

    def update_category(self, category_id, category_name):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id
                FROM Categories
                WHERE name = ?
            ''', (category_name,))
            
            result = cursor.fetchone()

            if result:
                raise ValueError(f"Category '{category_name}' already exists.")
            else:
                cursor.execute('''
                    UPDATE Categories 
                    SET name = ?
                    WHERE id = ?
                ''', (category_name, category_id))
            
            conn.commit()

    
    def get_expenses_by_category(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT c.name, SUM(e.amount)
                FROM Expenses e
                JOIN Categories c
                    ON c.id = e.category_id
                GROUP BY c.name
            ''')

            return cursor.fetchall()

