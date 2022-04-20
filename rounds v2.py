"""component 4 game mechanics and looping"""






import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# testing loop to generate 5 tokens
while play_again != 'x':
    rounds_played +- 1  # keep track of rounds
    number = random.randint(1, 100)

    # adjust balance
    # if the random number is between 1 and 5
    # user gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

        # if the random number is between 6 and 36
        # user gets a donkey ($1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

     # in all other cases the token must be a horse or a zebra
     # (subtract $0.50 from the balance in either case)
    else:
        # if the number is even, set the token zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

        # otherwise, set the token to horse
        else:
            token = "horse"
            balance -= .5

            # output
            print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
            if balance < 1:
                print("\n sorry but you have run out of money")
                play_again = "x"
            else:
                play_again = input ("\nDo you want to play another round?\n<enter> "
                                    "again or 'x' to exit ").lower()
            print()

            print("Thanks for playing")
            print(f"You started with ${TEST_AMOUNT:.2f}")
            print(f"and leave with ${balance:.2f}")
            print("Goodbye")



