import unittest
import sys
import os

# Add the directory containing the self_store_users package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Import the class to be tested
from self_store_users import SelfStoreUserDatabase


class TestSelfStoreUserDatabase(unittest.TestCase):
    def setUp(self):
        self.test_self_store_users_db = SelfStoreUserDatabase('.','organized_storage_self_store_users_unittest.db')
        self.test_self_store_user = {
            "name": "Alice",
            "address": "123 Good Rd, Greattown, Best Country",
            "phone_number": "12345678910",
            "email_address": "myemail@domain.that.does.not.exist.com",
            "hashed_password": "TODO",
            "password_salt": "TODO",
            "storage_unit_list": "",
            "storage_unit_prices": "",            
        }
        self.test_user_edited = dict(self.test_self_store_user)
        self.test_user_edited[SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME] = "15,20,21"

    def tearDown(self):
        self.test_self_store_users_db.delete_db()

    def test_setUp_and_tearDown(self):
        print("This test case doesn't test anything except the setUp and tearDown functions")

    def test_self_store_add_user(self):
        result, id_added = self.test_self_store_users_db.add_user(self.test_self_store_user)
        self.assertEqual(result, True)
        self.assertEqual(id_added, 1)

    def test_self_store_remove_user(self):
        self.test_self_store_users_db.add_user(self.test_self_store_user)
        key_to_search = "name"
        result = self.test_self_store_users_db.remove_user(key_to_search, self.test_self_store_user[key_to_search])
        self.assertEqual(result, True)

    def test_self_store_search_user(self):
        self.test_self_store_users_db.add_user(self.test_self_store_user)
        key_to_search = "name"
        results = self.test_self_store_users_db.user_search(key_to_search, self.test_self_store_user[key_to_search])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][key_to_search], self.test_self_store_user[key_to_search])

    def test_update_user_by_id(self):
        _, id = self.test_self_store_users_db.add_user(self.test_self_store_user)
        update_result = self.test_self_store_users_db.update_user_by_id(id, self.test_user_edited)
        self.assertEqual(update_result, True)
        key_to_search = SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME 
        results = self.test_self_store_users_db.user_search(key_to_search, self.test_self_store_user[key_to_search])
        self.assertEqual(len(results), 0)
        results = self.test_self_store_users_db.user_search(key_to_search, self.test_user_edited[key_to_search])
        self.assertEqual(len(results), 1)

    def test_add_units_to_user(self):
        _, id = self.test_self_store_users_db.add_user(self.test_self_store_user)
        before_results = self.test_self_store_users_db.user_search(self.test_self_store_users_db.get_primary_key(), id)
        self.assertEqual(len(before_results), 1)
        self.assertEqual(before_results[0][SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME], "")
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
        add_unit_result = self.test_self_store_users_db.add_units_to_user(id, new_unit_dict_list)
        self.assertEqual(add_unit_result, True)
        results = self.test_self_store_users_db.user_search(self.test_self_store_users_db.get_primary_key(), id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME], ",".join([n['id'] for n in new_unit_dict_list]))
        self.assertEqual(results[0][SelfStoreUserDatabase.SELF_STORE_UNIT_PRICE_LIST_NAME], ",".join([n['price'] for n in new_unit_dict_list]))

    def test_add_units_to_user_that_does_not_exist(self):
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
        add_unit_result = self.test_self_store_users_db.add_units_to_user(id, new_unit_dict_list)
        self.assertEqual(add_unit_result, False)
        results = self.test_self_store_users_db.user_search(self.test_self_store_users_db.get_primary_key(), id)
        self.assertEqual(len(results), 0)

    def test_add_units_to_user_that_already_has_them(self):
        _, id = self.test_self_store_users_db.add_user(self.test_self_store_user)
        before_results = self.test_self_store_users_db.user_search(self.test_self_store_users_db.get_primary_key(), id)
        self.assertEqual(len(before_results), 1)
        self.assertEqual(before_results[0][SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME], "")
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
        add_unit_result = self.test_self_store_users_db.add_units_to_user(id, new_unit_dict_list)
        self.assertEqual(add_unit_result, True)
        error_on_unit_add = False
        try:
            add_unit_result = self.test_self_store_users_db.add_units_to_user(id, new_unit_dict_list)
        except:
            error_on_unit_add = True
        self.assertEqual(error_on_unit_add, True)
        results = self.test_self_store_users_db.user_search(self.test_self_store_users_db.get_primary_key(), id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME], ",".join([n['id'] for n in new_unit_dict_list]))
        self.assertEqual(results[0][SelfStoreUserDatabase.SELF_STORE_UNIT_PRICE_LIST_NAME], ",".join([n['price'] for n in new_unit_dict_list]))

    def test_user_authorized_to_access_unit(self):
        _, id = self.test_self_store_users_db.add_user(self.test_self_store_user)
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
        add_unit_result = self.test_self_store_users_db.add_units_to_user(id, new_unit_dict_list)
        self.assertEqual(add_unit_result, True)
        authorized = self.test_self_store_users_db.user_authorized_to_access_unit(new_unit_dict_list[1]['id'], id)
        self.assertEqual(authorized, True)
        authorized = self.test_self_store_users_db.user_authorized_to_access_unit(24, id)
        self.assertEqual(authorized, False)

    # TODO:
    # def test_check_user_auth

if __name__ == "__main__":
    unittest.main()
