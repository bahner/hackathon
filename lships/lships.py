# coding: utf-8
import random


class Map(object):
    """Et kart over et havomr�de

    Tar størrelse i x og y. Standard er 5x5 for
    å matche LED-skjermen ti microbit
    """

    def __init__(self,
                 owner,
                 xmax=4,
                 ymax=4):
        """Init havomr�de"""

        self._id = owner
        self.map = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]

    def status(self):
        """Give status of object"""
        ret = {
            'owner': self._id,
            'map': self.map,
        }

        return ret

    def shoot(self):
        """Aims at a place"""


    def place_ship(self, ship):
        """Places a ship in the map"""

        #check that ship can be placed without overlapping
        for xpos, ypos in ship:
            if self.map[xpos][ypos]:
                return False


        for xpos, ypos in ship:
            self.map[xpos][ypos] = 9
        return True

class Ship(object):
    """Et kart over et havomr�de

    Tar størrelse i x og y. Standard er 5x5 for
    å matche LED-skjermen ti microbit
    """

    def __init__(self,
                 length,
                 xmax=4,
                 ymax=4,
                ):
        """Init havomr�de"""

        self.length = length
        self.xmax = xmax
        self.ymax = ymax
        self.hull = self._gen_ship()

    def _gen_start_pos(self):
        """Generates a point within the allow range to start drawing.
        """
        _xpos = random.randint(0, self.xmax)
        _ypos = random.randint(0, self.ymax)
        return (_xpos, _ypos)

    def _gen_incrementors():
        """Function decides on a direction to in-/decrement x and y

        If x and y are both zero one of the must yield, and redraw.
        """

        while True:
            _xpos = random.randint(-1, 1)
            _ypos = random.randint(-1, 1)
            if not _xpos and not _ypos:
                continue
            else:
                return (_xpos, _ypos)

    def _gen_ship(self):

        while True:
            hull = list()
            xpos, ypos = self._gen_start_pos()
            xinc, yinc = self._gen_incrementors()
            # Generate a ship
            for _ in range(0, self.length):
                hull = hull + [(xpos, ypos)]
                xpos = xpos + xinc
                ypos = ypos + yinc

            # Verify that it's not out of bounds.
            if not 0 <= xpos <= self.xmax:
                continue
            if not 0 <= ypos <= self.ymax:
                continue

            return hull


skip = Ship(3)
skip2 = Ship(3)
print(skip.hull)

kart = Map('lars')

kart.place_ship(skip.hull)
kart.place_ship(skip2.hull)

print(kart.map)
