import bcrypt


class Authenticator:
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        return hashed_password

    @staticmethod
    def password_matches_hashed_password(password, hashed_password):
        # Verifying a password
        is_correct = bcrypt.checkpw(password, hashed_password)
        return is_correct


def unit_tests():
    test_basic_hash_and_check()


def test_basic_hash_and_check():
    password = b"fake_password"
    hashed_password = Authenticator.hash_password(password)
    assert Authenticator.password_matches_hashed_password(password, hashed_password)


def main():
    unit_tests()


main()
