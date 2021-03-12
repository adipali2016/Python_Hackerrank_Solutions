def minion_game(string):
    # your code goes here
    kevin = 0 # Vowel
    stuart = 0 # Consonant
    string = string.upper()
    l = ''
    for i in range(0, len(string)):
        if string[i] in 'AEIOU':
            kevin += len(string)-i
        else :
            stuart += len(string)-i

    if stuart > kevin:
        print(f'Stuart {stuart}')

    elif kevin > stuart:
        print(f'Kevin {kevin}')

    else:
        print('Draw')
