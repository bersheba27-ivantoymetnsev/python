a = 10 #integer
b = 10.7 #float
c = "Hello" #string array
d = True #bool
c = False #bool
e = [1,2,3] #array/list
#print(type(d))
#print(type(e))
#print(10 % 3)
#print(type(10 % 3))
#print(a / 3) #float
#print(a // 3) #integer
#print(10 / 2) #float

list = [x for x in range(10)]
#print(list)

even_nums_list = [x for x in range(10) if x % 2 == 0]
#print(even_nums_list)

list_of_even_strings =  [str(x) for x in range(10) if x % 2 == 0]
#print(list_of_even_strings)

age = 50
comment = "child" if age < 13 else "adult"
# print("child" if age < 13 else "adult")

if age < 13:
    comment = "child"
else:
    comment = "adult"

# print(comment) 

numbers = [1, 2, 10, 7, 8]
#even_odd = [str(num) + ". " + ("even" if num % 2 == 0 else "odd") for num in numbers]
#print(even_odd)

#sequence[start:stop:step]
#start = index from
#stop = index to 
#step - step sequence
#built in sequences: rang, list, string
str = "Hello"
print(str[1:3]) #el
print(str[1:3:-1]) #No value
print(str[-1]) #o
print(str[:]) # copy of str
print(str[::-1]) #reverse string

print(str[2:0:-1]) #le
