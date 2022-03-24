
view_instructions = ""
while view_instructions != "x":

    # Ask the user if they have played the game before
    view_instructions = input("have you played this game before?: ").lower()

    # If they say yes program continues without viewing instructions
    if view_instructions == "yes" or view_instructions ==  "y":
        print("program continues")

    # if user says no show instructions
    elif view_instructions == "no" or view_instructions == "n":
        print("showing instructions")

    # otherwise show error
    else:
        print("invalid input please answer either 'yes' or 'no'")

    print(f"you entered '{view_instructions}'")
