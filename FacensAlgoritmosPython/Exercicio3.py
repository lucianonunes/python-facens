def intervalSum(x,y):
    sum = 0
    if x > y:
        z = x
        x = y
        y = z

    for i in range(x, y + 1):
        sum = sum + i

    return sum

print(intervalSum(9, 9))