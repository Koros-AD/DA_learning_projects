#6) Создайте класс для корзины покупок с методами добавления и удаления товаров и расчета общей стоимости.
class Cart:
    def __init__(self):
        self.items = {}

    def addit(self, name, price, quantity=1):
        if name in self.items:
            self.items[name] = (self.items[name][0], self.items[name][1] + quantity)
        else:
            self.items[name] = (price, quantity)
            print(f"{quantity} {name} added to the cart")

    def removeit(self, name, quantity=1):
        if name not in self.items:
            print(f"{name} is not in the cart")
            return

        if self.items[name][1] < quantity:
            print(f"Not enough {name} in the cart")
            return

        self.items[name] = (self.items[name][0], self.items[name][1] - quantity)
        print(f"{quantity} {name} removed from the cart")

    def checkvalue(self):
        total = 0
        for name, item in self.items.items():
            price, quantity = item
            item_total = price * quantity
            total += item_total
        return total


cart1 = Cart()
cart1.addit("cheese", 5)
cart1.addit("noodles", 0.5, 2)
cart1.removeit("cheese")
print(cart1.checkvalue())


