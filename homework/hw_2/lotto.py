import random

def exists(numbers, num, index):
    i = 0
    found = False

    while i < index:
        if numbers[i] == num:
            found = True
        i += 1

    return found

def distinct_random_numbers(min, max, size):

    if size > max - min + 1 or size < 0:
        return []

    
    random_nums = [random.randint(min,max) for x in range(size)]
    unique_random_nums = [random_nums[x] for x in range(len(random_nums)) if not exists(random_nums, random_nums[x], x)]
    return unique_random_nums

  
print (distinct_random_numbers(1, 49, 7))
