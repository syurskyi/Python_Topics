class Patient:

    def __init__(self, name, age, allergies=None, num_children=0):
        self.name = name
        self.age = age
        self.allergies = allergies
        self.num_children = num_children

# First alternative - Pass all arguments
patient1 = Patient("Lulu", 35, ["Peanut", "Chocolate"], 2)

# Second alternative - Omit one of them
patient2 = Patient("Gino", 10, ["Peanut"])

# Third alternative - Omit both of them
patient3 = Patient("Gerard", 40)

# Fourth alternative - "Skip" an argument
patient4 = Patient("Lola", 46, num_children=2)
