# 2.29 Custom Functions with Multiple Parameters
#def converter(original_unit, coefficient):
#    return(original_unit * coefficient)

#print(converter(10,0.3048))

def converter(original_unit, coefficient = 0.3048):
    return original_unit* coefficient

print(converter(10, 0.62))