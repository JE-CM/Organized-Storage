import os
import sqlite3

# TODO: Create a wrapper class for SqliteDatabase called
#       OrganizedStorageDatabase which has the table already built-in

class SqliteDatabase():
    def __init__(self, db_dir='~/.OrganizedStorageDatabase', db_filename='organized_storage.db'):
        self.db_dir = db_dir
        self.db_filename = db_filename
        self.db_path = db_dir + '/' + db_filename
    
    def execute_query(self, query):
        # Connect to a database (or create it if it doesn't exist)
        connection = sqlite3.connect(self.db_path)
        query_executed = False
        query_result = None
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute the query
            cursor.execute(query)
            query_executed = True
            # Commit the changes
            connection.commit()
            
            # Retrieve the results
            query_result = cursor.fetchall()
        finally:
            connection.close()

        return query_result
    
    def delete_db(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            print(f"Database '{self.db_path}' deleted successfully.")
            return True
        else:
            print(f"Database '{self.db_path}' does not exist.")
            return False
        

def unittest_create_db():
    return SqliteDatabase('.','unittest.db')

def unittest_create_table(my_db):
    # TODO: Potentially create a Composite (Multi-Column) PRIMARY KEY?
    my_db.execute_query('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            hashed_password TEXT,
            password_salt TEXT,
            square_meters_used REAL
        )
    ''')

def unittest_add_user(my_db):
    my_db.execute_query('''
        INSERT INTO users (name, address, hashed_password, password_salt, square_meters_used)
        VALUES ('Alice', '30 Giovanni Ln, Atlantis, 12345', 'TODO_HASHED_PASSWORD', 'TODO_PASSWORD_SALT', 8.5)
    ''')

def unittest_query_db(my_db):
    rows = my_db.execute_query('SELECT * FROM users')
    print(rows)

def unittests():
    test_failed = False
    try:
        my_db = unittest_create_db()
        unittest_create_table(my_db)
        unittest_add_user(my_db)
        unittest_query_db(my_db)
    except:
        test_failed = True
    finally:
        my_db.delete_db()

def main():
    unittests()

main()
