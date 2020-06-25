try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

username = input("Enter an username: ")
try:
#username = input("Enter an username: ")
  print("Hello " + username)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
