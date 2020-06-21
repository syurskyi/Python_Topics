class Ad:

    def __init__(self, owner, link):
        self.owner = owner
        self.link = link
        self.num_views = 0
        self.num_clicks = 0

class HouseAd(Ad):

    def __init__(self, owner, link, address, house_price):
        Ad.__init__(self, owner, link)
        self.address = address
        self.house_price = house_price

class ProductAd(Ad):

    def __init__(self, owner, link, description, product_price):
        Ad.__init__(self, owner, link)
        self.description = description
        self.product_price = product_price
