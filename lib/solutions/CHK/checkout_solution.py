from collections import defaultdict

from .sku_data import FREEBIES, ITEMS, OFFERS


class InvalidBasket(Exception):
    def __init__(self):
        self.msg = "Basket contained invalid item."


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket = _build_basket(skus)
    except InvalidBasket:
        return -1

    # in a first-pass, remove items from the basket which are part of a freebie offer
    for id, count in basket.items():
        if id in FREEBIES:
            required_count, free_id = FREEBIES[id]
            basket[free_id] / 
            while count >= required_count and basket_copy.get(free_id, 0) > 0:
                total -= ITEMS[free_id]
                basket[free_id] -= 1


    # calculate the basket value
    total = 0
    for id, count in basket.items():
        # for items without offers, we can simply add the price muliplied by count
        unit_price = ITEMS[id]
        if id not in OFFERS:
            total += unit_price * count
        else:
            # for items with offers, factor in the reduced price based on the number of offers
            offer_req, offer_price = OFFERS[id][0]  # TODO: pick best offer
            
            total += int(count / offer_req) * offer_price
            total += count % offer_req * unit_price

        # for items with freebies, remove their value from the total if present in the basket
        if id in FREEBIES:


    return total


def _build_basket(skus: str) -> dict[str, int]:
    if not isinstance(skus, str):
        raise InvalidBasket()

    basket = defaultdict(int)
    for id in skus:
        if id not in ITEMS:
            raise InvalidBasket()
        basket[id] += 1

    return basket



