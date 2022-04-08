





user_balance = int(input("How much do you want to play with? ( must be an " 
               "integer between 1 and 10)  $"))


while not 1 <= user_balance <= 10:
    print("try again. Please enter a number between 1 and 10")

    user_balance = int(input("How much do you want to play with $"))

print(f"you are playing with${user_balance}")
