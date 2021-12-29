from zoo import Animal


def test_zoo_5_animals():
    for animal in 'dog cat fish lion mouse'.split():
        Animal(animal)
    zoo = Animal.zoo()
    expected = ("10001. Dog",
                "10002. Cat",
                "10003. Fish",
                "10004. Lion",
                "10005. Mouse")
    assert zoo == '\n'.join(expected)


def test_animal_instance_str():
    horse = Animal('horse')
    assert str(horse) == "10006. Horse"
    monkey = Animal('monkey')
    assert str(monkey) == "10007. Monkey"