#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
    prompt = "(hbnb) "
    file = None

    def emptyline(self):
        return

    def do_EOF(self, line):
        'EOF command to exit the program\n'
        return True

    def do_quit(self, line):
        """ Quit command to exit the program\n """
        return True

    def do_create(self, line):
        """ Creates a new instance of BaseModel, \
        saves it (to the JSON file) and prints the id\n """
        if line == 'BaseModel':
            new_obj = BaseModel()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an \
        instance based on the class name and id\n"""
        classes = ['BaseModel']
        if line == "":
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        id_obj = str(tokens[0] + "." + tokens[1])
        if id_obj not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[id_obj])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
