#!/usr/bin/env python3

import os
import sys
import json
import textwrap
from cmd2 import Cmd
from Syx.world import *
from Syx.map import *
from Syx.room import *
from Syx.item import *
from Syx.character import *
from Syx.command import *


class Game():
    def __init__(self, world):
        self.world = world
        self.map = world.map
        self.items = world.items
        self.chars = world.chars

        #Add character select
