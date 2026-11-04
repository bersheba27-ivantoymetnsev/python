import functions
numbers1: list[int] = [10, 5, 20, 8, 12]
numbers2: list[int] = [-10, -5, -20, -8, -12]
numbers3: list[int] = [-15, 0, 25, -5, 10]
numbers4: list[int] = [7, 7, 7, 7, 7]
numbers5: list[int] = [42]
numbers6: list[int] = [3, 9, 3, 15, 2, 8, 2]

for numbers in [numbers1, numbers2, numbers3, numbers4, numbers5, numbers6]:
    min_num, max_num, average_num = functions.min_max_average(numbers)
    print(min_num, max_num, average_num)

functions.move_max_to_end(numbers6)
print(numbers6)