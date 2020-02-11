class Car:
    
    def __init__(self, model, year, id_num, engine_serial_num):
        self.model = model
        self.year = year
        self._id_num = id_num
        self.__engine_serial_num = engine_serial_num

my_car = Car("Escape", 2006, "44542", "201109048934242")
