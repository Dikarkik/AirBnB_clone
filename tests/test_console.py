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
    9.1. <class name>.all(): call 'do_all'.
    9.2. <class name>.count(): call 'count'.
    9.3. <class name>.show(<id>): call 'show'.
    9.4. <class name>.destroy(<id>): call 'destroy'.
    9.5. <class name>.update(<id>, <attribute name>, <attribute value>):
         call 'update'.
    9.6. <class name>.update(<id>, <dictionary representation>): call 'update'.

python3 -m unittest tests/test_console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """ unittests """

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
    0. emptyline(self)
    ------------------------------------------------------------
    """
    def test_emptyline(self):
        """ empty line + ENTER shouldn’t execute anything """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertTrue(f.getvalue() == "")

    """
    ------------------------------------------------------------
    1. do_EOF(self, line)
    ------------------------------------------------------------
    """
    def test_do_EOF(self):
        """ test if command EOF exit the program """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertTrue(f.getvalue() == "\n")

    """
    ------------------------------------------------------------
    2. do_quit(self, line)
    ------------------------------------------------------------
    """
    def test_do_quit(self):
        """ test if command 'quit' exit the program """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        print(f.getvalue())
        self.assertTrue(f.getvalue() == "")

    """
    ------------------------------------------------------------
    3. do_create(self, line)
    ------------------------------------------------------------
    """
    def test_do_create(self):
        """ test if command 'create <class name>' creates an instance
        with the correct class and prints the id """
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("create User")
        key = "User." + str(f.getvalue()).split("\n")[0]
        self.assertIsInstance(FileStorage._FileStorage__objects[key], User)

        """ test error message when <class name> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        """ test error message when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("create NotExistClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    """
    ------------------------------------------------------------
    4. do_show(self, line)
    ------------------------------------------------------------
    """
    def test_do_show(self):
        """ test if command 'show <class name> <id>' works """
        console = HBNBCommand()
        dictionary = {'__class__': "User",
                      'id': "1128",
                      'created_at': "2020-06-29T15:27:48.421135",
                      'updated_at': "2020-06-29T15:27:48.421148"}
        u = User(**dictionary)
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show User 1128")
        result = f.getvalue().split()
        self.assertEqual(result[0], "[User]")
        self.assertEqual(result[1], "(1128)")

        """ test error message when <class name> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        """ test error message when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show NotExistClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        """ test error message when <id> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show User")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        """ test error message when no instance found """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("show User 000")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    """
    ------------------------------------------------------------
    5. do_destroy(self, line)
    ------------------------------------------------------------
    """
    def test_do_destroy(self):
        """ test if command 'destroy <class name> <id>' works """
        dictionary = {'__class__': "User",
                      'id': "1128",
                      'created_at': "2020-06-29T15:27:48.421135",
                      'updated_at': "2020-06-29T15:27:48.421148"}
        u = User(**dictionary)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1128")
        self.assertFalse(FileStorage._FileStorage__objects.get("1128"))

        """ test error message when <class name> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        """ test error message when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NotExistClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        """ test error message when <id> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        """ test error message when no instance found """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 000")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    """
    ------------------------------------------------------------
    7. do_update(self, line)
    ------------------------------------------------------------
    """
    def test_do_update(self):
        u = User()
        """ test if the value of type str is correctly stored """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} string "text"'.format(u.id))
        self.assertTrue(u.string == "text")
        self.assertIsInstance(u.string, str)

        """ test if the value of type int is correctly stored """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} int 100'.format(u.id))
        self.assertTrue(u.int == 100)
        self.assertIsInstance(u.int, int)

        """ test if the value of type float is correctly stored """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} float 98.5'.format(u.id))
        self.assertTrue(u.float == 98.5)
        self.assertIsInstance(u.float, float)

        """ test if the value of type str is correctly stored
        (the value starts whith integers. ex: "98.5caraji")"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} fake 98.5caraji'.format(u.id))
        self.assertTrue(u.fake == "98.5caraji")
        self.assertIsInstance(u.fake, str)

        """ test if the values sended with **kwargs have the correct type """
        with patch('sys.stdout', new=StringIO()) as f:
            dic = {'first_name': "John", "age": 89}
            HBNBCommand().onecmd("User.update({}, {})".format(u.id, dic))
        self.assertTrue(u.first_name == "John")
        self.assertTrue(u.age == 89)
