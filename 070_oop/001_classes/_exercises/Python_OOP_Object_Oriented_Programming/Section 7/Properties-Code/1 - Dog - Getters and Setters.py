class Dog:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._nname

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Please enter a valid name")
