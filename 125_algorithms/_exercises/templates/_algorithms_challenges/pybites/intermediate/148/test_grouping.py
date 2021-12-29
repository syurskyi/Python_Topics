____ grouping _______ cars, group_cars_by_manufacturer

expected_output = """
CHEVROLET
- Cavalier
- Corvette
- Impala

FORD
- Bronco
- Mustang
- Taurus

HYUNDAI
- Elantra
- Sonata
- Veracruz

KIA
- Optima
- Sorento
- Sportage

MERCEDES-BENZ
- 300D
- 600SEL
- E-Class

NISSAN
- Maxima
- Pathfinder
- Titan

TOYOTA
- Avalon
- Highlander
- Tundra

VOLKSWAGEN
- GTI
- Passat
- Routan
"""


___ test_group_cars_by_manufacturer(capfd):
    group_cars_by_manufacturer(cars)
    actual_output, _ = capfd.readouterr()
    ... actual_output.strip() __ expected_output.strip()