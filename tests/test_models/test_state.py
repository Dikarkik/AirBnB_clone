#!/usr/bin/env python3
""" Unittest for ``/models/state.py``

class State:
    Public class attributes:
        - name
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'

python3 -m unittest tests/test_models/test_state.py
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    ------------------------------------------------------------
    Public class attributes
    ------------------------------------------------------------
    """
    def test_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('name' in State.__dict__)
        self.assertIsInstance(State.name, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init(self):
        """ Test constructor: defalt, with **kwargs (*args won’t be used) """
        b = State()
        self.assertTrue('id' in b.__dict__)
        self.assertTrue('created_at' in b.__dict__)
        self.assertTrue('updated_at' in b.__dict__)
        b2 = State(**{'__class__': "SomeClass",
                      'id': "f7f99",
                      'created_at': "2020-06-29T15:27:48.421135",
                      'updated_at': "2020-06-29T15:27:48.421148",
                      'name': "Antioquia"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in b2.__dict__)
        """ must create the keys """
        self.assertTrue('id' in b2.__dict__)
        self.assertTrue('created_at' in b2.__dict__)
        self.assertTrue('updated_at' in b2.__dict__)
        self.assertTrue('name' in b2.__dict__)
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b, State)
        self.assertIsInstance(b2, State)
