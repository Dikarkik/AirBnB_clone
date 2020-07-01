#!/usr/bin/env python3
""" Unittest for ``/models/engine/file_storage.py``

class FileStorage:
    0. classes(self)
    1. all(self)
    2. new(self, obj)
    3. save(self)
    4. reload(self)

python3 -m unittest tests/test_models/test_engine/test_file_storage.py
"""
import unittest
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ unittests """

    def setUp(self):
        """ resets __objects dictionary """
        FileStorage._FileStorage__objects = {}
        storage.save()

    """
    ------------------------------------------------------------
    0. classes(self)
    ------------------------------------------------------------
    """
    def test_classes(self):
        """ test if 'classes' returns a dict with the classes """
        dictionary = {'BaseModel': BaseModel,
                      'User': User,
                      'State': State,
                      'City': City,
                      'Amenity': Amenity,
                      'Place': Place,
                      'Review': Review}
        self.assertEqual(storage.classes(), dictionary)

    """
    ------------------------------------------------------------
    1. all(self)
    ------------------------------------------------------------
    """
    def test_all(self):
        """ test if 'all' returns the content of __objects """
        FileStorage._FileStorage__objects = {'key': "object"}
        self.assertEqual(storage.all(), {'key': "object"})

    """
    ------------------------------------------------------------
    2. new(self, obj)
    ------------------------------------------------------------
    """
    def test_new(self):
        """ test if 'new' adds an object in __objects """
        u = User()
        storage.new(u)
        self.assertTrue(
            FileStorage._FileStorage__objects[type(u).__name__ + "." + u.id])

    """
    ------------------------------------------------------------
    3. save(self)
    ------------------------------------------------------------
    """
    def test_save(self):
        """ test if 'save' actually save the data in file.json """
        u = User()
        storage.new(u)
        storage.save()
        try:
            with open(FileStorage._FileStorage__file_path,
                      'r', encoding='utf-8') as file:
                objs_dict = json.load(file)
        except:
            raise ValueError
        key = type(u).__name__ + "." + u.id
        self.assertTrue(key in objs_dict)

    """
    ------------------------------------------------------------
    4. reload(self)
    ------------------------------------------------------------
    """
    def test_reload(self):
        """ test if 'reload' reads 'file.json' and fill __objects """
        u = User()
        storage.new(u)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = type(u).__name__ + "." + u.id
        self.assertTrue(key in FileStorage._FileStorage__objects)
