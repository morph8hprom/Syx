import os
import sys
import json
import textwrap
from cmd2 import cmd
from world import *
from map import *
from room import *
from item import *
from character import *
from command import *
from game import *

"""
Main file which takes all components and creates/runs
the full game
"""

if __name__ == "__main__":
    room_start_id = 1
    
