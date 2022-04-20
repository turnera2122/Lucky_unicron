"""LU base component - based on 00_LU_base_v2
Adding instructions to instructions, and further text decoration
"""

import random


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "y" or answer == "yes":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "n" or answer == "no":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer with 'yes' or 'no'")


# Function to display instructions
def instructions():
    print(formatter("*", "How to Play"))
    print()
    print("Choose a starting amount to play with, must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token which will be a horse, donkey, zebra, or unicorn")
    print()
    print("Each round costs $1 to play, but depending on your prize, you could win some money back. These are the payout amounts:\n"
          "Unicorn: +$5 (balance increases by $4)\n"
          "Horse: -$0.50\n"
          "Zebra: -$0.50\n"
          "Donkey: -$1\n")
    print("See if you can avoid donkeys, get the unicorns, and finish with more money than you started with!")

    print("*" * 50)
    print()


# Number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # keep asking until a valid amount (1-10) is entered
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


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1 # keep track of rounds
        print()
        print(formatter(".", f"Round {rounds_played}"))
        print()
        number = random.randint(1,100)

        # adjust balance
        # If the random number is between 1 and 5
        # User gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a Unicorn"))
            print()

        # If the number is between 6 and 36
        # User gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Bad luck, you got a donkey"))
            print()

        # In all other cases, the token must be a horse or zebra
        # (subtract $0.50 from the balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                balance -= 0.5
                print(formatter("Z", "You got a zebra"))
                print()

            # otherwise, set the token to horse
            else:
                balance -= 0.5
                print(formatter("H", "You got a horse"))
                print()

        # output
        print(f"Your balance is now ${balance:.2f}")
        if balance < 1:
            print()
            print("Sorry but you have run out of money")
            play_again = "x"
        else:
            print()
            play_again = input("Do you want to play another round\n<enter> to play again or 'X' to exit").lower()
    print()
    return(balance)


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine go here
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# Ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")
print("Press <enter> to start")

closing_balance = generate_token(starting_balance)
print(f"Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")

print(formatter("*", "Goodbye"))
