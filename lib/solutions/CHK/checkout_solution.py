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
        if id not in OFFERS:
            total += ITEMS[id] * count
            continue
        
        multiplier, price = OFFERS[id]
        total += int(count / multiplier) * 
        total += count % multiplier

    return total