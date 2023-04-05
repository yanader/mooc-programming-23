# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        #return self.name
        return f'{self.name} ({self.height} cm)'

class Room:
    def __init__(self):
        self.people = []
    
    def add(self, person:"Person"):
        self.people.append(person)
    
    def is_empty(self):
        return len(self.people) == 0
    
    def print_contents(self):
        combined_height = 0
        room_string = ''
        for person in self.people:
            combined_height += person.height
            room_string += str(person) + '\n'
        print(f'There are {len(self.people)} persons in the room, and their combined height is {combined_height} cm')
        print(room_string.strip())
    
    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest = self.people[0].height
            return_person = self.people[0]
            for person in self.people:
                if person.height < shortest:
                    shortest = person.height
                    return_person = person
        return return_person
    
    def remove_shortest(self):
        if self.is_empty():
            pass
        else:
            name_of_shortest = self.shortest().name
            for person in self.people:
                if person.name == name_of_shortest:
                    return self.people.pop(self.people.index(person))
        


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()