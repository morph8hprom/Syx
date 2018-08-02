#!/usr/bin/env python3

import textwrap
from cmd2 import Cmd




class Command(Cmd):
    def __init__(self, main_map, player):
        Cmd.__init__(self)
        self._transcript_files = None
        self.prompt = ">"
        self.map = main_map
        self.player_loc = self.player.loc



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
        # exit_msg = self.map.rooms[self.player_loc].exit_msg[dir]
        # Prevents changing current player location if exit is not listed
        if new_room is None:
            print("There is no exit this way")
        else:
            print("\n")
            # Sets player_loc to equal the room id of the new room
            self.player_loc = new_room
            self.look()

    def do_north(self, args):
        self.move('north')

    def do_east(self, args):
        self.move('east')
    def do_south(self, args):
        self.move('south')
    def do_west(self, args):
        self.move('west')

    def do_quit(self, args):
        quit = input("Quit?\nYes or no\n>")
        if quit.lower() == "yes":
            return True
        elif quit.lower() == 'no':
            return False
        else:
            print("Input not recognized")
