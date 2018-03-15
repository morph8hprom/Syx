#!/usr/bin/env python3

import unittest
import os
from Syx.character import *

class CharacterAttributesTestCase(unittest.TestCase):
    """
    Verifies all attributes of character instance
    """

    def setUp(self):
        """
        Uses build_char function to create temporary character instance
        for testing purposes
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")
        start_id = 1
        num_of_char = 3
        self.chars = {}
        for i in range(start_id, num_of_char):
            self.chars[i] = build_char(i)


    def test_char_has_name(self):
        start_id = 1
        num_of_char = 3
        for i in range(start_id, num_of_char):
            att = hasattr(self.chars[i], 'name')
            self.assertTrue(att)
    def test_char_name_is_string(self):
        start_id = 1
        num_of_char = 3
        for i in range(start_id, num_of_char):
            att = self.chars[i].name
            self.assertIsInstance(att, str)
