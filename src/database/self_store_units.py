import os
import sys

# Add the directory containing the SqliteDatabase package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "/database/"))

from OrganizedStorageDatabase import OrganizedStorageDatabase

class SelfStoreUnitDatabase(OrganizedStorageDatabase):
    # The unit operations of the self-storage modality require basic unit data as
    # well as a reference to the customers which are authorized to access the unit
    SELF_STORE_AUTHORIZED_USER_LIST_NAME = "authorized_user_list"
    SELF_STORE_UNITS_DB_COLUMNS = {
        "id": {
            "primary": True,
            "type": "INTEGER",
        },
        "number": {
            "type": "TEXT",
        },
        "facility_address": {
            "type": "TEXT",
        },
        # List of user IDs, separated by commas
        SELF_STORE_AUTHORIZED_USER_LIST_NAME: {
            "type": "TEXT",
        },
    }
    def __init__(self, db_dir='~/',
                 self_store_units_db_filename='organized_storage_self_store_units.db'):
        super().__init__(db_dir,self_store_units_db_filename, self.SELF_STORE_UNITS_DB_COLUMNS)

    def remove_users_from_unit(self, unit_id, user_ids_to_remove):
        current_user_id_list = self.get_self_store_user_list_of_unit(unit_id)
        users_dont_exist = [user_id for user_id in user_ids_to_remove if user_id not in current_user_id_list]
        if len(users_dont_exist) != 0:
            raise Exception(f"Request to remove users(s) {users_dont_exist} invalid. They do not exist in the user list for unit {unit_id}") 
        new_user_id_list = [user_id for user_id in current_user_id_list if user_id not in user_ids_to_remove]
        new_user_id_list_dict = {
            self.SELF_STORE_AUTHORIZED_USER_LIST_NAME: ",".join(new_user_id_list)
        }
        # TODO: Rename update_user_by_id to update_row_by_id 
        return self.update_user_by_id(unit_id, new_user_id_list_dict)

    def add_users_to_units(self, unit_id, user_ids_to_add):
        current_user_id_list = self.get_self_store_user_list_of_unit(unit_id)
        users_already_added = [user_id for user_id in user_ids_to_add if user_id in current_user_id_list]
        if len(users_already_added) != 0:
            raise Exception(f"Request to add users(s) {users_already_added} invalid. They already exist in the user list for unit {unit_id}") 
        new_user_id_list = current_user_id_list
        new_user_id_list.extend(user_ids_to_add)
        new_user_id_list_dict = {
            self.SELF_STORE_AUTHORIZED_USER_LIST_NAME: ",".join(new_user_id_list)
        }
        # TODO: Rename update_user_by_id to update_row_by_id 
        return self.update_user_by_id(unit_id, new_user_id_list_dict)

    def get_self_store_user_list_of_unit(self, unit_id):
        # TODO: Rename user_search to row_search to update_row_by_id 
        results = self.user_search(self.get_primary_key(), unit_id)
        if len(results) == 0:
            return []
        assert(len(results) == 1)
        self_store_user_list_of_unit = [] if results[0][self.SELF_STORE_AUTHORIZED_USER_LIST_NAME] == '' else results[0][self.SELF_STORE_AUTHORIZED_USER_LIST_NAME].split(",")
        return self_store_user_list_of_unit

    def user_authorized_to_access_unit(self, unit_id, user_id):
        return user_id in self.get_self_store_user_list_of_unit(unit_id)

        