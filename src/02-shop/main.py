import random


class Student:
    def __init__(self, name, products_to_sell):
        self.name = name
        self.products_to_sell = products_to_sell
        self.bought_products = []

    def create_bag(self, n=4):
        bag = []
        for _ in range(n):
            bag.append(random.choice(self.products_to_sell))
        return bag

    def add_bag(self, bag):
        self.bought_products.append(bag)

    def eat(self):
        if len(self.bought_products) == 0:
            print("No hay productos para comer")
            return

        product = random.choice(self.bought_products)

        food = product.pop()
        print(f"{self.name} comió {food}")

        if len(product) == 0:
            self.bought_products.remove(product)

    def str(self):
        return f"{self.name} tiene bolsas con {self.bought_products}"


class Shop:
    def __init__(self) -> None:
        self.products = []
        self.products = []

    def add_products(self, seller, times=5):
        bag = seller.create_bag
        for _ in range(times):
            self.products.append(bag)

    def buy_products(self, buyer):
        if len(self.products) == 0:
            print("No hay productos para comprar")
            return

        product = random.choice(self.products)

        buyer.add_bag(product)
        self.products.remove(product)


benja = Student("Benja", ["confitado", "salado", "dulce"])
juan = Student("Juan", [])
tomas = Student("Tomas", [])

shop = Shop()

print(juan)

shop.add_products(benja)
shop.buy_products(juan)
shop.buy_products(tomas)

print(juan)

for _ in range(4):
    juan.eat()

print(juan)
