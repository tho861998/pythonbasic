thislist = ["a", "b", "c", "d"]
if "a" in thislist:
    print("Yes, apple is in this list")
print(len(thislist))
thislist.append("e")
print(thislist)
thislist.insert(1, "new")
print(thislist)
thislist.remove("new")
print(thislist)
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)