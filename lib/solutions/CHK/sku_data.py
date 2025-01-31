from collections import defaultdict

from solutions.CHK.constants import PRICE_TABLE


class SkuData:
    def __init__(self, price_table: str):
        self.item_prices: dict[str, int] = {}
        self.offers: dict[str, list[tuple]] = defaultdict(list)
        self.freebies: dict[str, tuple] = defaultdict(list)
        self.multi_offers: list[tuple[int, list[str]]] = []
        
        for line in price_table.splitlines()[3:-1]:
            l = line.split("|")
            item = l[1].strip()
            price = l[2].strip()
            offers = l[3].strip()
            self.item_prices[item] = int(price)

            for offer in offers.split(", "):
                if "buy any " in offer:
                    # buy any 3 of (S,T,X,Y,Z) for 45
                    pass
                    # self.multi_offers.append()
                elif " for " in offer:
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



