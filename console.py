#!/usr/bin/python3
""" Imports """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program Ctrl+D
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """emptyline do not execute before command"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
