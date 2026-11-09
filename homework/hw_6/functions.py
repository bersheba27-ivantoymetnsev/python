def max_with_negative_duplicate (numbers:list[int]) -> int:
    num_set = set(numbers)
    max_number = -1

    for num in numbers:
        if num > 0 and -num in num_set:
            max_number = max(max_number, num)
    
    return max_number




def sumOfTwoExists(numbers:list[int], sum: int):
    set_nums = set()

    for num in numbers:

        target: int = sum - num
        if target in set_nums:
            return True

        set_nums.add(num)

    return False


def bubble_sort(numbers: list[int]) -> None:
    numbers_length: int = len(numbers)

    while numbers_length > 0:
        no_swaps = True
        j: int = 0

        while j < numbers_length - 1:
            if numbers[j] > numbers[j + 1]:
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
                no_swaps = False

            j += 1

        if no_swaps:
            break

        numbers_length -= 1

def remove_duplicates(numbers: list[int])->list[int] :
    set_nums: set[int] = set()
    new_array: list[int] = []

    for num in numbers:
        if num not in set_nums:
            set_nums.add(num)
            new_array.append(num)        

    return new_array



