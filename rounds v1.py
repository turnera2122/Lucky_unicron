""" component 4 - game mechanics and looping v1"""


import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# testing loop to generate 5 tokens
while play_again != 'x':
    rounds_played += 1  # keep track of rounds
    number = random.randint(6, 36)  # can only be a donkey

    # adjust balance
    # if the random number is between 1 and 5
    # user get a unicorn (add $4 to balance)
    if 1 <= number   <= 5:
        token = "unicorn"
        balance += 4

        # if the random number is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    #in all other cases the token must be a horse or a zebra
    #(subtract $0.50 from balance in either case)
    else:
         # if the number is even set the token to zero
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

             # otherwise, set the token to horse
        else:
            token = "horse"
            balance -= .5

    # output
    print(f"round {rounds_played}. Token: {token}. Balance ${balance:.2f}")

    if balance < 1:
        print("\nsorry but you have run out of money")
        play_again = 'x'
    else:
        play_again = input(f"\nDo you want to play another round?\n<enter> to play "
                           "again or 'x' to exit ").lower()

        print()
        return balance


print("Thanks for playing")
print(f" You started with ${TEST_AMOUNT:.2f}")
print(f"And leave with ${balance:.2f}")
print("\\Good bye ")

