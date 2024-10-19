import unittest
import sys
import os

# Add the directory containing the OrganizedStorageDatabase package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Import the class to be tested
from OrganizedStorageDatabase import OrganizedStorageDatabase


class TestOrganizedStorageDatabase(unittest.TestCase):
    def setUp(self):
        self.test_db = OrganizedStorageDatabase('.','organized_storage_unittest.db')
        self.test_user = {
            "name": 'Alice',
            "address": '30 Giovanni Ln, Atlantis, 12345',
            "hashed_password": 'TODO_HASHED_PASSWORD',
            "password_salt": 'TODO_PASSWORD_SALT',
            "square_meters_used": 8.5,
        }
        self.test_user_edited = dict(self.test_user)
        self.test_user_edited["name"] = "Bob"

    def tearDown(self):
        self.test_db.delete_db()

    def test_setUp_and_tearDown(self):
        print("This test case doesn't test anything except the setUp and tearDown functions")

    def test_add_user(self):
        add_result, id = self.test_db.add_user(self.test_user)
        self.assertEqual(add_result, True)
        self.assertEqual(id, 1)

    def test_user_search(self):
        key_to_search = "name"
        self.test_db.add_user(self.test_user)
        results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['id'], 1)
        self.assertEqual(results[0][key_to_search], self.test_user[key_to_search])

    def test_remove_user(self):
        self.test_db.add_user(self.test_user)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 1)
        removed_user = self.test_db.remove_user(key_to_search, self.test_user[key_to_search])
        self.assertEqual(removed_user, True)
        after_remove_results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(after_remove_results), 0)

    def test_user_search_on_nonexistent_user(self):
        key_to_search = "name"
        results= self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 0)

    def test_update_user_by_id(self):
        _, id = self.test_db.add_user(self.test_user)
        update_result = self.test_db.update_user_by_id(id, self.test_user_edited)
        self.assertEqual(update_result, True)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 0)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user_edited[key_to_search])
        self.assertEqual(len(results), 1)

    def test_search_user_not_exist(self):
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 0)

    def test_update_user_not_exist(self):
        update_result = self.test_db.update_user_by_id(id, self.test_user)
        self.assertEqual(update_result, False)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user_edited[key_to_search])
        self.assertEqual(len(results), 0)

    def test_remove_user_not_exist(self):
        removed_user = self.test_db.remove_user(key_to_search, self.test_user[key_to_search])
        self.assertEqual(removed_user, False)

    def test_double_remove_user(self):
        self.test_db.add_user(self.test_user)
        key_to_search = "name"
        removed_user = self.test_db.remove_user(key_to_search, self.test_user[key_to_search])
        self.assertEqual(removed_user, True)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 0)
        removed_user = self.test_db.remove_user(key_to_search, self.test_user[key_to_search])
        self.assertEqual(removed_user, False)
        after_remove_results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(after_remove_results), 0)
        
if __name__ == "__main__":
    unittest.main()
