#!/usr/bin/env python3

import json

class Character():
    def __init__(
        self,
        id,
        name = "",
        desc = ""):
        self.id = id
        self.name = name
        self.desc = desc



def build_char(id):
    char = None
    #Opens the file
    with open("data/char/char{}.json".format(str(id)), 'r') as f:
        #Reads contents of file and stores in variable jsontext
        jsontext = f.read()
        #Decodes information from json file to dictionary
        d = json.loads(jsontext, strict = False)
        d['id'] = id
        char = Character(**d)
        return char
