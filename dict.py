thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1984
}
print(thisdict)

x = thisdict["year"]# x = thisdict.get("model")
print(x )

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1984
}
thisdict["year"] = 2018
print(thisdict["year"])
for x in thisdict:
    print(thisdict[x])