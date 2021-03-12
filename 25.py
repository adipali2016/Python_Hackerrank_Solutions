def solve(s):
    t = s.split()
    text = ""
    l = list()
    for i in t:
        l.append(i.capitalize())
        #print("Done")
    j = 0
    i = 0
    #print(l)
    while i < len(s):
        if s[i].isalnum():
            text += l[j]
            i += len(l[j])
            j += 1
           # print("added if")
            continue
        else:
            text += s[i]
            #print("added else")
        i += 1         
    return text

