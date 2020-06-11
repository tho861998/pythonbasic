value = eval(input("Please enter a number between 0 and 10: "))
if value >= 0:
    if value <= 10:
        print("It's in range")
    else:
        print("It is too large")
else:
    print(value, "is too small")
print("Done")
