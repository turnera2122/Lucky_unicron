


error = "please enter a whole between 1 and 10\n"
valid = False

# keep asking until a valid amount (1-10) is entered\
while not valid:
    try:
        # ask for amount
        user_balance = int(input("How much would you like to play with? $"))

        # check fi the amount is too high/low
        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance}")
            valid = True
        else:
            print (error)

    except ValueError:
        print(error)
