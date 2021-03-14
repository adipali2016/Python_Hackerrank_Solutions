import cmath
import math

inp = input()
c = complex(inp)

r = math.sqrt((c.real**2)+(c.imag**2)) 
print(r)
print(cmath.phase(c))
