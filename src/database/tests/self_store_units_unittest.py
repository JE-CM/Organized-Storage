import unittest
import sys
import os

# Add the directory containing the self_store_units package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Import the class to be tested
from self_store_units import SelfStoreUnitDatabase


class TestSelfStoreUnitDatabase(unittest.TestCase):
    def setUp(self):
        self.test_self_store_units_db = SelfStoreUnitDatabase('.','organized_storage_self_store_units_unittest.db')
    # SELF_STORE_AUTHORIZED_USER_LIST_NAME = "authorized_user_list"
    # SELF_STORE_UNITS_DB_COLUMNS = {
    #     "id": {
    #         "primary": True,
    #         "type": "INTEGER",
    #     },
    #     "number": {
    #         "type": "TEXT",
    #     },
    #     "facility_address": {
    #         "type": "TEXT",
    #     },
    #     # List of user IDs, separated by commas
    #     SELF_STORE_AUTHORIZED_USER_LIST_NAME: {
    #         "type": "TEXT",
    #     },

        self.test_self_store_unit = {
            "number": "131",
            "facility_address": "35 Best Drive, Great City, XY 01234",
            "authorized_user_list": "",            
        }
        self.test_user_edited = dict(self.test_self_store_unit)
        self.test_user_edited[SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME] = "1,2,4"

    def tearDown(self):
        self.test_self_store_units_db.delete_db()

    def test_setUp_and_tearDown(self):
        print("This test case doesn't test anything except the setUp and tearDown functions")

    def test_self_store_add_user(self):
        # TODO: Change add_user function to add_row
        result, id_added = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        self.assertEqual(result, True)
        self.assertEqual(id_added, 1)

    def test_self_store_remove_user(self):
        # TODO: Change add_user function to add_row
        _, id_added = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        key_to_search = "number"
        # TODO: Change remove_user function to remove_row
        result = self.test_self_store_units_db.remove_user(key_to_search, self.test_self_store_unit[key_to_search])
        self.assertEqual(result, True)

    def test_self_store_search_user(self):
        # TODO: Change add_user function to add_row
        self.test_self_store_units_db.add_user(self.test_self_store_unit)
        key_to_search = "number"
        # TODO: Change user_search function to row_search
        results = self.test_self_store_units_db.user_search(key_to_search, self.test_self_store_unit[key_to_search])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][key_to_search], self.test_self_store_unit[key_to_search])

    def test_update_user_by_id(self):
        _, id = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        update_result = self.test_self_store_units_db.update_user_by_id(id, self.test_user_edited)
        self.assertEqual(update_result, True)
        key_to_search = SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME
        results = self.test_self_store_units_db.user_search(key_to_search, self.test_self_store_unit[key_to_search])
        self.assertEqual(len(results), 0)
        results = self.test_self_store_units_db.user_search(key_to_search, self.test_user_edited[key_to_search])
        self.assertEqual(len(results), 1)

    def test_add_users_to_unit(self):
        _, id = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        before_results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), id)
        self.assertEqual(len(before_results), 1)
        self.assertEqual(before_results[0][SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME], "")
        new_user_list = ['1','4','5']
        add_unit_result = self.test_self_store_units_db.add_users_to_units(id, new_user_list)
        self.assertEqual(add_unit_result, True)
        results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME], ",".join(new_user_list))

    def test_add_units_to_user_that_does_not_exist(self):
        new_user_list = ['1','4','5']
        add_users_result = self.test_self_store_units_db.add_users_to_units("1", new_user_list)
        self.assertEqual(add_users_result, False)
        results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), "1")
        self.assertEqual(len(results), 0)

    def test_add_units_to_user_that_already_has_them(self):
        _, id = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        before_results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), id)
        self.assertEqual(len(before_results), 1)
        self.assertEqual(before_results[0][SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME], "")
        new_user_list = ['1','4','5']
        add_unit_result = self.test_self_store_units_db.add_users_to_units(id, new_user_list)
        self.assertEqual(add_unit_result, True)
        error_on_user_add_to_unit_add = False
        try:
            add_unit_result = self.test_self_store_units_db.add_units_to_user(id, new_unit_dict_list)
        except:
            error_on_user_add_to_unit_add = True
        self.assertEqual(error_on_user_add_to_unit_add, True)
        results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME], ",".join(new_user_list))

    def test_remove_users_from_unit(self):
        _, id = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        new_user_list = ['1','4','5']
        add_unit_result = self.test_self_store_units_db.add_users_to_units(id, new_user_list)
        self.assertEqual(add_unit_result, True)
        results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME], ",".join(new_user_list))
        remove_unit_result = self.test_self_store_units_db.remove_users_from_unit(id, ['1'])
        self.assertEqual(remove_unit_result, True)
        results = self.test_self_store_units_db.user_search(self.test_self_store_units_db.get_primary_key(), id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][SelfStoreUnitDatabase.SELF_STORE_AUTHORIZED_USER_LIST_NAME], '4,5')

    def test_user_authorized_to_access_unit(self):
        user_id_to_check = '2'
        authorized = self.test_self_store_units_db.user_authorized_to_access_unit('1',user_id_to_check)
        self.assertEqual(authorized, False)
        _, id = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        authorized = self.test_self_store_units_db.user_authorized_to_access_unit(id, user_id_to_check)
        self.assertEqual(authorized, False)
        new_user_list = [user_id_to_check,'4','5']
        add_user_result = self.test_self_store_units_db.add_users_to_units(id, new_user_list)
        self.assertEqual(add_user_result, True)
        authorized = self.test_self_store_units_db.user_authorized_to_access_unit(id, new_user_list[1])
        self.assertEqual(authorized, True)
        authorized = self.test_self_store_units_db.user_authorized_to_access_unit(id, user_id_to_check)
        self.assertEqual(authorized, True)
        authorized = self.test_self_store_units_db.user_authorized_to_access_unit(24, id)
        self.assertEqual(authorized, False)

    def test_get_self_store_unit_dict_of_user(self):
        _, id = self.test_self_store_units_db.add_user(self.test_self_store_unit)
        new_unit_dict_list = [
            {
                "id": "1",
                "price": "300",
            },
            {
                "id": "25",
                "price": "100",
            },
            {
                "id": "234",
                "price": "145",
            },
        ]
        add_unit_result = self.test_self_store_units_db.add_units_to_user(id, new_unit_dict_list)
        self.assertEqual(add_unit_result, True)
        unit_dict = self.test_self_store_units_db.get_self_store_unit_dict_of_user(id)
        for new_unit_dict in new_unit_dict_list:
            self.assertEqual(new_unit_dict['id'] in unit_dict, True)
            self.assertEqual(new_unit_dict['price'], unit_dict[new_unit_dict['id']])

if __name__ == "__main__":
    unittest.main()
