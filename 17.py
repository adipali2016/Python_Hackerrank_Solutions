def mutate_string(string, position, character):
    text = string[:position]+character+string[position+1:]
    return text