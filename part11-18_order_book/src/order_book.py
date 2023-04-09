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


if __name__ == "__main__":
    t = Task("code hello world", "Andy", 3)
    print(t)

# expected print out is
# 8: code hello world (3 hours), programmer Andy NOT FINISHED
# but string representation was
# 8: code hello world (3 hours). programmer Andy NOT FINISHED