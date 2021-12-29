MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    name = input("What is your name?")
    age = int(input("How old are you?"))
    MIN_DRIVING_AGE = age
    if MIN_DRIVING_AGE <= 18:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    pass