#!/usr/bin/python3
"""
class User that inherits from BaseModel

"""

#import required module
from base_model import BaseModel


class User(BaseModel):
    """
    User that inherit from BaseModel
    """
    email = ""
    password = ""
    firstname = ""
    lastname = ""
