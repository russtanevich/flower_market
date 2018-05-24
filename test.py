from datetime import datetime

import accessories
import flowers
import bouquets


date_future = datetime.strptime("12-12-2018", "%d-%m-%Y")
date_past = datetime.strptime("12-01-2018", "%d-%m-%Y")


def test_flower():
    roses = tuple(flowers.Rose(price=10, expired=date_future, colour="red", length=70) for _ in range(9))
    ribbons = tuple(accessories.Ribbon(price=10, expired=date_future) for _ in range(9))
    banch = bouquets.Bouquet(flowers=roses, accessories=ribbons)

    print banch.get_flower(price=10, colour="red", length=70)

    print banch.wilting_term


if __name__ == "__main__":
    test_flower()
