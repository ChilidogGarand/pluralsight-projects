import random
roll = random.randint(1,6)
guess = int(input('Guess the dice roll (D6):\n'))
if guess == roll:
    print("Holy shit, how'd you do that? The roll was indeed " + str(roll))
else:
    print("You actually suck, the correct answer is " + str(roll) + ".")