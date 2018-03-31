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
    @classmethod
    def setUpClass(cls):
        """
        Uses build_item function to test item data
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/tests")

        cls.items = item_list(start_id, num_of_items)

    def test_item_has_id(self):
        for i in range(start_id, num_of_items + 1):
            att = hasattr(self.items[i], 'id')
            self.assertTrue(att)


    def test_item_has_name(self):
        for i in range(start_id, num_of_items + 1):
            att = hasattr(self.items[i], 'name')
            self.assertTrue(att)

    def test_item_name_is_string(self):
        for i in range(start_id, num_of_items + 1):
            att = self.items[i].name
            self.assertIsInstance(att, str)

    def test_item_has_desc(self):
        for i in range(start_id, num_of_items + 1):
            att = hasattr(self.items[i], 'desc')
            self.assertTrue(att)

    def test_item_desc_is_string(self):
        for i in range(start_id, num_of_items + 1):
            att = self.items[i].desc
            self.assertIsInstance(att, str)
