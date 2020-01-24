def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0


print(power_of_two())
print(power_of_two())


# Define a Movie class that has two properties: name and director
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director


# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')