from itertools import cycle


def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result


lst = [10, 2, 16]
iterations = 5
result = infinite(lst, iterations)
print(result)
