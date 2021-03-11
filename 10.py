if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    lst = list()
    for i in arr:
        if i not in lst:
            lst.append(i)
    lst.sort(reverse = True)
    print(lst[1]) 
