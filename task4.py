"""Создание класов и атрибутов"""


class Store:
    type = 'Оргтехника'
    area = 200
    data = []                                   # база склада


class OrgTech:
    def __init__(self, name, price, qty):
        self.d = {}
        self.name, self.price, self.qty = name, price, qty
        self.d['name'] = self.name
        self.d['price'] = self.price
        self.d['qty'] = self.qty


class Printer(OrgTech):
    def __init__(self, name, price, qty):
        super().__init__(name, price, qty)
        self.type = 'scanner'
        self.d['type'] = self.type


class Scanner(OrgTech):
    def __init__(self, name, price, qty):
        super().__init__(name, price, qty)
        self.type = 'scanner'
        self.d['type'] = self.type


class Xerox(OrgTech):
    def __init__(self, name, price, qty):
        super().__init__(name, price, qty)
        self.type = 'scanner'
        self.d['type'] = self.type


one = Printer('P1000', 10000, 4)
two = Printer('P500', 5000, 5)
three = Xerox('X200', 2000, 3)
four = Xerox('X300', 3000, 5)
five = Scanner('S2000', 20000, 3)