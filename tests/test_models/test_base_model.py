#!/usr/bin/env python3
import unittest, json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_str(self):
        b = BaseModel()
        result = b.__str__()
        token = result.split()
        self.assertEqual(token[0], '[BaseModel]')
        """
        string_dir = " ".join(token[2:])
        print(string_dir)"""
