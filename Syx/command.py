import textwrap
from cmd2 import Cmd
from Syx.world import *
from Syx.map import *
from Syx.room import *
from Syx.item import *
from Syx.character import *


class Command(Cmd):
    def __init__(self, world):
        self.prompt = ">"
        self.world = world
        self.player_loc = self.world.start_loc
        self.map = self.world.map

    def look(self):
        """
        Prints the name and description of current player location
        """

        # Sets the variable room_name to the name of the room which matches the
        # id of the current player location

        room_name = self.map.rooms[self.player_loc].name
        for line in textwrap.wrap(room_name, 80):
            print("\n{}".format(line))

        # Sets the variable room_desc to the description of the room which matches
        # id of the current player room
        room_desc = self.map.rooms[self.player_loc].desc
        for line in textwrap.wrap(room_desc, 80):
            print(line)

    def move(self, dir):
        """
        Changes the player location and uses look function to print the name
        and description of new room
        """
        # Sets the variable new_room to equal the return of a function which
        # checks if dir is listed in room exits
        new_room = self.map.rooms[self.player_loc]._exits(dir)

        # Prevents changing current player location if exit is not listed
        if new_room is None:
            print("There is no exit this way")
        else:
            print("\n")
            # Sets player_loc to equal the room id of the new room
            self.player_loc = new_room
            self.look()
