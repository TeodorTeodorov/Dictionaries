products_dict = {}
while True:
    product = input()
    if product == "buy":
        break

    item, price, count = product.split()
    if item not in products_dict.keys():
        products_dict[item] = []

        products_dict[item].append(float(price))
        products_dict[item].append(int(count))
    else:
        products_dict[item][1] += int(count)
        products_dict[item][0] = float(price)


for item in products_dict:
    prices = products_dict[item][0] * products_dict[item][1]
    print(f"{item} -> {prices:.2f}")