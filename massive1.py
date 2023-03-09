from collections import Counter
array = [2, 7, 18, 7,23, 9, 12, 3,30, 6, 16, 21, 3, 28,7]
count=[]
for key, value in Counter(array).items():
    if value == 3:
        count.append(key)
print(count)
