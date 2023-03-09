import math
a=int(input("enter а "))
b=int(input("enter b "))
c=int(input("enter c "))
print(f'{a}x^2 + {b}x + {c}= 0')
def roots(a,b,c):
 D=(b**2)-(4*a*c)
 if D<0:
      print("no roots")
 if D==0:
      x=(-b+math.isqrt(D))/(2*a)
      print(f'x1={x}')
 if D>0:
      x1=(-b+math.sqrt(D))/(2*a)
      x2=(-b-math.sqrt(D))/(2*a)
      print(f'x1={x1},x2={x2}')
roots(a,b,c)





