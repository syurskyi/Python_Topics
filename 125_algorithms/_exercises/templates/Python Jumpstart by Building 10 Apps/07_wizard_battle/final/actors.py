_______ random


class Creature:
    ___ __init__(self, name, the_level):
        self.name  name
        self.level  the_level

    ___ __repr__(self):
        r.. "Creature: {} of level {}".f..(
            self.name, self.level
        )

    ___ get_defensive_roll(self):
        r.. random.randint(1, 12) * self.level


class Wizard(Creature):

    ___ attack(self, creature):
        print("The wizard {} attacks {}!".f..(
            self.name, creature.name
        ))

        my_roll  self.get_defensive_roll()
        creature_roll  creature.get_defensive_roll()

        print("You roll {}...".f..(my_roll))
        print("{} rolls {}...".f..(creature.name, creature_roll))

        __ my_roll > creature_roll:
            print("The wizard has handily triumphed over {}".f..(creature.name))
            r.. T..
        ____:
            print("The wizard has been DEFEATED!!!")
            r.. F..


class SmallAnimal(Creature):
    ___ get_defensive_roll(self):
        base_roll  super().get_defensive_roll()
        r.. base_roll / 2


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
        fire_modifier  5 __ self.breaths_fire ____ 1
        scale_modifier  self.scaliness / 10

        r.. base_roll * fire_modifier * scale_modifier
