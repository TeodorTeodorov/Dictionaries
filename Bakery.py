command = input().split()
dictionary  = {}
for i in range(0, len(command), 2):
    key = command[i]
    value = int(command[i + 1])
    dictionary[key] = value
print(dictionary)