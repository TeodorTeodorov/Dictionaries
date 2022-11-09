dict = {}

while True:
    command = input()
    if command == "stop":
        break

    int_command = int(input())
    if command not in dict:
        dict[command] = 0
    dict[command] += int_command

for resource, quantity in dict.items():
    print(f"{resource} -> {quantity}")