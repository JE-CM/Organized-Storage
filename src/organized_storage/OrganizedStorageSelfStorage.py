import os
import sys

# Add the directory containing the SqliteDatabase package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "/database/"))

from self_store_users import SelfStoreUserDatabase
from self_store_users import SelfStoreUnitDatabase

class OrganizedStorage:
    def __init__(self, db_dir='~/',
                 self_store_users_db_filename='organized_storage_self_store_users.db',
                 self_store_units_db_filename='organized_storage_self_store_units.db',
                 ):
        self.db_list = []
        # TODO: Each DB below needs to be adapted with custom organized_storage_table_columns to fit the
        #       use-case. The __init__ method of the OrganizedStorageDatabase method needs to be adapted
        #       to allow this.
        self.self_store_users_db = SelfStoreUserDatabase(db_dir, self_store_users_db_filename)
        self.self_store_units_db = SelfStoreUnitDatabase(db_dir, self_store_units_db_filename)
        self.db_list.extend([self.self_store_users_db,
                             self.self_store_units_db])

    def delete_all_dbs(self):
        for db in self.db_list:
            db.delete_db()

    def add_self_store_user(self, user_dict):
        return self.self_store_users_db.add_user(user_dict)

    def add_self_store_unit(self, unit_dict):
        return self.self_store_units_db.add_user(unit_dict)

    def add_authorized_users_to_unit(self, unit_id, user_id_list):
        for user_id in user_id_list:
            added_unit_to_user = self.self_store_users_db.add_authorized_user_to_unit([unit_id], user_id)
            if not added_unit_to_user:
                return added_unit_to_user
        added_user_to_unit = self.self_store_units_db.add_users_to_units(unit_id, user_id_list)
        return added_user_to_unit

    def add_units_to_user(self, unit_id_list, user_id):
        for unit_id in unit_id_list:
            added_user_to_unit = self.self_store_units_db.add_users_to_units(unit_id, [user_id])
            if not added_user_to_unit:
                return added_user_to_unit
        added_user_to_unit = self.self_store_users_db.add_authorized_user_to_unit(unit_id_list, user_id)
        return added_user_to_unit

    def remove_authorized_user_to_unit(self):
        # TODO
