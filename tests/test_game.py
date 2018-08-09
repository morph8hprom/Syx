#!/usr/bin/env/python3

import unittest
from Syx import game as g
from upacc import character as ch

class GameAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Game instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of Player and Game using default parameters
        """
        cls.test_player = ch.Player()
        cls.test_game = g.Game(cls.test_player)

    def test_game_has_constants(self):
        att = hasattr(self.test_game, '_constants')
        self.assertTrue(att)

    def test_game_has_world(self):
        att = hasattr(self.test_game, '_world')
        self.assertTrue(att)

    def test_game_has_map(self):
        att = hasattr(self.test_game, '_map')
        self.assertTrue(att)

    def test_game_has_items(self):
        att = hasattr(self.test_game, '_items')
        self.assertTrue(att)

    def test_game_has_characters(self):
        att = hasattr(self.test_game, '_characters')
        self.assertTrue(att)

    def test_game_has_player(self):
        att = hasattr(self.test_game, '_player')
        self.assertTrue(att)

    def test_game_has_player_loc(self):
        att = hasattr(self.test_game, '_player_loc')
        self.assertTrue(att)

class GameMethodsTestCase(unittest.TestCase):
    pass
