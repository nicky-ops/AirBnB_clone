#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module creates a class named User
"""


class User(BaseModel):
    """
    Class user that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
