#!/usr/bin/env python3
""" Unittest for ``/models/user.py``

class User:
    Public class attributes:
        - email
        - password
        - first_name
        - last_name
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'

python3 -m unittest tests/test_models/test_user.py
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    ------------------------------------------------------------
    Public class attributes
    ------------------------------------------------------------
    """
    def test_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('email' in User.__dict__)
        self.assertTrue('password' in User.__dict__)
        self.assertTrue('first_name' in User.__dict__)
        self.assertTrue('last_name' in User.__dict__)
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init(self):
        """ Test constructor: defalt, with **kwargs (*args won’t be used) """
        b = User()
        self.assertTrue('id' in b.__dict__)
        self.assertTrue('created_at' in b.__dict__)
        self.assertTrue('updated_at' in b.__dict__)
        b2 = User(**{'__class__': "SomeClass",
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
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b, User)
        self.assertIsInstance(b2, User)
