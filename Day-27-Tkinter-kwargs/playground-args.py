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
