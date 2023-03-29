from fractions import Fraction

def fractionate(amount: int):
    return_list = []
    for i in range(amount):
        fraction = Fraction(1,amount)
        return_list.append(fraction)
    return return_list

