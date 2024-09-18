import os
import sys

# Add the directory containing the SqliteDatabase package to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from db import SqliteDatabase

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
        columns_without_id = dict(self.organized_storage_table_columns)
        del columns_without_id["id"]
        assert(columns_without_id.keys() == user_dict.keys())
        user_dict_keys = [key for key in user_dict]
        user_dict_values_with_quotes_where_needed = [self.quote_value_if_needed(key, user_dict[key]) for key in user_dict]        
        insert_query = f"INSERT INTO {self.user_table_name} ({', '.join(user_dict_keys)}) VALUES ({', '.join(user_dict_values_with_quotes_where_needed)})"
        _, query_rowid = self.execute_query(insert_query)
        user_added = True if query_rowid else False
        return user_added, query_rowid

    def remove_user(self, key_to_search, value_to_remove):
        assert(key_to_search in self.organized_storage_table_columns.keys())
        primary_key = self.get_primary_key()
        primary_key_column_number = self.get_primary_key_column_number()
        value_quoted_if_needed = self.quote_value_if_needed(key_to_search,value_to_remove)
        if ("primary" in self.organized_storage_table_columns[key_to_search] and not self.organized_storage_table_columns[key_to_search]["primary"]) or \
                "primary" not in self.organized_storage_table_columns[key_to_search]:
            results = self.user_search(key_to_search, value_to_remove)
            assert(len(results) == 1)
            print(f"results == {results}")
            user_id = results[0][primary_key_column_number]
        remove_query = f"DELETE FROM {self.user_table_name} WHERE {primary_key} = {user_id};"
        print(f"value_to_remove == {value_to_remove}")
        print(f"remove_query == {remove_query}")
        _, query_rowid = self.execute_query(remove_query)
        print(f"query_rowid == {query_rowid}")
        user_removed = True if query_rowid else False
        return user_removed, query_rowid

    def get_primary_key_column_number(self):
        primary_key = self.get_primary_key()
        primary_key_column_number = next(
           (i for i, (key, _) in enumerate(self.organized_storage_table_columns.items()) if key == primary_key),
            None
        )
        return primary_key_column_number

    def get_primary_key(self):
        primary_keys = [key for key, value in self.organized_storage_table_columns.items() if value.get("primary") == True]
        assert(len(primary_keys) == 1)
        primary_key = primary_keys[0]
        return primary_key

    def update_user_by_id(self, user_id, user_dict_to_update):
        # assert(self.organized_storage_table_columns.keys() ==
        #        user_(dict.keys())
        primary_key = self.get_primary_key()
        user_dict_keys = [key for key in user_dict_to_update]
        user_dict_values_with_quotes_where_needed = [self.quote_value_if_needed(key, user_dict_to_update[key]) for key in user_dict_to_update]        
        zipped_keys_and_values = ', '.join([f"{key} = {value}" for key, value in zip(user_dict_keys, user_dict_values_with_quotes_where_needed)])
        update_query = f"UPDATE {self.user_table_name} SET {zipped_keys_and_values} WHERE {self.get_primary_key()} = {user_id}"
        _, query_rowid = self.execute_query(update_query)
        user_updated = True if query_rowid else False
        return user_updated, query_rowid


    def quote_value_if_needed(self, key, value):
        search_value_needs_quotes = sqlite_type_is_quoted(self.organized_storage_table_columns[key]['type'])
        search_value_sql = f"'{value}'" if search_value_needs_quotes else f"{value}"
        return search_value_sql

    # Search for all users with a matching value in the specified key (column)
    def user_search(self, user_data_key, user_data_value):
        assert(user_data_key in self.organized_storage_table_columns.keys())
        user_data_key_type = self.organized_storage_table_columns[user_data_key]['type']
        # TODO: matches_exactly does not work properly
        # if not matches_exactly:
        #     assert(user_data_key_type == "TEXT")
        #     user_data_value = f"%{user_data_value}%"
        search_query = f"SELECT * FROM {self.user_table_name} WHERE {user_data_key} = {self.quote_value_if_needed(user_data_key, user_data_value)};"
        print(f"search_query == {search_query}")
        # TODO: Clean up SQL return value for search
        search_result, _ = self.execute_query(search_query)
        return search_result

def sqlite_type_is_quoted(sqlite_type):
    return sqlite_type not in ['INTEGER', 'NUMERIC', 'REAL']

