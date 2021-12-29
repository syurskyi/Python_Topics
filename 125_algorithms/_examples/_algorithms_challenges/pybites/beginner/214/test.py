def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

print("start")
gen = infinite_sequence()
print("->", next(gen))
print("->", next(gen))
print("->", next(gen))
print("->", next(gen))
print("->", next(gen))
print("->", next(gen))