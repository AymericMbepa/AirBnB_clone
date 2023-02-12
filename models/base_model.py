#!/usr/bin/python3
"""
defines all common attributes/methods for other classes

"""

#import required module
import uuid
import datetime
from models import storage


class BaseModel:
    """
    define all common attribute methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        init method for BaseModel class

        Attribute:
           id: string- assign with an uuid when an instance is created
           create_at: date_time- assign with the current date_time when
           an instance
                   is created
           Updated_at: date_time- assign whit the current date_time when an
                    instance is created and it will be updated everytime you
                    change your oblect
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """
        str method for BaseModel class

        """
        return str(([self.__class__.__name__], (self.id), (self.__dict__)))

    def save(self):
        """
        update the publis instance attribute update_at with the current
        datetime

        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values of __dict__ of
        the instance

        """
        return {**self.__dict__, 'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()}
