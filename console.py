#!/usr/bin/python3

"""
this module contain entry point of the NBNB console

"""

#import required module
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """A custom command interpreter for HBNB"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on EOF (Ctrl + D)"""
        print()
        return True

    def emptyline(self):
        """Do not execute anything when an empty line is entered"""
        pass

    def do_create(self, line):
        """ Create a new instance of BaseMode, Save it to the json file
            and print the id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return

        new_model = eval(class_name)()
        storage.new(new_model)
        storage.save()
        print(new_model.id)

    def do_show(self, line):
        """print a string representation of an instance base on name and id"""

        ag = line.split()
        if not ag:
            print("** class name is missing **")
            return
        class_name = ag[0]
        if class_name not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return
        my_id = ag[1]
        if not ag[1]:
            print(" **instance id missing** ")
            return
        instances = storage.all()
        key = ag[0] + '.' + ag[1]
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """delete an insrance base on name and id"""
        if line == "":
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in ["BaseModel", "User"]:
                if len(line) > 1:
                    instances = storage.all()
                    key = line[0] + '.' + line[1]
                    if key in instances:
                        del instances[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
           on the class name
        """
        if line == "":
            instances = storage.all()
            print([str(instances[key]) for key in instances])
        else:
            line = line.split()
            if line[0] in ['BaseModel', 'User']:
                instances = storage.all()
                print([str(instances[key]) for key in instances
                       if key.startswith(line[0] + '.')])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """pdates an instance based on the class name and id by adding or
           updating attribute
        """
        if line == "":
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in ['BaseModel', 'User']:
                if len(line) >= 3:
                    instances = storage.all()
                    key = line[0] + '.' + line[1]
                    if key in instances:
                        obj = instances[key]
                        if hasattr(obj, line[2]):
                            if len(line) >= 4:
                                value = line[3].strip('"')
                                type_of_attribute = type(getattr(obj, line[2]))
                                if type_of_attribute is float:
                                    value = float(value)
                                elif type_of_attribute is int:
                                    value = int(value)
                                setattr(obj, line[2], value)
                                obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
