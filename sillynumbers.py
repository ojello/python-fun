import random

# # Generates a random number between a given positive range.
r = random.randint(0, 100)
print(r)

score = 20
guess = int(input("Please guess a number!:"))
i = 0
if i < 10:
    while guess != r:
        guess = input("Please keep trying :):")
        score = score - 1
    i += 1
