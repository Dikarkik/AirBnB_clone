#!/usr/bin/env python3
""" Unittest for ``/models/place.py``

class Place:
    Public class attributes:
        - city_id
        - user_id
        - name
        - description
        - number_rooms
        - number_bathrooms
        - max_guest
        - price_by_night
        - latitude
        - longitude
        - amenity_ids
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'

python3 -m unittest tests/test_models/test_place.py
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    ------------------------------------------------------------
    Public class attributes
    ------------------------------------------------------------
    """
    def test_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('city_id' in Place.__dict__)
        self.assertTrue('user_id' in Place.__dict__)
        self.assertTrue('name' in Place.__dict__)
        self.assertTrue('description' in Place.__dict__)
        self.assertTrue('number_rooms' in Place.__dict__)
        self.assertTrue('number_bathrooms' in Place.__dict__)
        self.assertTrue('max_guest' in Place.__dict__)
        self.assertTrue('price_by_night' in Place.__dict__)
        self.assertTrue('latitude' in Place.__dict__)
        self.assertTrue('longitude' in Place.__dict__)
        self.assertTrue('amenity_ids' in Place.__dict__)

        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init(self):
        """ Test constructor: defalt, with **kwargs (*args won’t be used) """
        b = Place()
        self.assertTrue('id' in b.__dict__)
        self.assertTrue('created_at' in b.__dict__)
        self.assertTrue('updated_at' in b.__dict__)
        b2 = Place(**{'__class__': "SomeClass",
                      'id': "f7f99",
                      'created_at': "2020-06-29T15:27:48.421135",
                      'updated_at': "2020-06-29T15:27:48.421148",
                      'name': "room"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in b2.__dict__)
        """ must create the keys """
        self.assertTrue('id' in b2.__dict__)
        self.assertTrue('created_at' in b2.__dict__)
        self.assertTrue('updated_at' in b2.__dict__)
        self.assertTrue('name' in b2.__dict__)
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b, Place)
        self.assertIsInstance(b2, Place)
