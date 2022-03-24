

# noinspection PyUnusedLocal
# skus = unicode string

price_table = { 'A': {'Price': 50, 'Offers': ['3A', 130]},
                'B': {'Price': 30, 'Offers': ['2b', 45]},
                'C': {'Price': 20, 'Offers': []},
                'D': {'Price': 15, 'Offers': []}
               }

def checkout(skus):
    try:
        stock = skus[1]
        units = skus[0]
        item = price_table.get(stock)
        running_total = 0
        offers = item.get('Offers', [])
        offer = int(item.get('Offers', [])[0][0])
        if item.get('Offers', []) != []:
            if units >= offer:
                offer_quantity = int(units / int(offer))
                running_total += offers[1] * offer_quantity
                units -= offer_quantity * units
        amount = units * item['Price']
        running_total += amount
        return running_total
    except Exception as e:
        return -1
