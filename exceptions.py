try:
    count = int(input("Give me a Number: "))
except ValueError:
    print("That's Not a number!")
else:
    print(" Hi there," * count)