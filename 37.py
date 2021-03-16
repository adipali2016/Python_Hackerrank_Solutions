from collections import defaultdict

inp = list(map(int, input().split()))
d = defaultdict(list)
for i in range(1,inp[0]+1):
    n = input()
    d[n].append(i)
for i in range(1,inp[1]+1):
    j = input()
    if j in d.keys():
        for v in d[j]:
            print(v, end=" ")
        print()
    else:
        print(-1)        