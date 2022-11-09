
dict = {}
while True:
    command = input()
    if '-' not in command:
        break
    name, number = command.split('-')
    if name not in dict.items():
        dict[name] = 0
    dict[name] = number
for check in range(int(command)):
    searched_name = input()
    if searched_name in dict.keys():
        print(f"{searched_name} -> {dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
