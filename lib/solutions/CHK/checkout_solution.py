

# noinspection PyUnusedLocal
# skus = unicode string

price_table = { 'A': {'Price': 50, 'Offers': ['3A', 130]},
                'B': {'Price': 30, 'Offers': ['2b', 45]},
                'C': {'Price': 20, 'Offers': []},
                'D': {'Price': 15, 'Offers': []}
               }


def checkout(skus):
    if ((skus.isalpha() and skus.isupper()) or skus == ''):
        order_dict = build_orders(skus)
        running_total = 0
        for order in order_dict:
            cur_total = get_price(order, order_dict[order])
            running_total += cur_total
        return running_total
    else:
        return -1

def get_price(stock, units):
    try:
        item = price_table.get(stock)
        running_total = 0
        offers = item.get('Offers', [])
        if item.get('Offers', []) != []:
            offer = int(offers[0][0])
            if units >= offer:
                offer_quantity = int(units / int(offer))
                running_total += (offers[1] * offer_quantity)
                units -= int(offer_quantity * offer)
        amount = units * item['Price']
        running_total += amount
        return running_total
    except Exception as e:
        return 0


def build_orders(orders):
    order_dict = {}
    for order in orders:
        quantity = order_dict.get(order.upper(), 0)
        quantity += 1
        order_dict.update({order.upper(): quantity})
    return order_dict