#Itertools code that calculates how many codewords containing only 5 letters (А,Т,О,М) could be created, M can be used only once,
#others can be repeated or not used at all.
import itertools
k = 0
a = list(itertools.product("атом", repeat = 6))
for x in a:
  if x.count("м") == 1:
   k += 1
   print(k)
