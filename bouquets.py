# -*- coding: utf-8 -*-
""" The BOUQUET module"""
import datetime
import flowers as fl
import accessories as acc


class Bouquet(object):
    """THE BOUQUET class"""

    # DICT object with available items in the Bouquet and their attributes.
    _allowed = {
        fl.Flower: "_flowers",
        acc.Accessory: "_accessories"
    }
    _incorrect_item = "Impossible to add <{item}> to the {obj}"
    _not_exist = "No {item} in {obj}"
    _str_format = "<{cls} #{id},  ${prc} expired: {dt}>"

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
        """The sum of flowers and accessories"""
        return self.flowers | self.accessories

    @property
    def price(self):
        """The price of tne bouquet object"""
        return sum(item.price for item in self.items)

    def __contains__(self, flower):
        return flower in self.flowers

    def __iter__(self):
        return iter(self.flowers)

    def add_item(self, item):
        """ADD flowers and accessories to the bouquet"""
        type_ = set(type(item).mro()) & set(Bouquet._allowed)
        if type_:
            key = Bouquet._allowed[type_.pop()]
            self.__getattribute__(key).add(item)
        else:
            raise TypeError(Bouquet._incorrect_item.format(item=item, obj=self))

    def add_items(self, *items, **kwargs):
        """ADD an array of items to the bouquet."""
        count = kwargs.get("count")
        for item in items[:count]:
            self.add_item(item)

    def _gen_get_flower(self, **kwargs):
        """Return a GEN object of found flowers"""
        for flower in self.flowers:
            if all((flower.__getattribute__(key) == kwargs[key]) for key in kwargs):
                yield flower

    def get_flower(self, **kwargs):
        """Get the first found flower or None (if it is not exist)"""
        try:
            return next(self._gen_get_flower(**kwargs))
        except StopIteration:
            return

    def get_flowers(self, sort_by="__class__", **kwargs):
        """Get flowers by parameters. The sorting is available by attributes"""
        return sorted(
                    (_ for _ in self._gen_get_flower(**kwargs)),
                    key=lambda x: x.__getattribute__(sort_by)
                )

    def remove(self, item):
        """Remove item from the bouquet. And break a flower."""
        if item in self.flowers:
            item.break_down()
            self._flowers.remove(item)
        elif item in self.accessories:
            self._accessories.remove(item)
        else:
            raise LookupError(Bouquet._not_exist.format(item=item, obj=self))

    def uncouple(self):
        """To uncouple the bouquet."""
        for item in self.items:
            self.remove(item)

    @property
    def wilting_term(self):
        """Return wilting term of the bouquet. Return None if no flowers."""
        if not self.flowers:
            return
        date_now = datetime.datetime.now()
        gen_left_expired = ((flower.date_expired - date_now) for flower in self.flowers)
        avg_left_expired = sum(gen_left_expired, datetime.timedelta(0)) / len(self.flowers)
        avg_date_expired = date_now + avg_left_expired
        return avg_date_expired.date()

    def __str__(self):
        """The STR-FORMAT method"""
        return Bouquet._str_format.format(
                    cls=type(self).__name__,
                    id=id(self),
                    prc=self.price,
                    dt=self.wilting_term
                )

    def __repr__(self):
        return str(self)


