# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.products):
            product = self.products[self.i]
            self.i += 1
            return product
        else:
            raise StopIteration