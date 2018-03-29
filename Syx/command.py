import textwrap
from Syx.world import *
from Syx.map import *
from Syx.room import *
from Syx.item import *
from Syx.character import *
import cmd

class Command(cmd.Cmd):
    def __init__(self, world):
        self.prompt = ">"
        self.world = world
        self.player_loc = self.world.start_loc
