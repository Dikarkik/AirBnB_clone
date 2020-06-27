#!/usr/bin/python3
""" Console Module """
import cmd
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
        """ Creates a new instance, \
        saves it (to the JSON file) and prints the id\n """
        if line in storage.classes():
            new_obj = storage.classes()[line]()
            storage.save()
            print(new_obj.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an
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
        """ Deletes an instance based on the class name and id """
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
        """ Prints all string representation of all \
        instances based or not on the class name """
        if line == "":
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
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
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
        if len(tokens) < 4:
            print("** value missing **")
            return
        if tokens[3][0] == '"':
            value = " ".join(token for token in tokens[3:])
            value = value.split('"')[1]
        else:
            value = tokens[3]
        setattr(storage.all()[tokens[0] + "." + tokens[1]], tokens[2], value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
