#!/usr/bin/env python3

import unittest
import os
from Syx.world import *
from Syx.item import *
from Syx.character import *
from Syx.map import *
from Syx.room import *


class WorldAttributeTestCase(unittest.TestCase):
    """
    Verifies all attributes of world instance
    """

    def setUp(self):
        """
        Uses build_world function to check world data
        """
