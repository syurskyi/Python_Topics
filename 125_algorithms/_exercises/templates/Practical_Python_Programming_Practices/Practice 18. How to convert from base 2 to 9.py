num1 _ in.(input("Insert number to convert: "))
base_num _ in.(input("Choose the base(2-9): "))

__ not(2<_ base_num <_9):
    quit()

num2 _ ''

while num1>0:
    num2 _ st.(num1%base_num) + num2
    num1 //_ base_num

print(num2)