class OnlyNumbers(Exception):
    def __init__(self, data):
        self.user_data = data
        self.res_list = []
        self.list_numbers = [str(i) for i in range(10)]

    def check(self):
        while self.user_data != 'stop':
            self.user_data = input()
            try:
                for i in self.user_data:
                    if i not in self.list_numbers:
                        raise OnlyNumbers("Введен не числовой параметр")
            except OnlyNumbers as err:
                print(err)
            else:
                self.res_list.append(int(self.user_data))
        return self.res_list


res = OnlyNumbers('')
print(res.check())