# Functions go here
def num_checker(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))

            # If the amount is too low/ too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine go here
how_much = num_checker("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
