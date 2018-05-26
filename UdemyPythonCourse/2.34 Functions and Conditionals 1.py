def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    #elif type(mystring) == float:
    #    return "Sorry, no floats :("
    else:
        return len(mystring)

input(string_length(mystring))

