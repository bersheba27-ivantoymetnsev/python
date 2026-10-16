import random
def exists(numbers, num):

    for i in range(len(numbers)):
        if numbers[i] == num:
            return True
    return False

def distinct_random_numbers(min, max, size):

    numbers =[]

    while len(numbers) < size:
        num = random.randint(min,max)

        if not exists(numbers, num):
            numbers.append(num)

    return numbers

    

 
print (distinct_random_numbers(1, 49, 7))