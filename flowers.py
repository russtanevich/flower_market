from market.goods import Good


class Flower(Good):

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
        self._is_broken = True
        return "{} is broken".format(self)


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
