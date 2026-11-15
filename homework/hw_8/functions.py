from collections.abc import Callable, Sequence


def bubble_sorted(items: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
      in accorgance with key function-converter like standard Python sorting
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
          default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers
                 bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=
    """
    result = list(items)
    if key is None:
        key = lambda x: x

    for i in range(len(result) - 1):
        swapped = False
        for j in range(len(result) - 1 - i):
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


def even_asc_odd_desc(numbers: list[int])->list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """
    evens = []
    odds = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    evens.sort()
    odds.sort(reverse=True)
    return evens + odds


def  merge(part1: Sequence[object], part2: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """

    if key is None:
        key = lambda x: x

    result = []
    i = 0
    j = 0

    while i < len(part1) and j < len(part2):
        if key(part1[i]) <= key(part2[j]):
            result.append(part1[i])
            i += 1
        else:
            result.append(part2[j])
            j += 1

    result.extend(part1[i:])
    result.extend(part2[j:])
    return result
