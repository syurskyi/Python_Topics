MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    if age <= MIN_DRIVING_AGE:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    pass