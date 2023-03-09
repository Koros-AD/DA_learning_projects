import math

r = float(input("Enter circle radius: "))
while r <= 0:
    print("Enter a valid radius.")
    r = float(input("Enter circle radius: "))
def findarea(r):
    area = math.pi * r ** 2
    return area
area = findarea(r)
print(f"Circle area = {area:.2f}")


