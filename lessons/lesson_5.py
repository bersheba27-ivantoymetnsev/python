import random

# int in python 32 bytes
#a: int = 2000
#a is variable name
#each name is bound to an object, it contains reference (address) to some data
#a is like pointer(8 bytes)
#pointer -> |count ref(8 bytes)|type( 8 bytes)|size (8 bytes)|data (int: 8 bytes)| 

#== and is
#== is equal. May be different objects with the same value
#"is" operator - is the same. One object but different names

a: int = 2000
b: int = 2000

b: int = int("2000")
c: int = int("2000")

print(f"a == b: {a == b}") #true
print(f"a is b: {a is b}") #true. a and b points to the same address
print(f"b == c: {a == b}") #true
print(f" b is c: {a is b}") #false. c and b(explicit casting to int) point to different addresses

a: int = 50000
b = a
d: int = 100000
print(a is b) #true
def double(c: int) -> int:
    result: int = c * 2
    print(a is c) #true
    return result
a = double(a)
print(b is a) # false
print(a == d) #true
print(a is d) #false 

#immutable and mutable
#Only list is mutable, other types immutable
l1: list[int] = [1,2,3]
min = 100
max = 200
def add_random_number(l2: list[int], min1:int, max2:int): 
    l2.append(random.randint(min1,max2))
    print(min is min1) #true
    min1 = 1000
    max2 = 5000
    print(min is min1) #false

add_random_number(l1, min, max)
print(l1, min, max)

#tuple - immutable list
t: tuple[int, int, int] #tuple with 3 ints
t: tuple[int, ...] # tuple with any amount of ints

l1: list[int] = list(range(100000))
#num1, num2, *_ = l1 # works but performance issues are present
num1, num2 = l1[0], l1[1] 
t1: tuple[int, ...] = tuple(l1)
t2: tuple[str, int] = "1", 2

def string_number_presentation(num: int) -> tuple[str, int]:
    str_presentation: str = ""

    if num == 1:
        str_presentation = "one"
    elif num == 2:
        str_presentation = "two"
    else:
        str_presentation = str(num)

    return str_presentation, num


str_num, number_num = string_number_presentation(10) #unpacking

a: int = 10
b: int = 20
b, a = a, b #packing(swapping) int tuple(a, b), unpacking to b and a=
