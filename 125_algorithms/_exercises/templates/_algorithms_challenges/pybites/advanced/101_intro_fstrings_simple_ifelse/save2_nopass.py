MIN_DRIVING_AGE = 18


___ allowed_driving(name, age):
    MIN_DRIVING_AGE = age
    __ MIN_DRIVING_AGE <= 18:
        print(f"{name} is allowed to drive")
    ____:
        print(f"{name} is not allowed to drive")
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    p..