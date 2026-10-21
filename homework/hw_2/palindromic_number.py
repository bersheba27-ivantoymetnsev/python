def int_reverse(num):

    return int(str(num)[::-1])


def create_palindromic_list(start, stop):
    
    if start <= stop:
        step = 1
    else:
        step = -1

    palindromic_numbers = [num for num in range(start, stop + step, step) if num == int_reverse(num)]


    return palindromic_numbers



print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 
