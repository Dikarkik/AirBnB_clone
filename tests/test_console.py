#!/usr/bin/python3
""" Unittest for ``/console.py``

class HBNBCommand:
    0. emptyline(self)
    1. do_EOF(self, line)
    2. do_quit(self, line)
    3. do_create(self, line)
    4. do_show(self, line)
    --- <class name>.show(<id>)
    5. do_destroy(self, line)
    --- <class name>.destroy(<id>)
    6. do_all(self, line)
    --- <class name>.all()
    7. do_update(self, line)
    --- <class name>.update(<id>, <attribute name>, <attribute value>)
    --- <class name>.update(<id>, <dictionary representation>)
    8. do_count(self, line)
    --- <class name>.count()
    9. default(self, line)

python3 -m unittest tests/test_console.py
"""
import unittest
import json
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """ unittests """

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        storage.save()

    def classes(self):
        """ Method that return a dict of the classes """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        options = {'BaseModel': BaseModel,
                   'User': User,
                   'State': State,
                   'City': City,
                   'Amenity': Amenity,
                   'Place': Place,
                   'Review': Review}
        return options

    """
    ------------------------------------------------------------
    Tests to breack the console
    ------------------------------------------------------------
    """
    def test_unknown_sintax(self):
        """ test invalid commands """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("helppp")
        self.assertEqual(f.getvalue(), "*** Unknown syntax: helppp\n")

    def test_empty(self):
        """ test emplty """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), "")

    def test_space(self):
        """ test space """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" ")
        self.assertEqual(f.getvalue(), "")

    def test_tab(self):
        """ test tab """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\t")
        self.assertEqual(f.getvalue(), "")
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
        for className, Cls in self.classes().items():
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("create {}".format(className))
            key = "{}.".format(className) + str(f.getvalue()).split("\n")[0]
            self.assertIsInstance(FileStorage._FileStorage__objects[key], Cls)

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
        """ test if command 'show <class name> <id>'
        and '<class name>.show(<id>)' works """
        console = HBNBCommand()
        for className, Cls in self.classes().items():
            u = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("show {} {}".format(className, u.id))
            result = f.getvalue().split()
            self.assertEqual(result[0], "[{}]".format(className))
            self.assertEqual(result[1], "({})".format(u.id))
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd('{}.show("{}")'.format(className, u.id))
            result = f.getvalue().split()
            self.assertEqual(result[0], "[{}]".format(className))
            self.assertEqual(result[1], "({})".format(u.id))

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
        """ test if command 'destroy <class name> <id>'
        and '<class name>.destroy(<id>)' works """
        for className, Cls in self.classes().items():
            u = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {} {}".format(className, u.id))
            self.assertFalse(FileStorage._FileStorage__objects.get(u.id))
            u = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.destroy({})".format(className, u.id))
            self.assertFalse(FileStorage._FileStorage__objects.get(u.id))

        """ test error message when <class name> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        """ test error message when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NotExistClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("NotExistClass.destroy(1128)")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        """ test error message when <id> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy()')
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        """ test error message when no instance found """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 000")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy("000")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    """
    ------------------------------------------------------------
    6. do_all(self, line)
    ------------------------------------------------------------
    """
    def test_do_all(self):
        """ test if command 'all <class name>'
        and '<class name>.all()' works """
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("all")
        self.assertEqual(len(json.loads(f.getvalue())), 0)
        u = self.classes()['User']()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("all")
        self.assertEqual(len(json.loads(f.getvalue())), 1)

        self.setUp()
        for className, Cls in self.classes().items():
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("all {}".format(className))
            self.assertEqual(len(json.loads(f.getvalue())), 0)
            u = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("all {}".format(className))
            self.assertEqual(len(json.loads(f.getvalue())), 1)

        """ test error message when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("all NotExistClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    """
    ------------------------------------------------------------
    7. do_update(self, line)
    ------------------------------------------------------------
    """
    def test_do_update(self):
        """ test command
        'update <class name> <id> <attribute name> <attribute value>'
        and '<class name>.update(<id>, <attribute name>, <attribute value>)'
        and <class name>.update(<id>, <dictionary representation>) """

        for className, Cls in self.classes().items():
            u = Cls()

            """ 'update <class name> <id> <attr name> <attr value>' """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('update {} {} string "text"'
                                     .format(className, u.id))
            self.assertTrue(u.string == "text")
            self.assertIsInstance(u.string, str)

            """ '<class name>.update(<id>, <attr name>, <attr value>)' """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.update("{}", string, "text")'
                                     .format(className, u.id))
            self.assertTrue(u.string == "text")
            self.assertIsInstance(u.string, str)

            """ <class name>.update(<id>, <dictionary representation>) """
            dic = {'first_name': "John", "age": 89}
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.update("{}", {})'
                                     .format(className, u.id, dic))
            self.assertTrue(u.first_name == "John")
            self.assertTrue(u.age == 89)

            """ test if the value of type int is correctly stored """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('update {} {} int 100'
                                     .format(className, u.id))
            self.assertTrue(u.int == 100)
            self.assertIsInstance(u.int, int)

            """ test if the value of type float is correctly stored """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('update {} {} float 98.5'
                                     .format(className, u.id))
            self.assertTrue(u.float == 98.5)
            self.assertIsInstance(u.float, float)

            """ test if the value of type str is correctly stored
            (the value starts whith integers. ex: "98.5caraji")"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('update {} {} fake 98.5caraji'
                                     .format(className, u.id))
            self.assertTrue(u.fake == "98.5caraji")
            self.assertIsInstance(u.fake, str)

            """ test if the values sended with kwargs have the correct type """
            with patch('sys.stdout', new=StringIO()) as f:
                dic = {'first_name': "John", "age": 89}
                HBNBCommand().onecmd("{}.update({}, {})"
                                     .format(className, u.id, dic))
            self.assertTrue(u.first_name == "John")
            self.assertTrue(u.age == 89)

        """ test error message when <class name> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        """ test error message when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NotExistClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        """ test error message when <id> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        """ test error message when no instance found """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 000")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        """ test error message when <attribute name> is missing """
        user = self.classes()['User']()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {}".format(user.id))
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

        """ test error message when <value> is missing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} attribute".format(user.id))
        self.assertEqual(f.getvalue(), "** value missing **\n")

    """
    ------------------------------------------------------------
    8. do_count(self, line)
    ------------------------------------------------------------
    """
    def test_do_count(self):
        """ test if command 'count <class name>' and '<class name>.count()'
         prints the number of instances of a class """
        console = HBNBCommand()
        for className, Cls in self.classes().items():
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("count {}".format(className))
                self.assertEqual(f.getvalue(), '0\n')
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("{}.count()".format(className))
                self.assertEqual(f.getvalue(), '0\n')
            i1 = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("count {}".format(className))
                self.assertEqual(f.getvalue(), '1\n')
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("{}.count()".format(className))
                self.assertEqual(f.getvalue(), '1\n')
            i2 = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("count {}".format(className))
                self.assertEqual(f.getvalue(), '2\n')
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("{}.count()".format(className))
                self.assertEqual(f.getvalue(), '2\n')
            i3 = Cls()
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("count {}".format(className))
                self.assertEqual(f.getvalue(), '3\n')
            with patch('sys.stdout', new=StringIO()) as f:
                console.onecmd("{}.count()".format(className))
                self.assertEqual(f.getvalue(), '3\n')

        """ test when <class name> doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd("count NotExistClass")
        self.assertEqual(f.getvalue(), "0\n")
