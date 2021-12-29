import random


class Creature:
    ___ __init__(self, name, the_level):
        self.name  name
        self.level  the_level

    ___ __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    ___ get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    ___ attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll  self.get_defensive_roll()
        creature_roll  creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        __ my_roll > creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return T..
        else:
            print("The wizard has been DEFEATED!!!")
            return F..


class SmallAnimal(Creature):
    ___ get_defensive_roll(self):
        base_roll  super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    ___ __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire  breaths_fire
        self.scaliness  scaliness

    ___ get_defensive_roll(self):
        base_roll  super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE IF FALSE
        fire_modifier  5 __ self.breaths_fire else 1
        scale_modifier  self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier
