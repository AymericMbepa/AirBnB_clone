#!/usr/bin/python3

"""
this module provide a class that serializes instances to a JSON file
and deserializes JSON file to instances

"""
#import the required module
import json
import os


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
        instances

    Attributes:
        __file_path: string
        __objects: dictionnary

    Methods:
        all(self): returns the dictionary
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionnary"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __object the obj with the key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serialize __objects to the json file"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """deserializes the json file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
