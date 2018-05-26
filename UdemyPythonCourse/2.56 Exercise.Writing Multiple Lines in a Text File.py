numbers = [1, 2, 3]

myfile = open("Numbers.txt", "w")
for i in numbers:
    #str(i) = i
    #myfile.write(\n)
    myfile.write(str(i) + "\n")
myfile.close()