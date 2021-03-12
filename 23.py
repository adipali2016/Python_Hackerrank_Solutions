def print_formatted(number):
    # your code goes here
    bt = bin(number).replace("0b","")
    l = str(bt).__len__()
    for i in range(1,number+1):
        o = oct(i).replace("0o","")
        h = hex(i).replace("0x","")
        h2 = ""
        for a in h:
            if a.isalpha():
                a = a.upper()
            h2 += a
        b = bin(i).replace("0b","")
        print(str(i).rjust(l), end=' ')
        print(str(o).rjust(l), end=' ')
        print(str(h2).rjust(l), end=' ')
        print(str(b).rjust(l))

