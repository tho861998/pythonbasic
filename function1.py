def my_function(country = "Norway"): #default parameters
    print("I am from " + country)
my_function("London")
my_function()
my_function("Canada")


def my_fun(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "orange"]
my_fun(fruits)