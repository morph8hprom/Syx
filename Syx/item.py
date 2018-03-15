#!/usr/bin/env python3

import json
"""
Defines an item class and a fucntion used to create an instance of item class
"""
class Item():
    def __init__(self,
        id,
        name = "",
        desc = ""):
        self.id = id
        self.name = name
        self.desc = desc


def build_item(id, num_of_items):
    item = None
    #Open file
    with open("data/item/item{}.json".format(str(id)), 'r') as f:
        #Reads contents of file and stores in variable jsontext
        jsontext = f.read()
        #Decodes information into dictionary
        d = json.loads(jsontext, strict = False)
        print("Gathering item data")
        d['id'] = id
        item = Item(**d)
        print("Successfully created item {} of {}".format(str(id), num_of_items))
        return item
