# Write your solution here
from random import randint, choice

def roll(die: str):
    a = [3,3,3,3,3,6]
    b = [2,2,2,5,5,5]
    c = [1,4,4,4,4,4]

    if die == 'A':
        die_to_roll = a
    elif die == 'B':
        die_to_roll = b
    elif die == 'C':
        die_to_roll = c
    
    return choice(die_to_roll)

def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    draws = 0
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            die1_wins += 1
        elif roll2 > roll1:
            die2_wins += 1
        else:
            draws += 1

    return (die1_wins, die2_wins, draws)

##print(play('A','B',15))