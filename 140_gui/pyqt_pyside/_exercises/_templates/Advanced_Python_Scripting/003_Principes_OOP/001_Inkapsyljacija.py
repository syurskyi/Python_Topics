class dividerClass(object):
    def __init__(self):
        self.__div = 1

    def divide(self, value):
        return value / self.__div

    def setDivider(self, val):
        if self.__checkValue(val):
            self.__div = val
        else:
            print('Wrong value')

    def __checkValue(self, val):
        return not val == 0

d = dividerClass()
d.setDivider(2)
d.divide(100)
# d.divide(15)
# d.div = 3
# d.div = 0
# d.setDivider(0)

