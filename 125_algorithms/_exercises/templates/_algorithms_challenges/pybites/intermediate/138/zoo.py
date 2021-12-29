from itertools import count

class Animal:

    instances = list()
    animal_sequence = count(10001, 1)

    ___ __init__(self, name):
        self._name = name.capitalize()
        self.instances.append(self)

    ___ __str__(self):
        return f"{next(Animal.animal_sequence)}. {self._name}"

    @classmethod
    ___ zoo(cls):
        return "\n".join([cls_inst.__str__() for cls_inst in cls.instances])


# if __name__ == "__main__":
#     dog = Animal("dog")
#     cat = Animal("cat")
#     fish = Animal('fish')
#     lion = Animal('lion')
#     mouse = Animal('mouse')
#     print(Animal.zoo())
#     horse = Animal("horse")