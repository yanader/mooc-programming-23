class Task:
    nextUID = 1
    def __init__(self, description:str, programmer:str, workload:int):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.completed = False
        self.id = Task.nextUID
        Task.nextUID +=1 
    
    def mark_finished(self):
        self.completed = True

    def is_finished(self):
        return self.completed
    
    def __str__(self):
        if self.completed:
            completed_string = 'FINISHED'
        else:
            completed_string = 'NOT FINISHED'
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {completed_string}'

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, name:str, workload:int):
        self.orders.append(Task(description, name, workload))

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set([task.programmer for task in self.all_orders()]))

    def mark_finished(self, id:int):
        for task in self.all_orders():
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError

    def finished_orders(self):
        return [order for order in self.all_orders() if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.all_orders() if not order.is_finished()]
    
    def status_of_programmer(self, programmer:str):
        if programmer not in self.programmers():
            raise ValueError
        finished = 0
        unfinished = 0
        finished_hours = 0
        unfinished_hours = 0
        for order in self.all_orders():
            if order.programmer == programmer:
                if order.is_finished():
                    finished += 1
                    finished_hours += order.workload
                else:
                    unfinished += 1
                    unfinished_hours += order.workload
        return (finished, unfinished, finished_hours, unfinished_hours)

class OrderBookInterface:
    def __init__(self):
        self.orderbook = OrderBook()
    
    def opening_text(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def add_order(self):
        desc = input('description: ')
        details = input('programmer and workload estimate: ')
        details_list = details.split(' ')
        if len(details_list) == 1 or not details_list[1].isnumeric():
            print('erroneous input')
            return
        self.orderbook.add_order(desc, details_list[0], int(details_list[1]))
        print('added!')

    def list_finished(self):
        if len(self.orderbook.finished_orders()) == 0:
            print('no finished tasks')
        else:
            for order in self.orderbook.finished_orders():
                print(order)

    def list_unfinished(self):
        if len(self.orderbook.unfinished_orders()) == 0:
            print('no unfinished tasks')
        else:
            for order in self.orderbook.unfinished_orders():
                print(order)

    def mark_as_finished(self, id:str):
        try:
            self.orderbook.mark_finished(int(id))
            print('marked as finished')
        except ValueError:
            print('erroneous input')
            return 

    def programmer_list(self):
        for programmer in self.orderbook.programmers():
            print(programmer)

    def programmer_status(self, name:str):
        try:
            details = self.orderbook.status_of_programmer(name)
            print(f'tasks: finished {details[0]} not finished {details[1]}, hours: done {details[2]} scheduled {details[3]}')
        except ValueError:
            print('erroneous input')
            return 

    def execute(self):
        self.opening_text()
        while True:
            print()
            command = int(input('command: '))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished()
            elif command == 3:
                self.list_unfinished()
            elif command == 4:
                finished_id = input('id: ')
                self.mark_as_finished(finished_id)
            elif command == 5:
                self.programmer_list()
            elif command == 6:
                name = input('programmer: ')
                self.programmer_status(name)
    




interface = OrderBookInterface()
interface.execute()