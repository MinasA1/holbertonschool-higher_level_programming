#!/usr/bin/python3
"""test for Base"""


import unittest
from models import base
from models.base import Base


class Test_Base(unittest.TestCase):
    """tests for class Base"""
    def test_for_mdl_doc(self):
        doc = base.__doc__
        self.assertTrue(len(doc) > 0)

    def test_for_cls_doc(self):
        doc = Base.__doc__
        self.assertTrue(len(doc) > 0)

    def test_for_methods_doc(self):
        doc = Base.__init__.__doc__
        self.assertTrue(len(doc) > 0)
        doc = Base.to_json_string.__doc__
        self.assertTrue(len(doc) > 0)
        doc = Base.from_json_string.__doc__
        self.assertTrue(len(doc) > 0)
        doc = Base.save_to_file.__doc__
        self.assertTrue(len(doc) > 0)
        doc = Base.create.__doc__
        self.assertTrue(len(doc) > 0)
        doc = Base.load_from_file.__doc__
        self.assertTrue(len(doc) > 0)

    def test_for_id(self):
        self.dummy = Base()
        self.assertEqual(self.dummy.id, 1)
        self.dummy = Base(89)
        self.assertEqual(self.dummy.id, 89)
        del self.dummy

if __name__ == '__main__':
    unittest.main()
