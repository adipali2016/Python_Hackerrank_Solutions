import math

a,b = int(input()), int(input())

s = a/b
s = math.atan(s)
print(f'{round(math.degrees(s))}°')