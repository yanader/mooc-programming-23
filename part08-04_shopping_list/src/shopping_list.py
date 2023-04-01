# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------

def total_units(my_list: ShoppingList):
    total = 0
    for i in range(1,my_list.number_of_items()+1):
        total +=my_list.amount(i)
    return total

if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add('bananas',5)
    shopping_list.add('cans',5)


    print(total_units(shopping_list))