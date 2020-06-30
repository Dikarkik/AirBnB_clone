#!/usr/bin/env python3
""" test BaseModel """
import unittest, json, time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ tests """

    def test_init(self):
        """ def __init__(self, *args, **kwargs) """

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

    def test_str(self):
        """ test the string representation of a BaseModel instance """
        b = BaseModel()
        result = b.__str__()
        token = result.split()
        self.assertEqual(token[0], '[BaseModel]')

    def test_save(self):
        b = BaseModel(**{'__class__': "SomeClass",
                              'id': "f7f99",
                              'created_at': "2020-06-29T15:27:48.421135",
                              'updated_at': "2020-06-29T15:27:48.421148",})
        time.sleep(0.1)
        b.save()
        self.assertTrue(b.updated_at is not "2020-06-29T15:27:48.421148")
