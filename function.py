def my_fun():
    print("Hello from a function")
my_fun()

def my_function(fname):
    print(str(fname) + " Refsnes")
my_function(123)
my_function("Tobias")
my_function("Linus")

def my_func(fname, lname):
    print(fname + " " + lname)
my_func("Thaung Htike", "Oo")

def my_fun(*kids): #unknown parameters
    print("The youngest child is " + kids[1])
my_fun("emil", "dick", "steve")
