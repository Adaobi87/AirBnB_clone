#!/usr/bin/python3
""" Unittest module for the Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Tests cases for the Review class """

    def __init__(self, *args, **kwargs):
        """ Initializes the object attributes of the Review class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Tests the functionality of the place id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Tests the functionality of the user id  """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Verifies the behaviour of the text attribute of the object place"""
        new = self.value()
        self.assertEqual(type(new.text), str)

if __name__ = "__main__"
    unittest.main()
