def get_profile(name="julian", profession="programmer"):
    if (name, profession) is False:
        raise TypeError("please provide input")
    else:
        return "{} is a {}".format(name, profession)
