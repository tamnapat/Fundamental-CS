price = 0
for i in range(int(input("Please enter item nums: "))):
    price = price + int(input(f"Item {i + 1}: "))
print(price)
