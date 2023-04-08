# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another:"Money"):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __ne__(self, another:"Money"):
        return self.__euros != another.__euros or self.__cents != another.__cents
    
    def __lt__(self, another:"Money"):
        return self.__euros * 100 + self.__cents < another.__euros * 100 + another.__cents
    
    def __gt__(self, another:"Money"):
        return self.__euros * 100 + self.__cents > another.__euros * 100 + another.__cents

    def __add__(self, another:"Money"):
        total_cents = (self.__euros * 100) + (another.__euros * 100) + self.__cents + another.__cents
        new_euros = total_cents // 100
        new_cents = total_cents % 100
        return Money(new_euros, new_cents)
    
    def __sub__(self, another:"Money"):
        self_money = self.__euros * 100 + self.__cents
        another_money = another.__euros * 100 + another.__cents
        if another.__euros < 0 or another.__cents < 0 or another_money > self_money:
            raise ValueError
        total_new_cents = self_money - another_money
        new_euros = total_new_cents // 100
        new_cents = total_new_cents % 100
        return Money(new_euros, new_cents)


if __name__ == "__main__":
    print(e1)
    e1.euros = 1000
    print(e1)