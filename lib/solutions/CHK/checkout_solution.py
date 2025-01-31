from collections import defaultdict

from .sku_data import sku_data


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

    # a pre-pass to remove items from the basket which are part of a freebie offer
    basket = _remove_freebies_from_basket(basket)

    total = 0
    # a pre-pass to remove items which are part of a multi-deal offer
    for offer in sku_data.multi_offers:
        basket, value = _apply_multi_offers(basket, offer)
        total += value

    # calculate the basket value
    for id, count in basket.items():
        total += _calculate_item_basket_price(id, count)
    return total


def _build_basket(skus: str) -> dict[str, int]:
    if not isinstance(skus, str):
        raise InvalidBasket()

    basket = defaultdict(int)
    for id in skus:
        if id not in sku_data.item_prices:
            raise InvalidBasket()
        basket[id] += 1

    return basket


def _remove_freebies_from_basket(basket: dict[str, int]) -> dict[str, int]:
    for id in basket.keys():
        if id in sku_data.freebies and sku_data.freebies[id][1] in basket:
            required_count, free_id = sku_data.freebies[id]
            x = int(basket[id] / required_count)
            basket[free_id] = max(basket[free_id] - x, 0)

    return basket


def _apply_multi_offers(
    basket: dict[str, int], multi_offer: tuple[str, int, int]
) -> tuple[dict[str, int], int]:
    # assumption: items in multi-offers can not be part of any other offer type
    valid_items = multi_offer[0]
    req_count = multi_offer[1]
    offer_price = multi_offer[2]

    prices = []
    for item_id in valid_items:
        for _ in range(0, basket[item_id]):
            prices.append(sku_data.item_prices[item_id])
    prices.sort()

    # We prioritise the highest priced items to include in the offers. 
    # The remaining (cheapest) items must be charged at their base rate.
    offers = int(len(prices) / req_count)
    remainders = len(prices) % req_count
    total = offers * offer_price + remainders
    
    # update the basket to remove the items accounted for in the multi-deal
    return basket, total


def _calculate_item_basket_price(id: str, count: int) -> int:
    # for items without offers, we can simply add the price muliplied by count
    unit_price = sku_data.item_prices[id]
    if id not in sku_data.offers:
        return unit_price * count

    # for items with offers, factor in the reduced price based on the best combination of offers
    # assumption is made that offers with more items are always better value
    offer_total = 0
    remaining_count = count

    for req_count, offer_price in sku_data.offers[id]:
        while remaining_count >= req_count:
            remaining_count -= req_count
            offer_total += offer_price

    return offer_total + unit_price * remaining_count
