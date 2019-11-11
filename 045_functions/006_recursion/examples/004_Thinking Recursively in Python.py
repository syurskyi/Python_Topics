houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]


def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)

deliver_presents_iteratively()
# Delivering presents to Eric's house
# Delivering presents to Kenny's house
# Delivering presents to Kyle's house
# Delivering presents to Stan's house

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)
# Delivering presents to Eric's house
# Delivering presents to Kenny's house
# Delivering presents to Kyle's house
# Delivering presents to Stan's house