# WRITE YOUR SOLUTION HERE:

class SimpleDate:

    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __lt__(self, another:"SimpleDate"):
        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day < another.day:
            return True
        else:
            return False

    def __gt__(self, another:"SimpleDate"):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day > another.day:
            return True
        else:
            return False

    def __eq__(self, another:"SimpleDate"):
        return self.year == another.year and self.month == another.month and self.day == another.day

    def __ne__(self, another:"SimpleDate"):
        return self.year != another.year or self.month != another.month or self.day != another.day

    def __add__(self,days_to_add:int):
        day = self.day + days_to_add
        month = self.month
        year = self.year
        if day > 30:
            month = month + day // 30
            day = day % 30
        if month > 12:
            year = year + month // 12
            month = month % 12
        return SimpleDate(day, month, year)

    def __sub__(self, another:"SimpleDate"):
        selfdate = (self.year * 360) + (self.month * 30) + self.day
        anotherdate = (another.year * 360) + (another.month * 30) + another.day
        return abs(selfdate - anotherdate)



if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)