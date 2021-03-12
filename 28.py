from itertools import product

inp1 = list(input().split())
inp1 = list(map(int,inp1))
inp2 = list(input().split())
inp2 = list(map(int, inp2))
prd = list(product(inp1, inp2))

for (i,j) in prd:
    print(f"({i}, {j})", end=' ')
