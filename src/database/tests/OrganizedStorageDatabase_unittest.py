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
        # TODO: remove_user does not return anything meaningful yet because the SqliteDatabase.execute_query
        #       function does not return anything that a DELETE query would use for output, such as cursor.rowcount
        #       . We should convert SqliteDatabase.execute_query to return a dict with all possible values
        _, _ = self.test_db.remove_user(key_to_search, self.test_user[key_to_search])
        after_remove_results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(after_remove_results), 0)

    def test_user_search_on_nonexistent_user(self):
        key_to_search = "name"
        results= self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 0)

    def test_update_user_by_id(self):
        _, id = self.test_db.add_user(self.test_user)
        update_result, id = self.test_db.update_user_by_id(id, self.test_user_edited)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user[key_to_search])
        self.assertEqual(len(results), 0)
        key_to_search = "name"
        results = self.test_db.user_search(key_to_search, self.test_user_edited[key_to_search])
        self.assertEqual(len(results), 1)
        
if __name__ == "__main__":
    unittest.main()
