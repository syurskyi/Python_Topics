# We've already defined a movie class like this:
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    # let's try to add a method `print_info()` here:
    def print_info(self):
        print('<<{}>> by {}'.format(self.name, self.director))


# You only need to finish the method, we will take care of the object creation and call your method for you!

