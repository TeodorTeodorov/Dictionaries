items = {"shards": 0, "fragments": 0, "motes": 0}
command = input().split()
full = False
while not full:
    for index in range(0, len(command), 2):
        quantity = int(command[index])
        item = command[index + 1].lower()
        if item not in items.keys():
            items[item] = 0
        items[item] += quantity
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            full = True
        elif items['fragments'] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            full = True
        elif items['motes'] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            full = True
        if full:
            break
    if full:
        break
    command = input().split()

for item, quantity in items.items():
    print(f'{item}: {quantity}')
