file = open("fruits.txt", "r")
content = file.read()
file.close()
print(content)

# My solution worked the same way
# I used descriptive variable names but the result
# was the same. See below for code:
#fruitList = open("/Users/davey/source/repos/UdemyPythonCourse/UdemyPythonCourse/fruits.txt")
#fruitListContent = fruitList.read()
#fruitList.close()
#fruitListContent.splitlines()
#print(fruitListContent)