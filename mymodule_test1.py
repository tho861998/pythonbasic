import mymodule1
a = mymodule1.person1["age"]
print(a)

import mymodule1 as mx
b = mx.person1["name"]
print(b)

import platform
a = platform.system()
print(a)
b = dir(platform)
print(b)