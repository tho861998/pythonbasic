try:
    print(x)
except:
    print("An error occured")

try:
    print(x)
except NameError:
    print("var x is not defined")
except:
    print("something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")