def even_odd(numbers):
    numbers.sort()
    odd = []
    even = []

    for number in numbers:
        if(number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)

    ret = (even, odd)
    return ret


num=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_odd(num))