#!/usr/bin/python3
"""
Test suite for User Class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """
    test cases for the User class
    """
    my_instance = User()
    def test_instantiation(self):
        """
        test instantiation of User class
        """

        self.assertEqual(str(type(my_instance)), "<class 'models.user.User'>")
        self.assertIsInstance(my_instance, User)
        self.assertTrue(issubclass(type(my_instance), BaseModel))

    def test_attributes(self):
        """
        Testing attributes of User
        """
        test_attributes = storage.attributes()['User']
        for k, v in test_attributes.items():
            self.assertTrue(hasattr(my_instance, k))
            self.assertEqual(type(getattr(my_instance, k, None)), v)



if __name__ == "__main__":
    unittest.main()
