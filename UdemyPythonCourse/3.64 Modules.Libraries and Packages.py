correct_password = "python123" # set up variable to hold password
name = input("Enter name: ") # set up variable to hold name passed from input from user
password = input("Enter password: ") # set up variable to hold password passed from input from user
 

while correct_password != password: # create loop that is FALSE until password passed == stored...
                                    # 'current_password'
    password = input("Wrong password! Enter again: ") # if while loop conditional is FALSE then...
                                                       # ask user for password again

 # print("Hi", name, "you are Logged in!") # once correct_password == password conditional becomes...
                                        # TRUE and code drops in to the print statement that...
                                        # concatonates text with variable 'name'
# print("Hi %s you are Logged in!" % name) # the %s is string formatting
message = "Hi %s you are Logged in!" % name
print(message)

# The string formatting helps keep the output 'clean' Look what happens if the original format...
# using the concatenation is used with storing the text as a variable...
message = ("Hi", name,  "you are Logged in!")
print(message)

# The text is treated as a TUPLE and printed as such ('Hi', 'Andy', 'you are Logged in!')
