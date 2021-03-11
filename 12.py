if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N):
        inp = input()
        lst = inp.split()
        if lst[0] == 'insert':
            l.insert(int(lst[1]), int(lst[2]))
        elif lst[0] == 'print':
            print(l)
        elif lst[0] == 'remove':
            l.remove(int(lst[1]))
        elif lst[0] == 'append':
            l.append(int(lst[1]))
        elif lst[0] == 'sort':
            l.sort()
        elif lst[0] == 'pop':
            l.pop()
        elif lst[0] == 'reverse':
            l.reverse()
