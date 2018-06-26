def fatorialWhile(n):
    i = 1
    n_fat = 1

    while i <= n:
        n_fat = n_fat * i
        i = i + 1

    return n_fat

def fatorialFor(n):
    n_fat = 1

    for i in range(2, n + 1):
        n_fat = n_fat * i

    return n_fat


print(fatorialWhile(0))
print(fatorialWhile(1))
print(fatorialWhile(5))
print(fatorialFor(0))
print(fatorialFor(1))
print(fatorialFor(5))