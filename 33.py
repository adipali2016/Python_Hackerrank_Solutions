t = int(input())
for i in range(0, t):
    ans = True
    n1 = int(input())
    a = input().split()
    n2 = int(input())
    b = input().split()
    for i in a:
        if i not in b:
            ans = False
            break
    print(ans)