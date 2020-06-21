from abs_bakery import AbsBakery

class Bread(AbsBakery):
    def mix_dry_ingredients(self):
        print('Mixing flour, sugar and salt.')

    def add_leavening(self):
        print('Adding yeast.')

    def add_liquid(self):
        print('Mixing in oil.')

    def knead(self):
        print('Kneading the dough')
