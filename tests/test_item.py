#!/usr/bin/env python3

import unittest
import os
from Syx.item import *

start_id = 1
num_of_items = 3

class ItemAttributesTestCase(unittest.TestCase):
    """
    Verifies all attributes of item instance
    """

    def setUp(self):
        """
        Uses build_item function to test item data
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")

        self.items = {}
        for i in range(start_id, num_of_items):
            self.items[i] = build_item(i, num_of_items)

    def test_item_has_id(self):
        for i in range(start_id, num_of_items):
            att = hasattr(self.items[i], 'id')
            self.assertTrue(att)


    def test_item_has_name(self):
        for i in range(start_id, num_of_items):
            att = hasattr(self.items[i], 'name')
            self.assertTrue(att)

    def test_item_name_is_string(self):
        for i in range(start_id, num_of_items):
            att = self.items[i].name
            self.assertIsInstance(att, str)

    def test_item_has_desc(self):
        for i in range(start_id, num_of_items):
            att = hasattr(self.items[i], 'desc')
            self.assertTrue(att)

    def test_item_desc_is_string(self):
        for i in range(start_id, num_of_items):
            att = self.items[i].desc
            self.assertIsInstance(att, str)
