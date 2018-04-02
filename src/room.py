#!/usr/bin/env/ python3

import json
"""
Defines a room class and a fucntion used to create an instance of room class
"""
class Room():
    def __init__(
        self,
        id,
        name,
        desc,
        exits):
        self.id = id
        self.name = name
        self.desc = desc
        self.exits = exits

    def _exits(self, dir):
        """
        Verifies that provided exit is in room's list of exits
        """
        if dir in self.exits:
            return self.exits[dir]
        else:
            return None


def build_room(id):
    room = None
    #Opens the file
    with open("data/room/room{}.json".format(str(id)), 'r') as f:
        #Reads contents of file and stores in variable jsontext
        jsontext = f.read()
        #Decodes information from json file to a dictionary
        d = json.loads(jsontext, strict = False)
        d['id'] = id
        room = Room(**d)
        return room
