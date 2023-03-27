# The code generates random array and finds the greatest most common element in array
from collections import Counter
import random
a = []
#generating random array from input
n=(int(input("n= ")))
for i in range (n):
     x=random.randint(1,100)
     a.append(x)
#finding the most common number
def most_common_element(lst):
    counter = Counter(lst)
    most_common = counter.most_common()
    max_count = most_common[0][1]
    result = most_common[0][0]
    for elem, count in most_common:
        if count == max_count and elem > result:   # checking if the number is the greatest
            result = elem
    return result
print(a)
print(most_common_element(a))
