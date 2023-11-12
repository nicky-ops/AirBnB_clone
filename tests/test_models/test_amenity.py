#!/usr/bin/python3
"""
Test suite for Amenity Class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class TestAmenity(unittest.TestCase):
    """
    test cases for the Amenity class
    """
    my_instance = Amenity()
    def test_instantiation(self):
        """
        test instantiation of Amenity class
        """

        self.assertEqual(str(type(my_instance)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(my_instance, Amenity)
        self.assertTrue(issubclass(type(my_instance), BaseModel))

    def test_attributes(self):
        """
        Testing attributes of Amenity
        """
        test_attributes = storage.attributes()['Amenity']
        for k, v in test_attributes.items():
            self.assertTrue(hasattr(my_instance, k))
            self.assertEqual(type(getattr(my_instance, k, None)), v)



if __name__ == "__main__":
    unittest.main()
