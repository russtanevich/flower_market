from market.goods import Good


class Accessory(Good):
    def __init__(self, price, expired, discount=0):
        super(Accessory, self).__init__(price, expired, discount)


class Packaging(Accessory):
    pass


class Basket(Accessory):
    pass


class ArtificialFlower(Accessory):
    pass


class Ribbon(Accessory):
    pass


class Bows(Accessory):
    pass


