class OrganizedStorageDatabase(SqliteDatabase):
    def __init__(self, db_dir='~/.OrganizedStorageDatabase', db_filename='organized_storage.db'):
        super().__init__(db_dir,db_filename)
        self.user_table_name = "users"
        self.organized_storage_table_columns = {
            "id": {
                "primary": True,
                "type": "INTEGER",
            },
            "name": {
                "type": "TEXT",
            },
            "address": {
                "type": "TEXT",
            },
            "hashed_password": {
                "type": "TEXT",
            },
            "password_salt": {
                "type": "TEXT",
            },
            "square_meters_used": {
                "type": "REAL",
            },
        }
        self.organized_storage_table_columns_as_sql = self.dict_to_sql_columns(self.organized_storage_table_columns)
        self.create_organized_storage_table()
    
    def dict_to_sql_columns(self, in_dictionary):
        out_sql_strings = []
        for key, value in in_dictionary.items():
            current_sql_string = ""
            current_sql_string += key
            current_sql_string += f" {value['type']}"
            if "primary" in value and value["primary"]:
                current_sql_string += " PRIMARY KEY"
            current_sql_string += " "
            out_sql_strings.append(current_sql_string)
        return out_sql_strings

    def create_organized_storage_table(self):
        table_create_query = f"CREATE TABLE IF NOT EXISTS {self.user_table_name} ( {', '.join(self.organized_storage_table_columns_as_sql)} )"
        return self.execute_query(table_create_query)
    
    def add_user(self, user_dict):
        assert(self.organized_storage_table_columns.keys() ==
               user_dict.keys())
        user_dict_keys = [key for key in user_dict]
        user_dict_values = [user_dict[key] for key in user_dict]
        user_dict_values_with_quotes_where_needed = [self.quote_value_if_needed(value) for value in user_dict_values]
        insert_query = f"INSERT INTO {self.user_table_name} ({', '.join(user_dict_keys)}) VALUES ({', '.join(user_dict_values_with_quotes_where_needed)})"
        return self.execute_query(insert_query)

    def remove_user(self, key_to_search, value_to_remove):
        assert(key_to_search in self.organized_storage_table_columns.keys())
        value_quoted_if_needed = self.quote_value_if_needed(value_to_remove)
        if ("primary" in self.organized_storage_table_columns[key_to_search] and not self.organized_storage_table_columns[key_to_search]["primary"]) or \
                "primary" not in self.organized_storage_table_columns[key_to_search]["primary"]:
            search_results = self.user_search(key_to_search, value_to_remove)
            assert(len(search_results) == 1)
        remove_query = f"DELETE FROM {self.user_table_name} WHERE {key_to_search} = {value_quoted_if_needed};"
        return self.execute_query(remove_query)

    # TODO: Add update_user
    # def update_user(self, key_to_search, user_dict_to_update):
    #     "UPDATE users SET email = 'newemail@example.com', age = 25 WHERE id = 1;"

    def quote_value_if_needed(self, key, value):
        search_value_needs_quotes = sqlite_type_is_quoted(self.organized_storage_table_columns[key]['type'])
        search_value_sql = f"'{value}'" if search_value_needs_quotes else f"{value}"
        return search_value_sql

    # Search for all users with a matching value in the specified key (column)
    def user_search(self, user_data_key, user_data_value, matches_exactly=False):
        assert(user_data_key in self.organized_storage_table_columns.keys())
        user_data_key_type = self.organized_storage_table_columns[user_data_key]['type']
        if not matches_exactly:
            assert(user_data_key_type == "TEXT")
            user_data_value = f"%{user_data_value}%"
        search_query = f"SELECT * FROM {self.user_table_name} WHERE {user_data_key} = {self.quote_value_if_needed(user_data_key, user_data_value)};"
        # TODO: Clean up SQL return value for search
        return self.execute_query(search_query)

def sqlite_type_is_quoted(sqlite_type):
    return sqlite_type not in ['INTEGER', 'NUMERIC', 'REAL']

def create_OrganizedStorage():
    test_db = OrganizedStorageDatabase('.','organized_storage_unittest.db')
    return test_db

def unittest_add_user(unittest_db, test_user):
    unittest_db.add_user(test_user)

def unittest_user_search(unittest_db, test_user):
    key_to_search = "name"
    results = unittest_db.user_search(key_to_search, test_user[key_to_search])
    assert(len(results) == 1)
    assert(results[0][key_to_search] == test_user[key_to_search])

def unittest_remove_user(unittest_db, test_user):
    key_to_search = "name"
    unittest_db.remove_user(key_to_search, test_user[key_to_search])

def unittest_user_search_on_removed_user(unittest_db, test_user):
    results = unittest_db.user_search(test_user)
    assert(len(results) == 0)

def unittests():
    unittest_db = create_OrganizedStorage()
    test_user = {
        "name": 'Alice',
        "address": '30 Giovanni Ln, Atlantis, 12345',
        "hashed_password": 'TODO_HASHED_PASSWORD',
        "password_salt": 'TODO_PASSWORD_SALT',
        "square_meters_used": 8.5,
    }
    unittest_add_user(unittest_db, test_user)
    unittest_user_search(unittest_db, test_user)
    unittest_update_user(unittest_db, test_user)
    unittest_remove_user(unittest_db, test_user)
    unittest_user_search_on_removed_user(unittest_db, test_user)
    

def main():
    unittests()

main()