from collections import Counter

inp = int(input())
lt = input().split()
lt = list(map(int, lt))
cnt = Counter(lt)
n = int(input())
sum=0
for i in range(n):
    ip = input().split()
    ip = list(map(int, ip))
    if ip[0] in cnt.keys() and cnt[ip[0]]!=0:
        sum = sum + ip[1]
        cnt[ip[0]] = cnt[ip[0]]-1

print(sum)