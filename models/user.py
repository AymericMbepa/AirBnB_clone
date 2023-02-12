#!/usr/bin/python3
"""
class User that inherits from BaseModel

"""

#import required module
from models.base_model import BaseModel


class User(BaseModel):
    """
    User that inherit from BaseModel
    """
    email = ""
    password = ""
    firstname = ""
    lastname = ""

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
