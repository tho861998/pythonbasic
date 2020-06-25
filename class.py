class MyClass: #create class
    x = 5
p1 = MyClass() #create object named p1
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      #  name = "John"
       # age = 13
p1 = Person("John", 23)
print(p1.name)
print(p1.age)