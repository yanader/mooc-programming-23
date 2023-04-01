class  NumberStats:

    def __init__(self):
        self.numbers = 0
        self.number_list = []

    def add_number(self, number:int):
        self.numbers += 1
        self.number_list.append(number)

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return sum(self.number_list)
    
    def average(self):
        if self.count_numbers() == 0:
            return 0.0
        else:
            return float(self.get_sum()) / float(self.count_numbers())

print('Please type in integer numbers:')
numbers_stats = NumberStats()
numbers_even = NumberStats()
numbers_odd = NumberStats()
while True:
    entered_number = int(input())
    if entered_number == -1:
        break
    numbers_stats.add_number(entered_number)
    if entered_number % 2 == 0:
        numbers_even.add_number(entered_number)
    else:
        numbers_odd.add_number(entered_number)

print(f'Sum of numbers: {numbers_stats.get_sum()}')
print(f'Mean of numbers: {numbers_stats.average()}')
print(f'Sum of even numbers: {numbers_even.get_sum()}')
print(f'Sum of odd numbers: {numbers_odd.get_sum()}')