# Class
class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Method
def update_age(lst):
    print("==== Updating Age ====")
    print("\n-> Initial list:")
    for child in lst:
        print(f"Name: {child.name}; Age: {child.age}")

    # Update age
    for child in lst:
        child.age += 1
        
    print("\n-> Final list:")
    for child in lst:
        print(f"Name: {child.name}; Age: {child.age}")

classroom = [Child("Nora", 10), Child("Daniel", 13), Child("Jack", 7)]

# Method to increment the age
# of the instance of Child by 1
update_age(classroom)

