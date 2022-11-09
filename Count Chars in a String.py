command = ''.join(input().split())
output = {}
for symbol in command:
    if symbol not in output:
        output[symbol] = 0
    output[symbol] += 1
for key, value in output.items():
    print(f"{key} -> {value}")
