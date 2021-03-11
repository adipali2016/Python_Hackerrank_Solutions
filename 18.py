def count_substring(string, sub_string):
    count = 0
    x = 0
    while True:
        t = string.find(sub_string,x)
        if t == -1:
            break
        count += 1
        x = t+1    
        
    return count