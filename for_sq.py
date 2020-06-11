numbers = [1 , 2, 3, 4, 5]
square = 0
for var in numbers:
    square = var * var
    print(square)
print("Done")
print()

square = 0
for var in range(1, 11):
    square = var * var
    print(square)
print()

print("It is an example of for loop with else block")
for var in range(6):
    print(var)
else:
    print("The loop has completed execution. \n")

print("Here is an example of nested for loop.")
for num1 in range(3):
    for num2 in range(3):
        print(num1, ",", num2)





