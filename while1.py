#!/usr/bin/python3
"""
count = 0
while (count < 10):
    print("The count: ", count)
    count += 1
print("Goodbye")
"""
var = 1
while (var < 4):
    num = int(input("enter a number smaller than 4: "))
    print("Your entered number: ", num)
    var += 1
    print("Your current number:", var)
    print()
print("Never allow number greater than 4 to input!")
print()

n = 1
stop = int(input())
while n <= stop:
    print("VALUE: ", n)
    n += 1