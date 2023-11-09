#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module creates a class named Review
"""


class Review(BaseModel):
    """
    Class Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
