import itertools
k = 0
a = list(itertools.product("атом", repeat = 6))
for x in a:
  if x.count("м") == 1:
   k += 1
   print(k)
