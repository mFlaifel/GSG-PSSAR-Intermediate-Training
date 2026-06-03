# import pdb

def calculate_total(items):
    # pdb.set_trace()    # Execution pauses here
    total = 0
    for item in items:
        total += item.get("price", 0)
    return total


itemPrices = [
    {"price": 10, "name": "apple"},
    {"price": 12, "name": "orange"},
    {"price": 13, "name": "pineapple"},
]

print(calculate_total(itemPrices))
