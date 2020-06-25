thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1984
}
for x in thisdict:
    print(x)
for x, y in thisdict.items():
    print(x, y) 
if "model" in thisdict:
    print("Yes, there is model in this dictionary")
print(len(thisdict))
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("color")
print(thisdict)

if "i" in "string ":
    print("Yes, there is i in string")