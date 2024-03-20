x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter a third number: "))

# print largest number
if x >= y and x >= z:
    print(x, "is the largest number.")
elif y >= x and y >= z:
    print(y, "is the largest number.")
else:
    print(z, "is the largest number.")
    
# print smallest number
if x <= y and x <= z:
    print(x, "is the smallest number.")
elif y <= x and y <= z:
    print(y, "is the smallest number.")
else:
    print(z, "is the smallest number.")

# print if all numbers are equal
if x == y or x == z or y == z:
    print("There are two equal numbers.")