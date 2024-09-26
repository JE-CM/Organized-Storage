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
        self.test_self_store_users_db.add_user(self.test_self_store_user)
    
    def test_self_store_remove_user(self):
        self.test_self_store_users_db.add_user(self.test_self_store_user)
        key_to_search = "name"
        self.test_self_store_users_db.remove_user(key_to_search, self.test_self_store_user[key_to_search])
        
    def test_self_store_search_user(self):
        self.test_self_store_users_db.add_user(self.test_self_store_user)
        key_to_search = "name"
        results = self.test_self_store_users_db.user_search(key_to_search, self.test_self_store_user[key_to_search])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][key_to_search], self.test_self_store_user[key_to_search])

    # def test_user_search(self):
    #     key_to_search = "name"
    #     self.test_db.add_user(self.test_user)
    #     results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
    #     self.assertEqual(len(results), 1)
    #     self.assertEqual(results[0]['id'], 1)
    #     self.assertEqual(results[0][key_to_search], self.test_user[key_to_search])

    # def test_remove_user(self):
    #     self.test_db.add_user(self.test_user)
    #     key_to_search = "name"
    #     results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
    #     self.assertEqual(len(results), 1)
    #     removed_user = self.test_db.remove_user(key_to_search, self.test_user[key_to_search])
    #     self.assertEqual(removed_user, True)
    #     after_remove_results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
    #     self.assertEqual(len(after_remove_results), 0)

    # def test_user_search_on_nonexistent_user(self):
    #     key_to_search = "name"
    #     results= self.test_db.user_search(key_to_search, self.test_user[key_to_search])
    #     self.assertEqual(len(results), 0)

    def test_update_user_by_id(self):
        _, id = self.test_self_store_users_db.add_user(self.test_self_store_user)
        update_result = self.test_self_store_users_db.update_user_by_id(id, self.test_user_edited)
        self.assertEqual(update_result, True)
        key_to_search = SelfStoreUserDatabase.SELF_STORE_UNIT_LIST_NAME 
        results = self.test_self_store_users_db.user_search(key_to_search, self.test_self_store_user[key_to_search])
        self.assertEqual(len(results), 0)
        results = self.test_self_store_users_db.user_search(key_to_search, self.test_user_edited[key_to_search])
        self.assertEqual(len(results), 1)
        
if __name__ == "__main__":
    unittest.main()
