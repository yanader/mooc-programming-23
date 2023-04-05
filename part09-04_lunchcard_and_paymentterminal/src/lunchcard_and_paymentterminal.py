# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
             self.balance -= amount
             return True
        else:
             return False
        

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_price = 2.50
        if payment < lunch_price:
            return payment
        else:
            self.funds += lunch_price
            self.lunches += 1
            return payment - lunch_price

    def eat_special(self, payment: float):
        special_price = 4.3
        if payment < special_price:
            return payment
        else:
            self.funds += special_price
            self.specials +=1
            return payment - special_price

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_price = 2.5
        if card.balance < lunch_price:
            return False
        else:
            card.balance -= lunch_price
            self.lunches +=1
            return True


    def eat_special_lunchcard(self, card: LunchCard):
        special_price = 4.3
        if card.balance < special_price:
            return False
        else:
            card.balance -= special_price
            self.specials +=1
            return True

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.balance += amount



if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)    