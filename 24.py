def print_rangoli(size):
    # your code goes here
    x = list()
    l = size
    for i in range(0,l):
        s = ""
        t = 2*i+1
        if l <= size:
            for j in range(0,t):
                if j <= (t/2):
                    s += chr(ord('a')+(l-j-1)) + '-'
                else:
                    s += chr(ord('a')+(l-int(t))+j) + '-'    
                    
        s = s.center(4*l-3,'-')
        x.append(s[:(4*l-3)])

    for i in range(0,(l*2-1)):
        if i < l:
            print(x[i])
        else:
            print(x[l*2-2-i]) 
    

