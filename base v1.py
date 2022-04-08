




# function
def yes_no(question_text):
    while True:

        # ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes program continues
        if answer == "yes" or answer == "y":
            answer = "yes"
            return answer

         # if user says no show instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

    # othwerwise show error
    else:
        print("please answer 'yes's or 'no'")

def instructions():

    print("**** how to play ****")
    print()
    print("the rules of the game")
    print()
    print("program continues")
    print()
# main routine


 #number checker function
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


played_before = yes_no("have you played the game before? ")

if played_before == "No":
    instructions()



#ask user how much they want to play with
user_balance = num_check("how much would you like to play with? $", 1, 10)
print(f"you are playing with {user_balance}")
