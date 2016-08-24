# Guess the number game with a dice roller.
from random import randint
from time import sleep

def get_user_guess():
    user_guess = int(raw_input("Ay slim. Give me a number. Any number. Just guess. > "))
    return user_guess
  
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides * 2
    print "The maximum value is " + str(max_val)
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print "That number is too high."
        return 
    else:
        print "Rolling..."
        sleep(2)
        print "The first roll is %d" % first_roll
        sleep(1)
        print "The second roll is %d" % second_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "The total roll is:" + str(total_roll)
        print "Result..."
        sleep(1)
        
        if user_guess > total_roll:
            print "You won congrats!"
            return
        
        elif user_guess < total_roll:
            print "You lost!"
            return
roll_dice(6)
