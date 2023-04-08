# WRITE YOUR SOLUTION HERE:

class Car:

    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0
    
    def fill_up(self):
        self.__petrol = 60

    def drive(self, km:int):
        if km > 0:
            if km > self.__petrol:
                km = self.__petrol
        self.__odometer += km
        self.__petrol -= km
    
    def __str__(self):
        return f'Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres'