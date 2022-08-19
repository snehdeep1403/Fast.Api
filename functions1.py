def fun1():
    print("This is inside function")

def func1():
    print("Second funcrtion")



fun1()
func1()


def add(x,y):
    c = x + y
    return c

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def add_to_cart(prodid, cusid):
    print ("Create cart object")
    print ("add product to users cart")
    print ("redirct to cart page")

def calcu():
    first = input("Please enter first number : - ")
    second = input("Please enter second numnbenr:- ")
    op = input("Please let us konw what to do with these numbers : 1/2/3-- - ")

    
    if op == 1:
        print(add(first, second))
    elif op == 2:
        print(sub(first, second))
    elif op == 3:
        print(mul(first, second))
    else:
        print("Please enter valid operation")


calcu()


# map
# filter

l1 = ["one", "two", "three", "four"]

def capt(x):
    return x.capitalize()

print(map(capt, l1))

# filter
l2 = [12,44,55,66,77,88,30,44]

def filter_pass(x):
    if x < 33:
        return x

print(filter(filter_pass, l2))