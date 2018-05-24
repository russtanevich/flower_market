class Bouquet(object):

    def __init__(self, flowers="", accessories=""):
        self._flowers = set(flowers)
        self._accessories = set(accessories)

    @property
    def flowers(self):
        return self._flowers

    @property
    def accessories(self):
        return self._accessories

    @property
    def items(self):
        return self.flowers | self.accessories

    @property
    def price(self):
        return sum(item.price for item in self.items)

    def __contains__(self, item):
        return item in self.flowers

    def __iter__(self):
        return iter(self.flowers)

    def add_item(self, item):
        """ADD flowers and accessories to the bouquet"""
        # self._validate(item)  # CONVERT good to tuple for maintaining of operation iter
        self._flowers.add(item)

    def add_items(self, *items, **kwargs):
        """ADD array of items to the store."""
        count = kwargs.get("count")
        for item in items[:count]:
            self.add_item(item)

    def _gen_get_flower(self, **kwargs):
        for flower in self.flowers:
            if all((flower.__getattribute__(key) == kwargs[key]) for key in kwargs):
                yield flower

    def get_flower(self, **kwargs):
        try:
            return next(self._gen_get_flower(**kwargs))
        except StopIteration:
            return

    def get_flowers(self, sort_by=None, **kwargs):
        return sorted(
                    (_ for _ in self._gen_get_flower(**kwargs)),
                    key=lambda x: x.__getattribute__(sort_by)
                )

    def remove(self, item):
        if item in self.flowers:
            item.break_down()
            self._flowers.remove(item)
        elif item in self.accessories:
            self._accessories.remove(item)
        else:
            raise LookupError("No {} in {}".format(item, self))

    def uncouple(self):
        for item in self.items:
            self.remove(item)

    def __str__(self):
        return "<{} ${}>".format(self.__class__.__name__, self.price)

    def __repr__(self):
        return str(self)


