cars = [
    # need mock data? -> https://www.mockaroo.com == awesome
    ('Mercedes-Benz', '300D'), ('Mercedes-Benz', '600SEL'),
    ('Toyota', 'Avalon'), ('Ford', 'Bronco'),
    ('Chevrolet', 'Cavalier'), ('Chevrolet', 'Corvette'),
    ('Mercedes-Benz', 'E-Class'), ('Hyundai', 'Elantra'),
    ('Volkswagen', 'GTI'), ('Toyota', 'Highlander'),
    ('Chevrolet', 'Impala'), ('Nissan', 'Maxima'),
    ('Ford', 'Mustang'), ('Kia', 'Optima'),
    ('Volkswagen', 'Passat'), ('Nissan', 'Pathfinder'),
    ('Volkswagen', 'Routan'), ('Hyundai', 'Sonata'),
    ('Kia', 'Sorento'), ('Kia', 'Sportage'),
    ('Ford', 'Taurus'), ('Nissan', 'Titan'),
    ('Toyota', 'Tundra'), ('Hyundai', 'Veracruz'),
]


___ group_cars_by_manufacturer(cars):
    """Iterate though the list of (manufacturer, model) tuples
       of the cars list defined above and generate the output as described
       in the Bite description (see the tests for the full output).
       
       No return here, just print to the console. We use pytest > capfd to
       validate your output :)
    """
    cars_grouped    # dict
    ___ model, make __ cars:
        __ model n.. __ cars_grouped:
            cars_grouped[model] = [make]
        ____:
            cars_grouped[model].a..(make)
    
    cars_description = ""
    ___ idx, value __ e..(s..(cars_grouped.items())):
        cars_description += f"{value[0].upper()}\n"
        ___ model __ value[1]:
            cars_description += f"- {model}\n"
        __ idx != l..(cars_grouped):
            cars_description += "\n"
    print(cars_description)


# if __name__ == "__main__":
#     group_cars_by_manufacturer(cars)