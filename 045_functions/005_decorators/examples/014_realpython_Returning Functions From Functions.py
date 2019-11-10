def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first)
# <function parent.<locals>.first_child at 0x7f599f1e2e18>

print(second)
# <function parent.<locals>.second_child at 0x7f599dad5268>

print(first())
print(second())