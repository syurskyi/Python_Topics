# Roleplaying Game Classes Solution
#
# First define the Character class:


class Character():
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

# And then define the NPC class which inherits from Character.
# It also calls the Character __init__() method using super().


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "{0} says: 'I heard monsters running around last night!'".format(self.name)
