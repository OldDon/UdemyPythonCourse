name = "Dave"
age = 50
accurate_age = 49+11/12


print("Hello %s is %d years old. Or better yet, %f years old." % (name, age, accurate_age)) # %s format string
                                                                                            # %d format integer
                                                                                            # %f format float

print("Hello %s is %d years old. Or better yet, %.2f years old." % (name, age, accurate_age))# %s format string
                                                                                            # %d format integer
                                                                                            # %.2f format float to 2 decimal places
print("Hello %s is currently %d years old. In ten years time will be %.2f" % (name, age, accurate_age + 10))# %s format string


data = ("Dave", "Elliott", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)