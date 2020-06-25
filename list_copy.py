thislist = ["a", "b", "c", "d", "e"]
thislist.sort()
print(thislist)
thislist.reverse()
print(thislist)
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)
print(mylist)

list1 = ["a", "b"]
list2 = ["c", "d"]
list3 = list1 + list2
print(list3)
for x in list1:
    list2.append(x)
print(list2)
list1.extend(list2)
print(list1)

mylist = list(("a", "b"))
print(mylist)