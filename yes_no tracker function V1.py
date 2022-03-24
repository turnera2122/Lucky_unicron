




# function
def yes_no(question_text):
    while true:

        # ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes program continues
        if answer == 'yes' or answer == 'y':
            answer = "yes"
            return answer
    # if user says no show instructions
    elif answer == 'no' or answer == 'n':
        answer = "No"
        return answer


    # othwerwise show error
    else:
        print("please answer 'yes's or 'no'")


# main routine
question = yes_no("have you played the game before? ")
print(f"your entered '{question}'")

