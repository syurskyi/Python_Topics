PRICE_KWH = 0.11  # TODO get list of prices per country


class ApplianceCost:

    ___ __init__(self, name, wattage, price_kwh=PRICE_KWH
        self.name = name
        self.wattage = wattage
        self.price_kwh = price_kwh
        self._minutes = []  # log minutes

    @property
    ___ cost(self
        hours_used = su.(self._minutes)/60
        cost = self.wattage * hours_used / 1000 * self.price_kwh
        r_ round(float(cost), 2)

    ___ consume(self, minutes
        __ not isinstance(minutes, int
            raise ValueError('Please use int for minutes')
        self._minutes.append(minutes)


__ __name__ __ '__main__':
    # examples from:
    # https://energy.gov/energysaver/estimating-appliance-and-home-electronic-energy-use

    k = ApplianceCost('kettle', 1500)
    use = 365 * 60
    k.consume(use)
    assert k.cost __ 60.23
    print(k.cost)

    s = ApplianceCost('shredder', 360)
    use = 52 * 15
    s.consume(use)
    assert s.cost __ 0.51
    print(s.cost)
