try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x + y)

except ValueError:
    print("Please enter a number")
