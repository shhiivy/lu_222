# Asker user have they played before
show_instructions = input("Have you played Lucky Unicorn before?").lower()

# If yes, output 'program continues'
if show_instructions.lower() == "yes":
    print("Program continues")

elif show_instructions.lower() == "Y":
    print("Program continues")

# If no output 'display instructions'
elif show_instructions.lower() == "No":
    print("Display instructions")

elif show_instructions.lower() == "N":
    print("Display instructions")

else:
    print("Please enter yes or no")
