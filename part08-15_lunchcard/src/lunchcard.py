class LunchCard:

    def __init__(self, initial_balance:float) -> None:
        self.balance = initial_balance
    
    def __str__(self) -> str:
        return f'The balance is {self.balance:0.1f} euros'

    def eat_lunch(self):
        lunch_cost = 2.6
        if self.balance >= lunch_cost:
            self.balance -= lunch_cost
            return True
        else:
            return False
        
    def eat_special(self):
        special_cost = 4.6
        if self.balance >= special_cost:
            self.balance -= special_cost
            return True
        else:
            return False
    
    def deposit_money(self, amount:float):
        if amount < 0.0:
            raise ValueError("ValueError: You cannot deposit an amount of money less than zero")
        else:
            self.balance += amount
  
peter_card = LunchCard(20)
grace_card = LunchCard(30)
peter_card.eat_special()
grace_card.eat_lunch()
print('Peter: ' + str(peter_card))
print('Grace: ' + str(grace_card))
peter_card.deposit_money(20)
grace_card.eat_special()
print('Peter: ' + str(peter_card))
print('Grace: ' + str(grace_card))
peter_card.eat_lunch()
peter_card.eat_lunch()
grace_card.deposit_money(50)
print('Peter: ' + str(peter_card))
print('Grace: ' + str(grace_card))