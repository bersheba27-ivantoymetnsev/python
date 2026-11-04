def min_max_average(array: list[int]) -> tuple[int, int, float]:
    array_length: int = len(array)
    total:int = 0 
    
    for num in array:
        total += num
        
    average = float(total / array_length)

    min_num: int = min(array)
    max_num: int = max(array)

    return min_num, max_num, average

    
def move_max_to_end(array: list[int]) ->  None:


    for index in range(len(array) - 1) :
        if(array[index] > array[index + 1]):
            array[index + 1], array[index] = array[index], array[index + 1]

