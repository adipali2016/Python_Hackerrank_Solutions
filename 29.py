from itertools import permutations

inp, num = input().split()
num = int(num)
ans = list(permutations(inp,num))
ans.sort()
str=''
for a in ans:
    print(str.join(a))
        