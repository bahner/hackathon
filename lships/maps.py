# coding: utf-8
"""Lage et kart over havområde for battleships"""

import random

class Kart(object):
    """Et kart over et havområde

    Tar størrelse i x og y. Standard er 5x5 for
    å matche LED-skjermen ti microbit
    """

    def __init__(self,
                 nummer,
                 eier=None,
                 x=5,
                 y=5):
        """Init havområde"""

        self._id = nummer
        self.eier = eier
        self.map = [[0 for _ in range(x)] for _ in range(y)]

    def status(self):
        """Give status of object"""
        ret = {
            'nummer': self._id,
            'eier': self.eier,
        }

        return ret

    def _xy_inc(self):
        """Function decides on a direction to in-/decrement x and y

        If x and y are both zero one of the must yield, and redraw.
        """

        while True:
            self.xinc = random.randint(-1, 1)
            self.yinc = random.randint(-1, 1)
            if not xinc and not yinc:
                continue
            else:
                break
