price = 49
txt = "This price is {} dollars"
print(txt.format(price))
txt = "This price is {:.2f} dollars" #with tow decimal places
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))