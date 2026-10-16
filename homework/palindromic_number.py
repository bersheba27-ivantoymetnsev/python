def int_reverse(num):

    reversed_int = str(num)[::-1]
    return reversed_int


def create_palindromic_list(start, stop) :

    palindromic_numbers = []
    reverse_result = False

    if start > stop:
        temp = stop
        stop = start
        start = temp
        reverse_result = True
    
    while start <= stop:
        normal_num = start
        reversed_int = int(int_reverse(normal_num))
        if normal_num == reversed_int:
            palindromic_numbers.append(reversed_int)
        start += 1

    
    if reverse_result:
      palindromic_numbers.reverse()
      

    return palindromic_numbers


print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 