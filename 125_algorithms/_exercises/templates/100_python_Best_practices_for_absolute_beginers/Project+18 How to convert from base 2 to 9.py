num1  i..(input("Insert number to convert: "))
base_num  i..(input("Choose the base(2-9): "))

__ n..(2< base_num <9):
    quit()

num2  ''

w___ num1>0:
    num2  str(num1%base_num) + num2
    num1 // base_num

print(num2)