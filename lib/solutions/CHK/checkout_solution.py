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
    basket = _remove_freebies_from_basket(basket)

    # calculate the basket value
    total = 0
    for id, count in basket.items():
        total += _calculate_item_basket_price(id, count)

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


def _remove_freebies_from_basket(basket: dict[str, int]) -> dict[str, int]:
    for id in basket.keys():
        if id in FREEBIES and FREEBIES[id][1] in basket:
            required_count, free_id = FREEBIES[id]
            x = int(basket[id] / required_count)
            basket[free_id] = max(basket[free_id] - x, 0)

    return basket


def _calculate_item_basket_price(id: str, count: int) -> int:
    # for items without offers, we can simply add the price muliplied by count
    unit_price = ITEMS[id]
    if id not in OFFERS:
        return unit_price * count

    # for items with offers, factor in the reduced price based on the best combination of offers
    # assumption is made that offers with more items are always better value
    offer_total = 0
    remaining_count = count
    ordered_offers: list[tuple[int, int]] = sorted(
        OFFERS[id], key=lambda x: x[0], reverse=True
    )

    for req_count, offer_price in ordered_offers:
        while remaining_count >= req_count:
            remaining_count -= req_count
            offer_total += offer_price

    return offer_total + unit_price * remaining_count
