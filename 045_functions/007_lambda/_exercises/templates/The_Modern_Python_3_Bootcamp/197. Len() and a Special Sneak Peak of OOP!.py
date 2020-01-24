class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50


l1 = SpecialList([1, 40, 30, 100, 30, 1, 2, 3, 4])
l2 = SpecialList([1, 3, 4, 5])

print(len(l1))  # 50
print(len(l2))  # 50
