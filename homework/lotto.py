import random
def exists(numbers, num):
    i = 0
    found = False

    while i < len(numbers) and not found:
        if numbers[i] == num:
            found = True
        i += 1

    return found


def distinct_random_numbers(min, max, size):
    numbers = []

    if size > max - min + 1 or size < 0:
        return numbers

    while len(numbers) < size:
        num = random.randint(min, max)

        if not exists(numbers, num):
            numbers.append(num)

    return numbers

    

 
print (distinct_random_numbers(1, 49, 7))