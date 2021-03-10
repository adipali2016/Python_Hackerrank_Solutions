def is_leap(year):
    leap = False
    
    sub = year%100
    if (sub)%4 == 0:
        leap = True
        if sub == 0 and year%400 != 0:
            leap = False
 
    # Write your logic here
    
    return leap