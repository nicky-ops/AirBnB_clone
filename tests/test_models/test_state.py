#!/usr/bin/python3
"""
Test suite for State Class
"""

import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestState(unittest.TestCase):
    """
    test cases for the State class
    """
    my_instance = State()

    def test_instantiation(self):
        """
        test instantiation of State class
        """

        self.assertEqual(str(type(my_instance)),
                         "<class 'models.state.State'>")
        self.assertIsInstance(my_instance, State)
        self.assertTrue(issubclass(type(my_instance), BaseModel))

    def test_attributes(self):
        """
        Testing attributes of State
        """
        test_attributes = storage.attributes()['State']
        for k, v in test_attributes.items():
            self.assertTrue(hasattr(my_instance, k))
            self.assertEqual(type(getattr(my_instance, k, None)), v)


if __name__ == "__main__":
    unittest.main()
