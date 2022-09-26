import random

# Main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 10):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5,
    # The user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # If the random # is between 6 and 36,
    # The user gets a donkey (subtract 1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # The token is either a horse or zebra...
    # In the case, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen
        # Item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # Otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

# output
    print("You got a {}. Your balance is "
          "${:.2F}".format(chosen, balance))
print()
print("Starting Balance: ${:.2F}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
