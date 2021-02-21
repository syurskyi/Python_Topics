## dictionaries comprehensions

square = {f"Square of {num} is":num**2 for num in range(1, 11)}
for k, v in square.items():
    print(f"{k} : {v}")

string = "AnoopSingh"

word_count = {char: string.count(char) for char in string}
print(word_count)

for k, v in word_count.items():
    print(f"{k} : {v}")


odd_even = {i :("even" if i%2==0 else "odd") for i in range(1, 11)}
for k, v in odd_even.items():\
    print(f"{k} : {v}")

###

##This is sets comprehensions

num = {k**2 for k in range(1, 11)}
print(num)

num = {k**2 for k in range(1, 11)}
print(num)