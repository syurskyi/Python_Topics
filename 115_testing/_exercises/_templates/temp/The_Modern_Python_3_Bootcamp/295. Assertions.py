# Example 1
___ add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    r_ x + y


print(add_positive_numbers(1, 1))  # 2
add_positive_numbers(1, -1)  # AssertionError: Both numbers must be positive!

# Example 2


___ eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "food must be a junk food!"
    r_ f"NOM NOM NOM I am eating {food}"


food _ input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))
