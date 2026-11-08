
def bubble_sort(array: list[int]) -> None:
    no_swaps: bool
    array_length: int = len(array)

    while array_length > 0:
        no_swaps = True
        j: int = 0

        while j < array_length - 1:
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                no_swaps = False

            j += 1

        if no_swaps:
            break

        array_length -= 1



array_of_ints: list[int] = [29,15,1,44,2,3,5,19]
bubble_sort(array_of_ints)
print(array_of_ints)

