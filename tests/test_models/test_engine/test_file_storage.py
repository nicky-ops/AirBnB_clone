
#!/usr/bin/python3

""" Unittest module for the FileStorage class """
import unittest
import json
import os
from models import storage


class TestFileStorage(unittest.TestCase):
    """"Test Cases for the FileStorage class"""

    def test_instantiation(self):
        """
        Tests intantiation of storage class.
        """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """
        Test initialization with no arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        message = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)
