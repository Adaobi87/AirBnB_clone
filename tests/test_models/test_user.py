#!/usr/bin/python3
""" Unittest module for the User class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Tests cases for the User class"""

    def __init__(self, *args, **kwargs):
        """ Initializing the object attribute """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Tests tge first name of the User"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Tests the last name of the User """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Tests the email of the User"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Tests the password of the User """
        new = self.value()
        self.assertEqual(type(new.password), str)

if __name__ = "__main__"
    unittest.main()
