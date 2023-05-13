#!/usr/bin/python3
""" Unittest module for the State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Tests cases for the State class """

    def __init__(self, *args, **kwargs):
        """ Initializes the object attributes """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Tests new name of the State class """
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ = "__main__"
    unittest.main()
