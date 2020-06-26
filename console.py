#!/usr/bin/python3
""" Console Module """
import cmd


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
        'Quit command to exit the program\n'
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
