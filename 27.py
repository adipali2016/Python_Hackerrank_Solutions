def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        text = ''
        for j in string[i:k+i]:
            if j not in text:
                text += j
        print(text)
