def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
  
    word_list = wrapper.wrap(text=string)
    st = ""
    for i in word_list:
        st +=  i + '\n'
    return st
