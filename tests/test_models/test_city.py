#!/usr/bin/env python3
""" Unittest for ``/models/city.py``
class City:
    Public class attributes:
        - state_id
        - name
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'

python3 -m unittest tests/test_models/test_city.py
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    ------------------------------------------------------------
    Public class attributes
    ------------------------------------------------------------
    """
    def test_class_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)
        """ check type """
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init(self):
        """ test constructor: defalt, with **kwargs (*args won’t be used) """
        c = City()
        self.assertTrue('id' in c.__dict__)
        self.assertTrue('created_at' in c.__dict__)
        self.assertTrue('updated_at' in c.__dict__)

        c2 = City(**{'__class__': "SomeClass",
                     'id': "f7f99",
                     'created_at': "2020-06-29T15:27:48.421135",
                     'updated_at': "2020-06-29T15:27:48.421148",
                     'name': "Medellin"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in c2.__dict__)
        """ must create the keys """
        self.assertTrue('id' in c2.__dict__)
        self.assertTrue('created_at' in c2.__dict__)
        self.assertTrue('updated_at' in c2.__dict__)
        self.assertTrue('name' in c2.__dict__)
        self.assertIsInstance(c, BaseModel)
        self.assertIsInstance(c2, BaseModel)
        self.assertIsInstance(c, City)
        self.assertIsInstance(c2, City)
