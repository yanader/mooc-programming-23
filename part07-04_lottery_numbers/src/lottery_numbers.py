from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    balls_in_machine = list(range(lower,upper+1))
    drawn_numbers = sample(balls_in_machine, amount)

    return sorted(drawn_numbers)
