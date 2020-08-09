"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    ___ talk(self
        raise NotImplementedError('This method should have implemented.')


class Dog(Toy
    ___ talk(self
        print 'Wow'


class Cat(Toy
    ___ talk(self
        print 'Meow'


class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    ___ getToy(self, type
        __ type __ 'Dog':
            r_ Dog()
        __ type __ 'Cat':
            r_ Cat()
