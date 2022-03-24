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
            print("please answer 'yes' or 'no'")

# function to show instructions
def instructions():
    print("**** how to play ****")
    print()
    print("the rules of the game")
    print()
    print("program continues")
    print()
# main routine
played_before = yes_no("have you played the game before? ")

if played_before == "No":
    instructions()
else:
    print("program continues")
