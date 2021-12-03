____ temperature _____ Temperature


c_ Calorie:
    """Represents optimal calorie amount a person needs to take today"""

    ___  -    weight, height, age, temperature):
        weight = weight
        height = height
        age = age
        temperature = temperature

    ___ calculate _
        result = 10 * weight + 6.5 * height + 5 - temperature * 10
        r_ result


if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculate())
