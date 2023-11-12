#!/usr/bin/python3
"""
Test suite for Place Class
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    """
    test cases for the Place class
    """
    my_instance = Place()

    def test_instantiation(self):
        """
        test instantiation of Place class
        """

        self.assertEqual(str(type(my_instance)),
                         "<class 'models.place.Place'>")
        self.assertIsInstance(my_instance, Place)
        self.assertTrue(issubclass(type(my_instance), BaseModel))

    def test_attributes(self):
        """
        Testing attributes of Place
        """
        test_attributes = storage.attributes()['Place']
        for k, v in test_attributes.items():
            self.assertTrue(hasattr(my_instance, k))
            self.assertEqual(type(getattr(my_instance, k, None)), v)


if __name__ == "__main__":
    unittest.main()
