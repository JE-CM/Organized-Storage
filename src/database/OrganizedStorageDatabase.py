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
        query_results = self.execute_query(insert_query)
        query_rows_added = query_results['rowcount']
        row_of_user_add = query_results['lastrowid']
        user_added = True if query_rows_added == 1 else False
        return user_added, row_of_user_add 

    def remove_user(self, key_to_search, value_to_remove, delete_multiple_users=False):
        assert(key_to_search in self.organized_storage_table_columns.keys())
        primary_key = self.get_primary_key()
        value_quoted_if_needed = self.quote_value_if_needed(key_to_search,value_to_remove)
        if ("primary" in self.organized_storage_table_columns[key_to_search] and not self.organized_storage_table_columns[key_to_search]["primary"]) or \
                "primary" not in self.organized_storage_table_columns[key_to_search]:
            results = self.user_search(key_to_search, value_to_remove)
            #assert(len(results) == 0)
            if (len(results) == 0):
                return False
            elif (len(results) == 1):
                user_id = results[0][primary_key]
                remove_query = f"DELETE FROM {self.user_table_name} WHERE {primary_key} = {user_id};"
            elif (len(results) > 1) and (delete_multiple_users == True):
                #DELETE FROM users WHERE name = 'Alice';
                remove_query = f"DELETE FROM {self.user_table_name} WHERE {key_to_search} = {value_to_remove};"
            else:
                remove_query = f"DELETE FROM {self.user_table_name} WHERE {primary_key} = {user_id};"
                return False
        
        query_results = self.execute_query(remove_query)
        num_rows_removed = query_results['rowcount']
        assert(not num_rows_removed > 1)
        user_removed = True if num_rows_removed == 1 else False
        return user_removed

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
        query_results = self.execute_query(update_query)
        num_users_updated = query_results['rowcount']
        assert(not num_users_updated > 1)
        user_updated = True if num_users_updated == 1 else False
        return user_updated


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
        search_results = self.execute_query(search_query)['fetchall']
        table_column_names = self.organized_storage_table_columns.keys()
        search_results_as_dicts = []
        for result in search_results:
            search_results_as_dict = dict(zip(table_column_names, result))
            search_results_as_dicts.append(search_results_as_dict)
        return search_results_as_dicts

def sqlite_type_is_quoted(sqlite_type):
    return sqlite_type not in ['INTEGER', 'NUMERIC', 'REAL']

