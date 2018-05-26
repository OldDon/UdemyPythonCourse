# Program to convert Celcius to Farenheit....
# Test for lowest possible temperature that physical matter can reach....
# That temperature is -273.15 degrees Celcius

def cel_to_fahr(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9/5 + 32
    return f

print(cel_to_fahr(-273.4))