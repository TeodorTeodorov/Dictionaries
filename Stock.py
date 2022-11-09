comand = input().split()
products = {}
for i in range(0, len(comand), 2):
    key = comand[i]
    value = comand[i+1]
    products[key] = int(value)

serch_products = input().split()

for product in serch_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")