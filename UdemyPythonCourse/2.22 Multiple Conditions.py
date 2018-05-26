while True:

    user_input = float(input("Enter number: "))
    if user_input > 100:
        print("Greater than ")
    elif user_input == 100:
        print("Equals 100")
    elif user_input == 99:
        print("CONGRATS :) YOU'VE PICKED THE BONUS NUMBER!!!!")
    else:
        print("Smaller than ")



