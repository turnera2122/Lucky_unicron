"""" component 4 game mechanics and looping """""






import random

    # main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(1, 100)

    # adjust balance
    # if the number is between 1 and 5
    # user gets a unicorn (add $4 to balance
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

            # if the random number is between 6 and 36
            # user gets a donkey (subtract $1 from the balance)
    elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

            # in all other cases the token must be a horse or a zebra
            # (subtract $0.50 from the balance in either case)
    else:
        # if the number is even, set the token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

             # otherwise, set token to horse
        else:
            token = "horse"
            balance -= .5

# output
print(f"round {rounds_played}. Token: {token}, balance: ${balance:. 2f}")
if balance <  1:





