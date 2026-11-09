import functions
#sumOfTwoExists
print(functions.sumOfTwoExists([1, -1, 40, 50, 0], 0))
print(functions.sumOfTwoExists([1, -1, 40, 50, 0], 42))
print(functions.sumOfTwoExists([0, -1, 2, -3, 1], -2))
#remove_duplicates
array_1: list[int] = [-1, 0, 100, -1, 20, 80, 20]
array_2: list[int] = [2, 4, 5, 9, 22, 4, 1, 15, 20]
array_3: list[int] = [-5, 17, 0, 4, 3, -5, 6, 7, 19]
print(functions.remove_duplicates(array_1))
print(functions.remove_duplicates(array_2))
print(functions.remove_duplicates(array_3))
#max_with_negative_duplicate
l1: list[int] = [-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]
l2: list[int] = [10, 20, -15, -11, 20]
l3: list[int] = [5, 6, 7, 8, 9, 10, -10, -5, 9]
print(functions.max_with_negative_duplicate(l1))
print(functions.max_with_negative_duplicate(l2))
print(functions.max_with_negative_duplicate(l3))
