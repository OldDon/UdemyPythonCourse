#myfile = open("myfile.txt", "w")
#myfile.write("SomethingElse")
#myfile.close()
#myfile.open("myfile.txt", "a")
#myfile.write("EvenMoreStuff")
#myfile.close()

with open("example.txt", "w") as myfile:
    myfile.write("Something new")