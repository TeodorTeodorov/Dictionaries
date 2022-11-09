all_products = {}
while True:

    key_value = input().split(": ")
    if len(key_value) == 1:
        break

    product, quantity = key_value[0], key_value[1]
    if product not in all_products.keys():
        all_products[product] = 0
    all_products[product] += int(quantity)
print("Products in stock:")
for (key, value) in all_products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(all_products)}")
print(f"Total Quantity: {sum(all_products.values())}")