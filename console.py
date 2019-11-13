#!/usr/bin/python3
""" Imports """
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_create(self, name):
        """Create a new instance"""
        if name == '':
            print("** class name missing **")
        elif name in HBNBCommand.classes:
            Class = HBNBCommand.classes.get(name)()
            Class.save()
            print(Class.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance"""
        if line:
            args = line.split(' ')
            if args[0] in HBNBCommand.classes:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    objs = storage.all()
                    obj = "{}.{}".format(args[0], args[1])
                    if obj in objs.keys():
                        storage.delete(args[0], args[1])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, name):
        """Update a instance based on the class name"""
        if name:
            pass
        else:
            print("** class doesn't exist **")

    def do_all(self, name):
        """Prints all instances"""
        objs = storage.all()
        if name in HBNBCommand.classes or name == "":
            print(objs[obj])
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints a instance based on the class name"""
        if line:
            args = line.split(' ')
            if args[0] in HBNBCommand.classes:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    objs = storage.all()
                    obj = "{}.{}".format(args[0], args[1])
                    if obj in objs.keys():
                        print(objs[obj])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
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
