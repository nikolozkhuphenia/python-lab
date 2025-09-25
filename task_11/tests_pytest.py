# #5 pytest2
#
# შექმენით ფუნქცია რომელიც ამოწმებს მომხმარებლის ლოგინს და პაროლს dictionary-დან
# pytest-ში გამოიყენეთ raises შეცდომის დასატესტად
#
# ნიმუში: raise ValueError
#
import pytest

import pytest

# User database
users = {
    "admin": "123",
    "user": "pass",
    "user1": "pass1",
    "user2": "pass2"
}


def login(username, password):
    if username not in users:
        raise ValueError("User not found")

    if users[username] != password:
        raise ValueError("Wrong password")

    return True

def test_successful_login():
    assert login("admin", "123") == True


def test_user_not_found():
    with pytest.raises(ValueError, match="User not found"):
        login("fake_user", "123")


def test_wrong_password():
    with pytest.raises(ValueError, match="Wrong password"):
        login("admin", "wrong_pass")
#
# #6 pytest3
#
# დაწერეთ ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი სწორი email (ანუ შეიცავს @ და . სიმბოლოებს)
# pytest-ით გააკეთეთ ტესტები parametrization-ის გამოყენებით
#
# ნიმუში: @pytest.mark.parametrize



import pytest

def is_valid_email(email):
    return '@' in email and '.' in email


@pytest.mark.parametrize("email, expected", [
    ("user@gmail.com", True),
    ("admin@yahoo.com", True),
    ("test@site.ge", True),
    ("nogmail.com", False),
    ("no@gmail", False),
    ("nothing", False),
])
def test_email_validation(email, expected):
    assert is_valid_email(email) == expected