def int_reverse(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return reversed_num


def create_palindromic_list(start, stop):
    palindromic_numbers = []

    if start <= stop:
        step = 1
    else:
        step = -1

    for num in range(start, stop + step, step):
        if num == int_reverse(num):
            palindromic_numbers.append(num)

    return palindromic_numbers



print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 