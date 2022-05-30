def staircase(n):

    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

print(staircase(5))