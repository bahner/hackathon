# coding: utf-8
"""Lage et kart over havområde for battleships"""
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
