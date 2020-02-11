class Product:

    def __init__(self, code, price, brand):
        self.code = code
        self.price = price
        self.brand = brand

    def display_product_data(self):
        print("==== Product Data ====")
        print("Code:", self.code)
        print("Price:", self.price)
        print("Brand:", self.brand)

class Butter(Product):

    def __init__(self, code, price, brand, expiration_date, temp):
        Product.__init__(self, code, price, brand)
        self.expiration_date = expiration_date
        self.temp = temp

class Shampoo(Product):

    def __init__(self, code, price, brand, size):
        Product.__init__(self, code, price, brand)
        self.size = size
