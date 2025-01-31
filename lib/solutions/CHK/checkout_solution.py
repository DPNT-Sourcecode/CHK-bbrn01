from collections import defaultdict

ITEMS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}
OFFERS = {
    "A": (3, 130),
    "B": (2, 45),
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    # build the basket for the given checkout
    basket = defaultdict(int)
    for id in skus:
        if id not in ITEMS:
            return -1
        basket[id] += 1

    # calculate the basket value
    total = 0
    for id, count in basket.items():
        # for items without offers, we can simply add the 
        unit_price = ITEMS[id]
        if id not in OFFERS:
            total += unit_price * count
            continue
        
        # for items with offers, factor in the reduced price 
        offer_req, offer_price = OFFERS[id]
        total += int(count / offer_req) * offer_price
        total += count % offer_req * unit_price

    return total
