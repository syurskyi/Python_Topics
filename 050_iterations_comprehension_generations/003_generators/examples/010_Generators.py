def city_generator():
    yield("Hamburg")
    yield("Konstanz")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

city = city_generator()

print(next(city))
# Hamburg

print(next(city))
# Konstanz

print(next(city))
# Berlin

print(next(city))
# Zurich

print(next(city))
# Schaffhausen

print(next(city))
# Stuttgart

# print(next(city))


def count(firstval=0, step=1):
    x = firstval
    while True:
        yield x
        x += step


counter = count()  # count will start with 0
for i in range(10):
    print(next(counter), end=", ")

start_value = 2.1
stop_value = 0.3
print("\nNew counter:")
counter = count(start_value, stop_value)
for i in range(10):
    new_value = next(counter)
    print(f"{new_value:2.2f}", end=", ")

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
# New counter:
# 2.10, 2.40, 2.70, 3.00, 3.30, 3.60, 3.90, 4.20, 4.50, 4.80,