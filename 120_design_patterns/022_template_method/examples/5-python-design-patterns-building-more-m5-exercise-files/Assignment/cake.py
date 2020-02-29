from abs_bakery import AbsBakery

class Cake(AbsBakery):
    def mix_dry_ingredients(self):
        print('Mixing flour, sugar and salt.')

    def add_leavening(self):
        print('Adding baking powder.')

    def add_liquid(self):
        print('Beating in butter.')
