import unittest
import sys
import os

# Add the directory containing the Authentication package to the system path
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Import the class to be tested
from auth import Authenticator


class TestAuthenticator(unittest.TestCase):
    # def setUp(self):
    #     Authenticator = Authenticator()

    # def tearDown(self):
    #     del Authenticator

    def test_password_matches_hashed_password(self):
        password = b"fake_password"
        hashed_password = Authenticator.hash_password(password)
        self.assertTrue(
            Authenticator.password_matches_hashed_password(password, hashed_password)
        )

    def test_hash_password(self):
        password = b"fake_password"
        hashed_password = Authenticator.hash_password(password)
        self.assertNotEqual(password, hashed_password)


if __name__ == "__main__":
    unittest.main()
