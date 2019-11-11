#!/usr/bin/python3
""" Imports """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    prompt = "(hbnb) "

    def do_create(self, name):
        """Create a new instance"""
        if name == 'BaseModel':
            self.my_model=BaseModel()
            print("{}".format(self.my_model))
        else:
            print("** class name missing **")

    def do_destroy(self, name):
        """Deletes an instance"""
        if name:
            pass
        else:
            print("** class name missing **")

    def do_update(selfi, name):
        """Update a instance based on the class name"""
        if name:
            pass
        else:
            print("** class doesn't exist **")

    def do_all(self, name):
        """Prints all instances"""
        if name:
            pass
        else:
            print("** class doesn't exist **")

    def do_show(self, name):
        """Prints a instance based on the class name"""
        if name:
            pass
        else:
            print("** class name missing **")

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program Ctrl+D
        """
        return True

    def emptyline(self):
        """emptyline do not execute before command"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
