#!/usr/bin/env python3

import os
import sys
import json
import textwrap
from cmd2 import Cmd
from world import *
from map import *
from room import *
from command import *
from game import *

"""
Main file which takes all components and creates/runs
the full game
"""

def main():
    start_id = 1
    num_of_rooms = 5
    start_loc = 1
    game = build_game(start_id, num_of_rooms, start_loc)
    cli = Command(game)
    cli.cmdloop()


if __name__ == "__main__":
    main()
