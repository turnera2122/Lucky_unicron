


import random

tokens = ["unicorn," "horse","donkey", "zebra"]

# testing loop to generate 8 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t') # caqn wrap output making it easier to take a screenshot
