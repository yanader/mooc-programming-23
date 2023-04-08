class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'

class Suitcase:

    def __init__(self, max_weight:int):
        self.__max_weight = max_weight
        self.items = []

    def add_item(self, item:"Item"):
        if self.weight() + item.weight() <=self.max_weight():
            self.items.append(item)

    def weight(self):
        current_weight = 0
        for item in self.items:
            current_weight += item.weight()
        return current_weight
    
    def max_weight(self):
        return self.__max_weight
    
    def print_items(self):
        for item in self.items:
            print(item.__str__())

    def heaviest_item(self):
        heaviest_weight = 0
        return_item = None
        for item in self.items:
            if item.weight() > heaviest_weight:
                heaviest_weight = item.weight()
                return_item = item
        return return_item
    
    def __str__(self):
        if len(self.items) != 1:
            s = 's'
        else:
            s = ''
        return f'{len(self.items)} item{s} ({self.weight()} kg)'

class CargoHold:

    def __init__(self, max_weight:int):
        self.__max_weight = max_weight
        self.cargo = []
    
    def add_suitcase(self, suitcase:"Suitcase"):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.cargo.append(suitcase)

    def weight(self):
        weight = 0
        for case in self.cargo:
            weight += case.weight()
        return weight
    
    def __str__(self):
        s = ''
        if len(self.cargo) != 1:
            s = 's'
        return f'{len(self.cargo)} suitcase{s}, space for {self.__max_weight - self.weight()} kg'
    
    def print_items(self):
        for case in self.cargo:
            case.print_items()

if __name__ == "__main__":
    hold = CargoHold(100)
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)
    print(hold.__str__())