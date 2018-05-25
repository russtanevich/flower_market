# -*- coding: utf-8 -*-
""" The FLOWERS module"""
from market.goods import Good


class Flower(Good):
    """The abstraction of flowers"""
    _broken_flag = "BROKEN"
    _no_broken_flag = ""
    _str_format = "<{cls} {colour} #{id}: ${prc}, expired: {dt} {brk}>"

    def __init__(self, price, expired, colour, length, discount=0, is_broken=False):
        super(Flower, self).__init__(price, expired, discount)
        self._colour = colour
        self._length = length
        self._is_broken = is_broken

    @property
    def colour(self):
        return self._colour

    @property
    def length(self):
        return self._length

    @property
    def is_broken(self):
        return self._is_broken

    def break_down(self):
        """The flower become broken"""
        self._is_broken = True

    def __str__(self):
        """The STR-FORMAT method"""
        is_broken = Flower._no_broken_flag
        if self.is_broken:
            is_broken = Flower._broken_flag
        return Flower._str_format.format(
                    cls=type(self).__name__,
                    colour=self.colour,
                    id=id(self),
                    prc=self.price,
                    dt=self.date_expired.date(),
                    brk=is_broken
                )

    def __repr__(self):
        return str(self)


class Rose(Flower):
    pass


class Chrysanthemum(Flower):
    pass


class Lily(Flower):
    pass


class Chamomile(Flower):
    pass


class Orchid(Flower):
    pass


class Tulip(Flower):
    pass


class Cornflower(Flower):
    pass


class Astra(Flower):
    pass


class Peony(Flower):
    pass


class Gladiolas(Flower):
    pass


class Gerbera(Flower):
    pass
