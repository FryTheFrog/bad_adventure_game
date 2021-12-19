from unittest import TestCase

from resources.entities import Monster, Player
from resources.inventory import Smith, Witch

class TestCase(TestCase):
    def test_instantiation(self):
        p = Player()
        m = Monster()
        s = Smith()
        w = Witch()