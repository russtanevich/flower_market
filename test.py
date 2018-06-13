import datetime
import logging
from sys import exc_info

import accessories
import flowers
import bouquets


logger = logging.getLogger("spam")
raise ValueError("Special Error")

def expired_in(days):
    """<Expired in> func returns dynamic expired terms."""
    return datetime.datetime.now() + datetime.timedelta(days=days)


def test_flower():
    """Testing of flowers and bouquets."""
    # DECLARE flowers
    white_roses = [flowers.Rose(price=2, expired=expired_in(3), colour="white", length=70) for _ in range(19)]
    red_roses = [flowers.Rose(price=3, expired=expired_in(5), colour="red", length=70) for _ in range(1000+1)]
    fresh_yellow_tulips = [flowers.Tulip(price=1.5, expired=expired_in(9), colour="yellow", length=50) for _ in range(21)]

    # ADD a some accessories
    ribbons = [accessories.Ribbon(price=1) for _ in range(99)]
    bows = [accessories.Bow(price=1) for _ in range(99)]
    packs = [accessories.Packaging(price=2) for _ in range(99)]
    baskets = [accessories.Basket(price=5) for _ in range(99)]

    # MAKE bouquets
    defenseless_spikes = bouquets.Bouquet(flowers=white_roses[:-1], accessories=(packs[0], ribbons[0], ribbons[1], bows[0]))
    million_red_roses = bouquets.Bouquet(flowers=red_roses[:-1])

    yellow_tulips = bouquets.Bouquet()
    yellow_tulips.add_items(*fresh_yellow_tulips[:19])
    yellow_tulips.add_items(baskets[0])
    yellow_tulips.add_items(*ribbons[2:4])

    strange_bouquet = bouquets.Bouquet()
    strange_bouquet.add_items(red_roses[-1], white_roses[-1], fresh_yellow_tulips[-1])

    # OPERATIONS:
    #  TRY TO ADD incorrect type to the bouquet
    try:
        item = 123
        defenseless_spikes.add_items(item)
    except TypeError:
        print("\nTEST #1. TRY ADD {item} into the {obj}\nGET {err}\n".format(
            item=item, obj=defenseless_spikes, err=exc_info()))

    #  Check flowers for breaking after uncoupling
    print("FRESH ROSES:\n{}".format(red_roses[:5]))
    million_red_roses.uncouple()
    print("And they become BROKEN after uncoupling:\n{}\n".format(red_roses[:5]))

    #  SORTING, ITER, SEARCHING
    print("\nSORTING BY EXPIRED:\n{}".format(strange_bouquet.get_flowers(sort_by="date_expired")))
    print("\nSEARCH RED AND FOR $3:\n{}".format(strange_bouquet.get_flowers(price=3, colour="red")))
    print("\nEXPIRED TERM OF THE {} -- {}\nIt consists from\n{}".format(
        strange_bouquet, strange_bouquet.wilting_term, strange_bouquet.items))


if __name__ == "__main__":
    test_flower()
