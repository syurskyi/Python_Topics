from zoo ______ Animal


___ test_zoo_5_animals(
    ___ animal in 'dog cat fish lion mouse'.split(
        Animal(animal)
    zoo = Animal.zoo()
    assert "10001. Dog" in zoo
    assert "10002. Cat" in zoo
    assert "10003. Fish" in zoo
    assert "10004. Lion" in zoo
    assert "10005. Mouse" in zoo


___ test_animal_instance_str(
    horse = Animal('horse')
    assert str(horse) __ "10006. Horse"
    horse = Animal('monkey')
    assert str(horse) __ "10007. Monkey"