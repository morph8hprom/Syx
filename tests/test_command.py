#!/usr/bin/env python3

import unittest
import os
from Syx.command import *
from Syx.world import *
from Syx.map import *
from Syx.room import *
from Syx.item import *
from Syx.character import *
import cmd

class CommandAttributesTestCase(unittest.TestCase):
    """
    Verifies all attrbiutes of command instance
    """
    @classmethod
    def setUpClass(cls):
        pass
