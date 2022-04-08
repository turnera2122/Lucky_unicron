






def num_check(question, low, high):
    error =  "that was not a valid input\n" \
            "please enter a number between {} and {}\n". format(low, high)

    # keep asking until a valid input (1-10)  is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine
user_balance = num_check("how much would you like to play with? $", 1, 10)
print(f"you are playing with {user_balance}")
