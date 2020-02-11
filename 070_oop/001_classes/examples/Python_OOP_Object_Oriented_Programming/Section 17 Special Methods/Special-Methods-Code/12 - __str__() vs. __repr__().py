class Shirt:
    def __init__(self, color, size, brand):
        self.color = color
        self.size = size
        self.brand = brand

    def __str__(self):
        return f"Color: {self.color}; Size: {self.size}; Brand: {self.brand}"

    def __repr__(self):
        return f'Shirt("{self.color}", "{self.size}", "{self.brand}")'

shirt = Shirt("Blue", "XL", "Retro Land")

print("__str__() -", str(shirt))

print("\n__repr__() -", repr(shirt))

# The object can be recreated if needed
new_shirt = eval(repr(shirt))

print("\n(New object)", new_shirt)
