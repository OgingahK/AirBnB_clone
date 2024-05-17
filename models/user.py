#!/usr/bin/python3
"""A module that creates a user class"""

from models.base_models import BaseModel


class User(BaseModel):
    """A class that manages user objects"""


    email = ""
    password = ""
    first_name = ""
    last_name = ""
