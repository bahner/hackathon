# coding: utf-8
"""Lage et kart over havområde for battleships"""

class Map(object):
    """Et kart over et havområde

    Tar størrelse i x og y. Standard er 5x5 for
    å matche LED-skjermen ti microbit
    """

    def __init__(self,
                 owner,
                 xmax=4,
                 ymax=4):
        """Init havområde"""

        self._id = owner
        self._map = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]

    def status(self):
        """Give status of object"""
        ret = {
            'owner': self._id,
            'map': self.map,
        }

        return ret

    @property
    def map(self):
        """Return the current map"""
        return self._map

    def shoot(self):
        """Aims at a place"""


    def place_ship(self, ship):
        """Places a ship in the map"""

        #check that ship can be placed without overlapping
        for xpos, ypos in ship:
            if self._map[xpos][ypos]:
                return False


        for xpos, ypos in ship:
            self._map[xpos][ypos] = 9
        return True
