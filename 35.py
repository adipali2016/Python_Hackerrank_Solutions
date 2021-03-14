import numpy as np

inp = list(input().split())
inp2 = list(map(int, inp))

arr = np.array(inp2)
arr = arr.reshape(3,3)

print(arr)