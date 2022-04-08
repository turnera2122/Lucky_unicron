


import random

tokens = ["unicorn," "horse","donkey", "zebra"]
balance = 100

# testing loop to generate 8 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t') # can wrap output making it easier to take a screenshot

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
            balance -= 1
    else:
        balance -= 50

    # output
    print(f"Token: {token}, balance: ${balance}")
