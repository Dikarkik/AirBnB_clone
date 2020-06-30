#!/usr/bin/python3
""" Unittest for ``/console.py``

class HBNBCommand:
    0. emptyline(self)
    1. do_EOF(self, line)
    2. do_quit(self, line)
    3. do_create(self, line)
    4. do_show(self, line)
    5. do_destroy(self, line)
    6. do_all(self, line)
    7. do_update(self, line)
    8. do_count(self, line)
    9. default(self, line)

python3 -m unittest tests/test_console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """ tests """

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        storage.save()

    """
    ------------------------------------------------------------
    Tests for 'help' (this is in the 'cmd' module)
    ------------------------------------------------------------
    """
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

    """
    ------------------------------------------------------------
    7. do_update(self, line)
    ------------------------------------------------------------
    """
    def test_do_update(self):
        u = User()
        """ test str """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} string "text"'.format(u.id))
        self.assertTrue(u.string == "text")
        self.assertIsInstance(u.string, str)

        """ test int """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} int 100'.format(u.id))
        self.assertTrue(u.int == 100)
        self.assertIsInstance(u.int, int)

        """ test float """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} float 98.5'.format(u.id))
        self.assertTrue(u.float == 98.5)
        self.assertIsInstance(u.float, float)

        """ test str """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} fake 98.5caraji'.format(u.id))
        self.assertTrue(u.fake == "98.5caraji")
        self.assertIsInstance(u.fake, str)

        with patch('sys.stdout', new=StringIO()) as f:
            dic = {'first_name': "John", "age": 89}
            HBNBCommand().onecmd("User.update({}, {})".format(u.id, dic))
        self.assertTrue(u.first_name == "John")
        self.assertTrue(u.age == 89)
