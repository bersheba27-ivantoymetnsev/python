def binary_search(numbers: list[int], num:int)->int:
    """
    O[logN]
    numbers: sorted list
    num: being searched number
    returns an inedex of the first occurrence at which "num" resides in "numbers" or
    negative number as -(index_sort + 1) where index_sort is the index where "num" should have been in "numbers"
    for example: numbers: list[int] = [10, 10, 10, 20, 20, 20, 30, 30, 40]
    binary_search(numbers, 20) -> 3 (not 4),binary_search(numbers, 15) -> -4 (not -1),
    binary_search(numbers, 45) -> -10
    """
    left: int = 0
    right: int = len(numbers) - 1

    while left <= right:
        middle: int = (left + right) // 2

        if numbers[middle] < num:
            left = middle + 1
        else:
             right = middle - 1

    if left < len(numbers) and numbers[left] == num:
            return left

    return -(left + 1)


def insert_sorted(numbers: list[int], num: int) -> None:
    """
    numbers: sorted list
    num: inserted number
    inserts "num" keeping "numbers" sorted
    For example: numbers: list[int] = [10, 10, 10, 20, 20, 20, 30, 30, 40]
    after insert_sorted (numbers, 19) the list will contain [10, 10, 10, 19, 20, 20, 20, 30, 30, 40]
    after insert_sorted (numbers, 20) (initial list) the list will contain [10, 10, 10, 20, 20, 20, 20, 30, 30, 40]

    """
    start: int = 0
    end: int = len(numbers) - 1

    while start < end and numbers[start] < num:
        start+=1

    numbers[start:start] = [num]
