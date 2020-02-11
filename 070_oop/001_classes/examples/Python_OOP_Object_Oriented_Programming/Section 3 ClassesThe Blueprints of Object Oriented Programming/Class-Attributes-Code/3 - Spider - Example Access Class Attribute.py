class Spider:

    num_legs = 8

    def __init__(self, code, species, weight, size):
        self.code = code
        self.species = species
        self.weight = weight
        self.size = size

print(Spider.num_legs)

my_spider = Spider("453", "Tarantula", 50, 12)

print(my_spider.num_legs)

