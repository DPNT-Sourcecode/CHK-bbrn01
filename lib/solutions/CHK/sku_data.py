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
        self.item_prices: dict[str, int] = {
        #     "A": 50,
        #     "B": 30,
        #     "C": 20,
        #     "D": 15,
        #     "E": 40,
        #     "F": 10,
        }
        self.offers: dict[str, list[tuple]] = {
            # "A": [(3, 130), (5, 200)],
            # "B": [(2, 45)],
        }
        self.freebies: dict[str, tuple] = {
            # "E": (2, "B"),
            # "F": (3, "F"),
        }

        for line in price_table.splitlines()[3:-1]:
            item, price, offers = line.split("|")
            


sku_data = SkuData(PRICE_TABLE)


