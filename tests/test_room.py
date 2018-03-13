#!/usr/bin/env/ python3

import unittest
from Syx.room import *
import os
import sys
from Syx.map import *





class RoomAttributesTestCase(unittest.TestCase):
    """
    Contains tests for room object
    """
    def setUp(self):
        """
        Uses build map function from map.py to build multiple rooms for testing
        purposes
        """

        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")
        id = 1
        num_of_rooms = 5
        self.map = Map(build_map(id, num_of_rooms))


    def test_room_has_id(self):
        """
        Verifies that room object has attribute id
        """
        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'id')
            self.assertTrue(att)
    def test_room_has_name(self):
        """
        Verifies that room object has the attribute name
        """
        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'name')
            self.assertTrue(att)
    def test_room_name_is_string(self):
        """
        Verifies that room object attribute name is a string
        """
        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms + 1):
            att = self.map.rooms[i].name
            self.assertIsInstance(att, str)
    def test_room_has_desc(self):
        """
        Verifies that room object has attribute desc
        """

        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'desc')
            self.assertTrue(att)
    def test_room_desc_is_string(self):
        """
        Verifies that room object attribute desc is a string
        """
        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms + 1):
            att = self.map.rooms[i].desc
            self.assertIsInstance(att, str)

    def test_room_has_exits(self):
        """
        Verifies that room object has attribute exits
        """
        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms + 1):
            att = hasattr(self.map.rooms[i], 'exits')
            self.assertTrue(att)

    def test_room_exits_are_dict(self):
        id = 1
        num_of_rooms = 5
        for i in range(id, num_of_rooms +1):
            att = self.map.rooms[i].exits
            self.assertIsInstance(att, dict)
