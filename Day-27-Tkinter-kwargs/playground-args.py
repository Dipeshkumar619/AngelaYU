# Unlimited arguments , args is tuple
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(2,3,4,5,53,56,78,90))

def multi(*numbers):
    product=1
    for i in numbers:
        product*=i
    return product

print(multi(2,3,4,5,53,56,78,90))

# kwargs is keyword arguments which type is dictionary.
def calculate(**kwargs):
    print(kwargs)
    print(kwargs["add"])

print(calculate(add=3,find=5))

def newkfunction(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

newkfunction(2,add=4,multiply=6)

# class Car:
#     def __init__(self, **kw):
#         self.make=kw["make"]
#         self.model=kw["model"]
class Car:
    def __init__(self, **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
my_car=Car(make="Thar")
print(my_car.make)


def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)

4 (7,3,0) {'x': 10,'y': 64} <-- Answer

