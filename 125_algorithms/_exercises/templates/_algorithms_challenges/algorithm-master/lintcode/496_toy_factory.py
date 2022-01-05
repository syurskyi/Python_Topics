"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
c_ Toy:
    ___ talk
        r.. NotImplementedError('This method should have implemented.')


c_ Dog(Toy):
    ___ talk
        print 'Wow'


c_ Cat(Toy):
    ___ talk
        print 'Meow'


c_ ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    ___ getToy  t..):
        __ t.. __ 'Dog':
            r.. Dog()
        __ t.. __ 'Cat':
            r.. Cat()
