# code for 2.53 Writing Text to a File lesson

myfile = open("employees.txt", "a+") # "a+" is for Append PLUS (Add further to the file but can Read AND Write to the file)

myfile.seek(0)
myfile.read()
#print(len(myfile))

