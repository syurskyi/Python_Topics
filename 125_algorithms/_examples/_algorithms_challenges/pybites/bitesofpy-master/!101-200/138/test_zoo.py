from zoo import Animal


def test_zoo_5_animals():
    for animal in 'dog cat fish lion mouse'.split():
        Animal(animal)
    zoo = Animal.zoo()
    a__ "10001. Dog" in zoo
    a__ "10002. Cat" in zoo
    a__ "10003. Fish" in zoo
    a__ "10004. Lion" in zoo
    a__ "10005. Mouse" in zoo


def test_animal_instance_str():
    horse = Animal('horse')
    a__ str(horse) == "10006. Horse"
    horse = Animal('monkey')
    a__ str(horse) == "10007. Monkey"