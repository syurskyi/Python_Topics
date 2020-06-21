import abc

class AbsBakery(metaclass=abc.ABCMeta):
    def __init__(self, description):
        self._description = description

    def bake_product(self):
        self.mix_dry_ingredients()
        self.add_leavening()
        self.add_liquid()
        self.knead()
        self.bake_in_oven()
        self.let_it_cool()

    @abc.abstractproperty
    def mix_dry_ingredients(self):
        pass

    @abc.abstractproperty
    def add_leavening(self):
        pass

    @abc.abstractproperty
    def add_liquid(self):
        pass

    def knead(self):
        pass

    def bake_in_oven(self):
        print('Baking ' + self._description + ' in oven.')

    def let_it_cool(self):
        print(self._description + ' is cooling down.')
