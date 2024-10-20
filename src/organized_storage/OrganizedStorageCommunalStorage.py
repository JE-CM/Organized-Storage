import os
import sys

# Add the directory containing the SqliteDatabase package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "/database/"))

from OrganizedStorageDatabase import OrganizedStorageDatabase
from self_store_users import SelfStoreUserDatabase

class OrganizedStorage:
    def __init__(self, db_dir='~/',
                 self_store_users_db_filename='organized_storage_self_store_users.db',
                 self_store_units_db_filename='organized_storage_self_store_units.db',
                 communal_store_users_db_filename='organized_storage_communal_store_users.db',
                 communal_store_items_db_filename='organized_storage_communal_store_items.db',
                 ):
        self.db_list = []
        # TODO: Each DB below needs to be adapted with custom organized_storage_table_columns to fit the
        #       use-case. The __init__ method of the OrganizedStorageDatabase method needs to be adapted
        #       to allow this.
        self.self_store_users_db = SelfStoreUserDatabase(db_dir, self_store_users_db_filename)
        self.self_store_units_db = OrganizedStorageDatabase(db_dir, self_store_units_db_filename)
        self.communal_store_users_db = OrganizedStorageDatabase(db_dir, communal_store_users_db_filename)
        self.communal_store_items_db = OrganizedStorageDatabase(db_dir, communal_store_items_db_filename)
        self.db_list.extend([self.self_store_users_db,
                             self.self_store_units_db,
                             self.communal_store_users_db,
                             self.communal_store_items_db])

    def delete_all_dbs(self):
        for db in self.db_list:
            db.delete_db()