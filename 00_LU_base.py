import random
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
def instructions():
    print("**** How To Play ****")
    print()
    print("The rule of the game go here")
    print()
    print("""Welcome to Lucky Unicorn
Chose a starting amount, between $1 and $10.
Press <enter> to play.
Each round costs $1.
You will receive a Zebra, Horse, Donkey or Unicorn.
Depending on what you get you may win some money.
Unicorn: $5
Horse: $0.50
Zebra: $0.50
Donkey: Nothing
Good Luck!\n""")
    return ""


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


def statement_generator(statement, decoration):

    sides = decoration *3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")

print()


played_before = yes_no("Have you ever played the game before? ")

print()

if played_before == "no":
    instructions()

how_much = num_checker("How much would you like to play with? ", 0, 10)
print("You will be spending ${}".format(how_much))


print()


balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()


# Earnings and losses per token
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5,
    # The user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        statement_generator("You won a unicorn", "!")
        balance += 4

    # If the random # is between 6 and 36,
    # The user gets a donkey (subtract 1 from balance)
    elif 6 <= chosen_num <= 36:
        statement_generator("You received a donkey", "_")
        chosen = "donkey"
        balance -= 1

    # The token is either a horse or zebra...
    # In the case, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen
        # Item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            statement_generator("You received a horse", "+")

        # Otherwise set it to a zebra
        else:
            chosen = "zebra"
            statement_generator("You received a zebra", "=")
        balance -= 0.5

# output
    print("You got a {}. Your balance is "
          "${:.2F}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
         play_again = input("Press enter to play again"
                       "or 'xxx' to quit")

         print()

# The user final balance
print()
print("Final Balance: ${:.2f}".format(balance))
print()
# a thankyou message
statement_generator("Thank you for playing lucky unicorn", "@")
print()
