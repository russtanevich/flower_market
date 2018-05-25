# -*- coding: utf-8 -*-
""" The ACCESSORIES module"""
from market.goods import Good


class Accessory(Good):
    """ACCESSORY base class"""
    def __init__(self, price, expired=None, discount=0):
        super(Accessory, self).__init__(price, expired, discount)


class Packaging(Accessory):
    pass


class Basket(Accessory):
    pass


class ArtificialFlower(Accessory):
    pass


class Ribbon(Accessory):
    pass


class Bow(Accessory):
    pass
