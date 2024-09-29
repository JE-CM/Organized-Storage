import os
import sys

# Add the directory containing the SqliteDatabase package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "/database/"))

from OrganizedStorageDatabase import OrganizedStorageDatabase

class SelfStoreUserDatabase(OrganizedStorageDatabase):
    # The user operations of the self-storage modality require basic customer data as
    # well as a reference to the storage unit(s) being used by the customer and the
    # price the customer pays for those units.
    SELF_STORE_UNIT_LIST_NAME = "storage_unit_list"
    SELF_STORE_UNIT_PRICE_LIST_NAME = "storage_unit_prices"
    SELF_STORE_USERS_DB_COLUMNS = {
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
        "phone_number": {
            "type": "TEXT",
        },
        "email_address": {
            "type": "TEXT",
        },
        "hashed_password": {
            "type": "TEXT",
        },
        "password_salt": {
            "type": "TEXT",
        },
        # List of storage unit IDs, separated by commas
        SELF_STORE_UNIT_LIST_NAME: {
            "type": "TEXT",
        },
        # List of prices paid for units in the order of storage_unit_list, separated by commas
        SELF_STORE_UNIT_PRICE_LIST_NAME: {
            "type": "TEXT",
        }
    }
    def __init__(self, db_dir='~/',
                 self_store_users_db_filename='organized_storage_self_store_users.db'):
        super().__init__(db_dir,self_store_users_db_filename, self.SELF_STORE_USERS_DB_COLUMNS)


    # TODO:
    # def remove_units_from_user():

    def add_units_to_user(self, user_id, unit_dict_list):
        units_to_add = [unit['id'] for unit in unit_dict_list]
        prices_of_units_to_add = [unit['price'] for unit in unit_dict_list]
        units = self.get_self_store_unit_list_of_user(user_id)
        unit_prices = self.get_self_store_unit_price_list_of_user(user_id)
        intersection_of_units_to_add_and_units = []
        for to_add in units_to_add:
            if to_add in units:
                intersection_of_units_to_add_and_units.append(to_add)
        if len(intersection_of_units_to_add_and_units) != 0:
            raise Exception(f"Request to add unit(s) {intersection_of_units_to_add_and_units} invalid. They already exist in the unit list for user {user_id}") 
        units.extend(units_to_add)
        unit_prices.extend(prices_of_units_to_add)
        units_to_update = dict()
        units_to_update[self.SELF_STORE_UNIT_LIST_NAME] = ",".join([str(n) for n in units])
        units_to_update[self.SELF_STORE_UNIT_PRICE_LIST_NAME] = ",".join([str(n) for n in unit_prices])
        return self.update_user_by_id(user_id, units_to_update)

    def get_self_store_unit_dict_of_user(self, user_id):
        results = self.user_search(self.get_primary_key(), user_id)
        if len(results) == 0:
            return dict()
        assert(len(results) == 1)
        self_store_unit_list_of_user = [] if results[0]["storage_unit_list"] == '' else results[0]["storage_unit_list"].split(",")
        self_store_unit_price_list_of_user = [] if results[0]["storage_unit_prices"] == '' else results[0]["storage_unit_prices"].split(",")
        return dict(zip(self_store_unit_list_of_user, self_store_unit_price_list_of_user))

    def get_self_store_unit_list_of_user(self, user_id):
        unit_dict = self.get_self_store_unit_dict_of_user(user_id)
        return list(unit_dict.keys())

    def get_self_store_unit_price_list_of_user(self, user_id):
        unit_dict = self.get_self_store_unit_dict_of_user(user_id)
        return list(unit_dict.values())

    def user_authorized_to_access_unit(self, unit_id, user_id):
        return unit_id in self.get_self_store_unit_list_of_user(user_id)

    # TODO: username must be unique, need to implement as another primary column
    def authenticate_user(self, username, password):
        print("TODO")
        