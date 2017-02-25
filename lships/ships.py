# coding: utf-8
"""Lage et kart over havområde for battleships"""

import random

class Ship(object):
    """Et kart over et havområde

    Tar størrelse i x og y. Standard er 5x5 for
    å matche LED-skjermen ti microbit
    """

    def __init__(self,
                 length,
                 xmin=0,
                 xmax=4,
                 ymin=0,
                 ymax=4
                ):
        """Init havområde"""

        self.length = length
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def _gen_start_pos(self):
        """Generates a point within the allow range to start drawing.
        """

        self.x = random.randint(self.xmin, self.xmax)
        self.y = random.randint(self.ymin, self.ymax)

    def _gen_incrementors(self):
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

    def gen_ship(self):
        """Generates a random ship"""
