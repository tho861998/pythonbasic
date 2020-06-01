x = input("enter a number: ")
print(type(x))  #it's string althoug you enter integer or float


y = int(input("enter a number: "))
print(type(y))  #it's integer : you can't enter float or string else

z = float(input("enter a number: "))
print(type(z))   #it's float type even if you enter an integer

eval = eval(input("enter a number: "))
print(type(eval)) #int if you enter 2 and float if you enter 2.00