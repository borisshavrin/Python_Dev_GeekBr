"""Создание методов импорта и экспорта продукции"""


class Store:
    type = 'Оргтехника'
    area = 200
    data = []                                   # база склада


class OrgTech:
    """Класс Оргтехники"""
    def __init__(self, name, price, qty):       # конструктор класса
        self.d = {}                             # словарь атрибутов объекта
        self.name, self.price, self.qty = name, price, qty
        self.d['name'] = self.name              # добавление в словарь атрибутов
        self.d['price'] = self.price
        self.d['qty'] = self.qty

    def import_product(*objects):               # метод, вызовающиий к каждому объекту оргтехники, полученному
        for obj in objects:                     # на входе, другой метод - для приема оргтехники на скдад
            obj.get_product()

    def export_product(*objects):               # то же самое, только теперь наоборот - экспорт со склада
        for obj in objects:
            obj.post_product()


class Printer(OrgTech):
    """Подкласс оргтехники - Принтер"""
    printer_d = []                              # общий список уникальных моделей принтеров с их атрибутами
    printer_names = []                          # отдельный список наименований моделей

    def __init__(self, name, price, qty):       # конструктор принтеров
        super().__init__(name, price, qty)
        self.type = 'printer'                   # присваивание каждому объекту атрибут типа
        self.d['type'] = self.type              # добавление его в словарь атрибутов объекта

    def get_product(self):                      # метод приема принтеров на склад
        if self.d['name'] in Printer.printer_names:
            for row in Printer.printer_d:               # если модель уже принималась на склад, то
                if row['name'] == self.d['name']:       # прибавляем только количество поступающих моделей
                    row['qty'] += self.d['qty']
        else:
            Printer.printer_names.append(self.name)     # иначе - добавляем наименование в список моделей
            Printer.printer_d.append(self.d)            # дабавляем принтеры в список принтеров
            Store.data.append(self.d)                 # добавляем принтеры в базу оргтехники

    def post_product(self):
        for row in Store.data:                        # экспорт принтеров и списание с базы оргтехники
            if row['name'] == self.d['name']:           # и из списка принтеров
                row['qty'] -= self.d['qty']


class Scanner(OrgTech):
    scanner_d = []
    scanner_names = []

    def __init__(self, name, price, qty):
        super().__init__(name, price, qty)
        self.type = 'scanner'
        self.d['type'] = self.type

    def get_product(self):
        if self.d['name'] in Scanner.scanner_names:
            for row in Scanner.scanner_d:
                if row['name'] == self.d['name']:
                    row['qty'] += self.d['qty']
        else:
            Scanner.scanner_names.append(self.name)
            Scanner.scanner_d.append(self.d)
            Store.data.append(self.d)

    def post_product(self):
        for row in Store.data:                        # экспорт сканеров и списание с базы оргтехники
            if row['name'] == self.d['name']:           # и из списка сканеров
                row['qty'] -= self.d['qty']


class Xerox(OrgTech):
    xerox_d = []
    xerox_names = []

    def __init__(self, name, price, qty):
        super().__init__(name, price, qty)
        self.type = 'xerox'
        self.d['type'] = self.type

    def get_product(self):
        if self.d['name'] in Xerox.xerox_names:
            for row in Xerox.xerox_d:
                if row['name'] == self.d['name']:
                    row['qty'] += self.d['qty']
        else:
            Xerox.xerox_names.append(self.name)
            Xerox.xerox_d.append(self.d)
            Store.data.append(self.d)

    def post_product(self):
        for row in Store.data:                        # экспорт ксероксов и списание с базы оргтехники
            if row['name'] == self.d['name']:           # и из списка ксероксов
                row['qty'] -= self.d['qty']


"""Создание объектов"""
one = Printer('P1000', 10000, 5)
two = Printer('P500', 5000, 5)
three = Xerox('X200', 2000, 3)
four = Xerox('X300', 3000, 5)
five = Scanner('S2000', 2000, 4)
six = Scanner('S2000', 2000, 3)
seven = Scanner('S3457', 3457, 3)
eight = Scanner('S2000', 2000, 3)

"""Импорт заказов"""
OrgTech.import_product(one, two, three, four, five, six, seven, eight)

for row in Store.data:
    print(row)
print('-'*60)

first_order = Printer('P1000', 10000, 4)    # Создание объектов - заказов на экспорт
Printer.export_product(first_order)         # Экспорт заказов
for row in Store.data:                      # вывод базы Оргтехники
    print(row)
print('-'*60)

second_order = Scanner('S2000', 2000, 3)     # Создание объектов - заказов на экспорт
Scanner.export_product(second_order)         # Экспорт заказов
for row in Store.data:                       # вывод базы Оргтехники
    print(row)

#print(second_order.__dict__)