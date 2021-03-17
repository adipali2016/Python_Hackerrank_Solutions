n = int(input())
st1 = set(map(int, input().split()))
n = int(input())
st2 = set(map(int, input().split()))
ans = list(st1.symmetric_difference(st2))
ans.sort()
for i in ans:
    print(i)