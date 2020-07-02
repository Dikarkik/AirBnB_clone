#!/usr/bin/env python3
""" Unittest for ``/models/base_model.py``

class FileStorage:
    0. __init__(self, *args, **kwargs)
    1. __str__(self)
    2. save(self)
    3. to_dict(self)

python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import json
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs)
    ------------------------------------------------------------
    """
    def test_init(self):
        """ test constructor: defalt, with **kwargs (*args won’t be used) """
        b = BaseModel()
        self.assertTrue('id' in b.__dict__)
        self.assertTrue('created_at' in b.__dict__)
        self.assertTrue('updated_at' in b.__dict__)

        b2 = BaseModel(**{'__class__': "SomeClass",
                          'id': "f7f99",
                          'created_at': "2020-06-29T15:27:48.421135",
                          'updated_at': "2020-06-29T15:27:48.421148",
                          'name': "Diana Caro"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in b2.__dict__)
        """ must create the keys """
        self.assertTrue('id' in b2.__dict__)
        self.assertTrue('created_at' in b2.__dict__)
        self.assertTrue('updated_at' in b2.__dict__)
        self.assertTrue('name' in b2.__dict__)

    """
    ------------------------------------------------------------
    1. __str__(self)
    ------------------------------------------------------------
    """
    def test_str(self):
        """ test the string representation of a 'BaseModel' instance,
        must be [<class name>] (<self.id>) <self.__dict__> """
        b = BaseModel()
        result = b.__str__()
        token = result.split()
        self.assertEqual(token[0], '[BaseModel]')
        self.assertEqual(token[1], "(" + b.__dict__['id'] + ")")
        " compare the dict of the 3th section with b.__dict__ "
        just_dict = (b.__str__()).split('{')
        self.assertEqual(just_dict[1], (str(b.__dict__)).split('{')[1])

    """
    ------------------------------------------------------------
    2. save(self)
    ------------------------------------------------------------
    """
    def test_save(self):
        """ test if 'save' updates the value of 'updated_at' """
        b = BaseModel()
        value1 = b.updated_at
        time.sleep(0.5)
        b.save()
        value2 = b.updated_at
        self.assertNotEqual(value1, value2)

    """
    ------------------------------------------------------------
    3. to_dict(self)
    ------------------------------------------------------------
    """
    def test_to_dict(self):
        """ test if 'to_dict' returns the '__dict__' attributes with some changes:
        -> add '__class__': <class name>
        -> value of 'created_at' in iso format
        -> value of 'updated_at' in iso format """
        b = BaseModel()
        self.assertTrue('__class__' in b.to_dict())
        self.assertIsInstance(b.to_dict()['created_at'], str)
        self.assertIsInstance(b.to_dict()['updated_at'], str)
