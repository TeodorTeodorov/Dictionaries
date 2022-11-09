people_num = int(input())
register = {}
for people in range(people_num):
    command = input().split()
    if command[0] == "register":



        name, car_number = command[1], command[2]
        if name not in register:
            register[name] = car_number
            print(f"{name} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")
    else:
        name = command[1]
        if name not in register:
            print(f"ERROR: user {name} not found")
        else:
            # register.pop(name)
            del register[name]
            print(f"{name} unregistered successfully")

for name in register:
    print(f"{name} => {register[name]}")