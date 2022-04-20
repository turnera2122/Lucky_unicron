""" component 5 - statement formatter v2"""




# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"



# main routine
print(formatter("-", "Welcome to the lucky unicorn game"))
print()
print(formatter("!", "Congradulations, you got a unicorn"))
print()
print(formatter("*","Goodbye"))






