list = []

loop = int(input("How many times: "))

for i in range(loop):
    user_input = input(f"{i + 1}: ")
    list.append(user_input)

for i in sorted(list):
    print(f"{i}", end=" ")

print()
