# yes no function assesses input for yes/no
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If yes, out 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no, output 'display instructions'
        if response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")

# Main routine goes here ...
show_instructions = yes_no("Have you ever played the game before? ")
print("You chose {}".strip(show_instructions))
