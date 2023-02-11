#!/usr/bin/python3

"""
this module contain entry point of the NBNB console

"""

#import required module
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
