
# Functions go here ...
def yes_no(question):
    valid = False
    while not valid:
        # Ask user for input
        response = input(question).lower().strip()
        # if no the instruction are displayed
        if response == "yes" or response == "y":
            response = "yes"
            return response
        # if yes the program continues
        if response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter yes or no")


# Instructions function on how to play
def instructions ():
    print("**** How To Play ****")
    print()
    print("The rule of the game go here")
    print()
    return ""


# Main routine goes here ...
played_before = yes_no("Have you ever played the game before? ")

# if user hasn't played display instructions
if played_before == "no":
    instructions()
    print("Program Continues")
else:
    print("Program continues")


