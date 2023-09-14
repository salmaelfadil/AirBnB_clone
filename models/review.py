#!/usr/bin/python3
"""
reviews model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    definig review class
    """
    place_id = ""
    user_id = ""
    text = ""
