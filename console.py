#!/usr/bin/python3
""" Console Module """
import cmd
from models.engine.file_storage import FileStorage
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
    prompt = "(hbnb) "
    methods_lists = ['all', 'show', 'count', 'update', 'destroy']

    def emptyline(self):
        """ Do nothing """
        return

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line):
        """Creates a new instance, \
saves it (to the JSON file) and prints the id\n"""
        if line in storage.classes():
            new_obj = storage.classes()[line]()
            storage.save()
            print(new_obj.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an \
instance based on the class name and id\n"""
        if line == "":
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in storage.classes():
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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""
        if line == "":
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        id_obj = str(tokens[0] + "." + tokens[1])
        if id_obj not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[id_obj]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all \
instances based or not on the class name\n"""
        if not line or line == "":
            l = [str(value) for key, value in storage.all().items()]
        else:
            tokens = line.split(" ")
            if tokens[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            l = [str(value) for key, value in storage.all().items()
                 if type(value).__name__ == tokens[0]]
        print(l)

    def do_update(self, line):
        """Updates an instance based on the class name and id \
by adding or updating attribute (save the change into the JSON file).
Usage: update <class name> <id> <attribute name> "<attribute value>"\n"""
        if line == "":
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        id_obj = str(tokens[0] + "." + tokens[1])
        if id_obj not in storage.all():
            print("** no instance found **")
            return
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if '{' in tokens[2]:
            dic = json.loads(" ".join(elem for elem in tokens[2:]))
            for key, value in dic.items():
                setattr(storage.all()[tokens[0] + "." + tokens[1]], key, value)
                storage.all()[tokens[0] + "." + tokens[1]].save()
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        if tokens[3][0] == '"':
            value = " ".join(token for token in tokens[3:])
            value = value.split('"')[1]
        else:
            value = tokens[3]
        if '.' in value:
            try:
                value = float(value)
            except ValueError:
                pass
        else:
            try:
                value = int(value)
            except ValueError:
                pass
        setattr(storage.all()[tokens[0] + "." + tokens[1]], tokens[2], value)
        storage.all()[tokens[0] + "." + tokens[1]].save()

    def do_count(self, line):
        """Retrieve the number of instances of a class\n"""
        if not line or line == "":
            pass
        else:
            tokens = line.split(" ")
            l = [str(value) for key, value in storage.all().items()
                 if type(value).__name__ == tokens[0]]
        print(len(l))

    def default(self, line):
        """ this method process commands in python OOP notation
        - <class name>.all()
        - <class name>.count()
        - <class name>.show(<id>)
        - <class name>.destroy(<id>)
        - <class name>.update(<id>, <attribute name>, <attribute value>)
        - <class name>.update(<id>, <dictionary representation>)
        """
        if '.' in line and '(' in line and ')' in line:
            tokens = line.split(".")
            cl = tokens[0]
            cmd = tokens[1].split('(')[0]
            if cmd in HBNBCommand.methods_lists:
                args = tokens[1].split('(')[1].replace(')', "").split(", ")
                if cmd == 'update' and '{' in args[1]:
                    string = cmd + " " + cl + " " + args[0].replace('"', "") +\
                        " " + ", ".join(e for e in args[1:]).replace("'", '"')
                else:
                    string = cmd + " " + cl + " " + \
                        " ".join(elem.replace('"', "") for elem in args)
                self.onecmd(string)
                return
        print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
