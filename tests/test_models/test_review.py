#!/usr/bin/python3
"""
Test suite for Review Class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """
    test cases for the Review class
    """
    my_instance = Review()

    def test_instantiation(self):
        """
        test instantiation of Review class
        """

        self.assertEqual(str(type(my_instance)),
                         "<class 'models.review.Review'>")
        self.assertIsInstance(my_instance, Amenity)
        self.assertTrue(issubclass(type(my_instance), BaseModel))

    def test_attributes(self):
        """
        Testing attributes of Review
        """
        test_attributes = storage.attributes()['Review']
        for k, v in test_attributes.items():
            self.assertTrue(hasattr(my_instance, k))
            self.assertEqual(type(getattr(my_instance, k, None)), v)


if __name__ == "__main__":
    unittest.main()
