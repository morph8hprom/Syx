import unittest
import os
from Syx.map import *
from Syx.room import *

class MapAttributesTestCase(unittest.TestCase):
    """
    Verifies all attributes of map class
    """
    def setUp(self):
        """
        Uses build_map function to create multiple room instances
        inside of the map object
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")
        self.map = Map(build_map(1, 5))

    def test_map_has_rooms(self):
        att = hasattr(self.map, 'rooms')
