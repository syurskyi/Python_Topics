_______ random


c_ Creature:
    ___ - , name, the_level):
        name  name
        level  the_level

    ___ __repr__
        r.. "Creature: {} of level {}".f..(
            name, level
        )

    ___ get_defensive_roll
        r.. random.randint(1, 12) * level


c_ Wizard(Creature):

    ___ attack(self, creature):
        print("The wizard {} attacks {}!".f..(
            name, creature.name
        ))

        my_roll  get_defensive_roll()
        creature_roll  creature.get_defensive_roll()

        print("You roll {}...".f..(my_roll))
        print("{} rolls {}...".f..(creature.name, creature_roll))

        __ my_roll > creature_roll:
            print("The wizard has handily triumphed over {}".f..(creature.name))
            r.. T..
        ____:
            print("The wizard has been DEFEATED!!!")
            r.. F..


c_ SmallAnimal(Creature):
    ___ get_defensive_roll
        base_roll  super().get_defensive_roll()
        r.. base_roll / 2


c_ Dragon(Creature):
    ___ - , name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        breaths_fire  breaths_fire
        scaliness  scaliness

    ___ get_defensive_roll
        base_roll  super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE IF FALSE
        fire_modifier  5 __ breaths_fire ____ 1
        scale_modifier  scaliness / 10

        r.. base_roll * fire_modifier * scale_modifier
