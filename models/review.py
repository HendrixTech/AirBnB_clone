#!/usr/bin/python3
"""This module creates a review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class attributes"""
    place_id = ""
    user_id = ""
    text = ""
