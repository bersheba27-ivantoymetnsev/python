def indexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    first_index = -1

    for i in range(len(numbers)):
        if numbers[i] == num and first_index == -1:
            first_index = i

    return first_index

    
def lastIndexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
        lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    last_index = -1

    for i in range(len(numbers)):
        if numbers[i] == num:
            last_index = i

    return last_index

def min_even (numbers):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    min_even_num = None
    even_found = False

    for num in numbers:
        if not even_found and num % 2 == 0:
            min_even_num = num
            even_found = True
        elif even_found  and num % 2 == 0 and num < min_even_num:
            min_even_num = num
            

    return min_even_num
  
def count(numbers, num) :
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    counter = 0
    for n in numbers:
        if n == num:
            counter += 1

    return counter

def sumOfTwoExists(numbers, sum):
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """ 
    exist = False
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] +  numbers[j] == sum:
                exist = True

    return exist


# print calls for testing the above functions
#print(indexOf([10, 20, 30, 20, -1],20))
#print(count([10, 20, 30, 20, -1],20))
#print(min_even([-10001, 10, 20, 8, 2]))
#print(sumOfTwoExists([1, -1, 40, 50, 0], 42))