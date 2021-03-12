num = input()
lst = list(num.split())

n = int(lst[0])
m = int(lst[1])

for i in range(0,n):
    if i == int(n/2):
        print('WELCOME'.center(m,'-'))

    elif i < int(n/2):
        print(('.|.'*(2*i+1)).center(m,'-'))

    elif i > int(n/2):
        print(('.|.'*(2*(n-i)-1)).center(m,'-'))    
