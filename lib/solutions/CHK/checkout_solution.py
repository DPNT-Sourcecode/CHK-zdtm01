

# noinspection PyUnusedLocal
# skus = unicode string
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+

price_table = { 'A': {'Price': 50, 'Offers': ['3A', 130]},
                'B': {'Price': 30, 'Offers': ['2b', 45]},
                'C': {'Price': 20, 'Offers': []},
                'D': {'Price': 15, 'Offers': []}
               }

def checkout(skus):
    raise NotImplementedError()


