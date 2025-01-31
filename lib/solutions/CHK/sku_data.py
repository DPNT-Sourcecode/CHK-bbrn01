from collections import defaultdict

PRICE_TABLE = """+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+"""


class SkuData:
    def __init__(self, price_table: str):
        self.item_prices: dict[str, int] = {}
        self.offers: dict[str, list[tuple]] = defaultdict(list)
        self.freebies: dict[str, tuple] = defaultdict(list)

        for line in price_table.splitlines()[3:-1]:
            l = line.split("|")
            item = l[1].strip()
            price = l[2].strip()
            offers = l[3].strip()
            self.item_prices[item] = int(price)

            for offer in offers.split(", "):
                if " for " in offer:
                    for_offer = offer.split(" for ")
                    item_id = for_offer[0][-1]
                    req_count = int(for_offer[0][:-1])
                    offer_price = int(for_offer[1])
                    self.offers[item_id].append(
                        (
                            req_count,
                            offer_price,
                        )
                    )
                elif " get one " in offer:
                    get_one_offer = offer.split(" get one ")
                    req_count = int(get_one_offer[0][:-1])
                    free_id = get_one_offer[1][0]
                    # for freebie offers of the same item we require an additional item in the
                    # basket. e.g. buy 2x get x free, with only 2 items there is no item left to be free.
                    if item == free_id:
                        req_count += 1
                    self.freebies[item] = (req_count, free_id)

                # order the offers from highest value to lowest
                self.offers[item_id] = sorted(
                    self.offers[item_id], key=lambda x: x[0], reverse=True
                )


sku_data = SkuData(PRICE_TABLE)







