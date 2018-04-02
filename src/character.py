#!/usr/bin/env python3

import json
"""
Defines a character class and a fucntion used to create an instance of character class
"""
class Character():
    def __init__(
        self,
        id,
        name = "",
        desc = ""):
        self.id = id
        self.name = name
        self.desc = desc



def build_char(id, num_of_chars):
    char = None
    #Opens the file
    with open("data/char/char{}.json".format(str(id)), 'r') as f:
        #Reads contents of file and stores in variable jsontext
        jsontext = f.read()
        #Decodes information from json file to dictionary
        d = json.loads(jsontext, strict = False)
        print("Gathering character data")
        d['id'] = id
        char = Character(**d)
        print("Successfully created character {} of {}".format(str(id), num_of_chars))
        return char

def char_list(id, num_of_chars):
    list = {}
    for i in range(id, num_of_chars + 1):
        list[i] = build_char(i, num_of_chars)
    return list