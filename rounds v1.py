"""Component 4 - game mechanics and looping v1
"""

import random

# Main Routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1 # keep track of rounds
    number = random.randint(6,36) # Can only be a donkey

     # adjust balance
    # If the random number is between 1 and 5
    # User gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # If the number is between 6 and 36
    # User gets a donkey (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    # In all other cases, the token must be a horse or zebra
    # (subtract $0.50 from the balance in either case)
    else:
        # if the number is even, set the token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

        # otherwise, set the token to horse
        else:
            token = "horse"
            balance -= 0.5
    # output
    print(f"Round {rounds_played}, Token: {token}, Balance ${balance:.2f}")
    if balance < 1:
        print()
        print("Sorry but you have run out of money")
        play_again = "x"
    else:
        print()
        play_again = input("Do you want to play another round\n<enter> to play again or 'X' to exit").lower()
        print()

print(f"Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print(f"Goodbye!")
