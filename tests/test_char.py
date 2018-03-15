#!/usr/bin/env python3

import unittest
import os
from Syx.character import *

start_id = 1
num_of_char = 3
class CharacterAttributesTestCase(unittest.TestCase):
    """
    Verifies all attributes of character instance
    """
    @classmethod
    def setUpClass(cls):
        """
        Uses build_char function to test character data
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")

        cls.chars = {}
        for i in range(start_id, num_of_char + 1):
            cls.chars[i] = build_char(i, num_of_char)


    def test_char_has_name(self):

        for i in range(start_id, num_of_char + 1):
            att = hasattr(self.chars[i], 'name')
            self.assertTrue(att)
    def test_char_name_is_string(self):

        for i in range(start_id, num_of_char + 1):
            att = self.chars[i].name
            self.assertIsInstance(att, str)

    def test_char_has_desc(self):

        for i in range(start_id, num_of_char + 1):
            att = hasattr(self.chars[i], 'desc')
            self.assertTrue(att)

    def test_char_desc_is_string(self):

        for i in range(start_id, num_of_char + 1):
            att = self.chars[i].desc
            self.assertIsInstance(att, str)
