# The program is a function infinite(lst, tries) that will iterate over the elements of the list lst (integers) a specified number of times (tries) cyclically. 
# One time is one element of the list.
# After the last value of the sequence is displayed, the cycle starts again.

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
