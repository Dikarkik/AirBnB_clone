#!/usr/bin/python3
""" Test Console Module """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ tests """

    def test_help(self):
        """ test command help """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        value = """\nDocumented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n\n"""
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        value = "EOF command to exit the program\n\n"
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        value = "Quit command to exit the program\n\n"
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        value = "Creates a new instance, \
saves it (to the JSON file) and prints the id\n\n"
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        value = "Prints the string representation of an \
instance based on the class name and id\n\n"
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        value = "Deletes an instance based on the class name and id\n\n"
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        value = """Prints all string representation of all \
instances based or not on the class name\n\n"""
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        value = """Updates an instance based on the class name and id \
by adding or updating attribute (save the change into the JSON file).
Usage: update <class name> <id> <attribute name> "<attribute value>"\n\n"""
        self.assertTrue(f.getvalue() == value)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        value = "Retrieve the number of instances of a class\n\n"
        self.assertTrue(f.getvalue() == value)
