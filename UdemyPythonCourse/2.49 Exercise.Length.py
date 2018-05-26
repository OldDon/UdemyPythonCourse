#fruitList = open("/Users/davey/source/repos/UdemyPythonCourse/UdemyPythonCourse/fruits.txt")
#fruitListContent = fruitList.read()
#fruitList.close()
#fruitListContent = fruitListContent.splitlines()
#for i in fruitListContent:
#    print(len(i))

fruitList = open("/Users/davey/source/repos/UdemyPythonCourse/UdemyPythonCourse/fruits.txt")
fruitListContent = fruitList.readlines()
fruitListContent = [line.strip() for line in fruitListContent]
fruitList.close()

for i in fruitListContent:
    print(len(i))

#myfile = open("/Users/davey/source/repos/UdemyPythonCourse/UdemyPythonCourse/fruits.txt")
#content = myfile.read()
#myfile.close()
#content = content.splitlines()
#for i in content:
#     print(len(i))
   
    

