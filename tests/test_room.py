#!/usr/bin/env/ python3

import unittest
from Syx.room import *
class BuildRoomTestCase(unittest.TestCase):
    """
    Contains tests for build room function
    """


class RoomAttributesTestCase(unittest.TestCase):
    """
    Contains tests for room object
    """
    def setUp(self):
        """
        Uses a json file to build a room for testing
        """
        #self.room = build_room()
        pass

    def test_room_has_name(self):
        """
        Verifies that room object has the attribute name
        """
        att = hasattr(self.room, name)
        assertTrue(att)
    def test_room_name_is_string(self):
        """
        Verifies that room object attribute name is a string
        """
        att = self.room.name
        assertIsInstance(att, string)
    def test_room_has_desc(self):
        """
        Verifies that room object has attribute desc
        """
        att = hasattr(self.room, desc)
        assertTrue(att)
    def test_room_desc_is_string(self):
        att = self.room.desc
        assertIsInstance(att, string)

    def test_room_has_exits(self):
        att = hasattr(self.room, exits)
        assertTrue(att)
    
