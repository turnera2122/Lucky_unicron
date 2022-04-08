



# main routine
error = "That was nat a valid input\n"
user_balance = 0

# keep asking till a valid iinput (1-10) is entered
while not 1 <= user_balance <=10 :
    try:
        # ask for amount
        user_balance = int(input("please enter a whole number between 1 and 10"
                                 "\nHow much would you like to play with? $"))
        print()

    except ValueError:
        print(error)

print(f"You are with ${user_balance}")


