def exist(num: int, l: list[int]) -> bool:

    i: int = 0
    num_exist: bool = False

    while i < len(l) and not num_exist:
        if num == l[i]:
            num_exist = True
        i+=1
        
    return num_exist

def max_number(num: int, l: list[int]) -> int | None:
    i: int = 0
    result: int | None = None

    while i < len(l) and result is None:
        if num + l[i] == 0:
            result = l[i] if num < 0 else num
        i += 1

    return result


def intersection (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with integer numbers existing in both input lists
    Examples: intersection([1, 2, 3], [4, 3, 1])=> [1, 3]
    intersection([1, 2, 3], [4, 5, 6])=> [];
    """
    array: list[int] = []

    for num in l1:
        if exist(num, l2):
            array.append(num)

    return array
        

def union (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numbers existing  in ether list or both
    Result list shouldn't contain repeated numbers
    Examples: union([1, 2, 3], [4, 3, 1])=> [1, 2, 3, 4]
    union([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """

    array: list[int] = []

    for num in l1:
            array.append(num)

    for num in l2:
        if not exist(num, array):
            array.append(num)

    return array


def difference (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numbers existing  in l1
    but non-existing  l2
    Examples: difference([1, 2, 3], [4, 3, 1])=> [2]
    difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3]
    """
    array: list[int] = []

    for num in l1:
        if not exist(num, l2):
            array.append(num)

    return array

def symmetric_difference (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numbers existing  in either list but not in both
    Examples: symmetric_difference([1, 2, 3], [4, 3, 1])=> [2, 4]
    symmetric_difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """  
    array: list[int] = []

    for num in l1:
        if not exist(num, l2):
            array.append(num)

    for num in l2:
        if not exist(num, l1):
            array.append(num)

    return array

def remove_positive_greater_or_negative_less(numbers:list[int],\
                         positive_lim: int, negative_lim: int) -> list[int]:
    """
    numbers - list with integer numbers
    returns new list containing all numbers from the input list
    except the positive ones greater than 'positive_lim' and the negative ones
    less than 'negative_lim'
    Example: remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)
    => [1, 2, -3, 10]
    """  

    array: list[int] = []

    for num in numbers:
        if negative_lim <= num <= positive_lim:
            array.append(num)

    return array 

def max_with_negative_duplicate (numbers:list[int]) -> int:
    """
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate 
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """

    max_numbers: list[int] = []

    for num in numbers:
        n = max_number(num, numbers)
        if n is not None and not exist(n, max_numbers):
            max_numbers.append(n)


    max: int = -1

    for num in max_numbers:
        if(num > max):
            max = num

    return max

