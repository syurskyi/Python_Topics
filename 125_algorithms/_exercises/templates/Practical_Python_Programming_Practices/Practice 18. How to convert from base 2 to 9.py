num1 _ in.(i..("Insert number to convert: "))
base_num _ in.(i..("Choose the base(2-9): "))

__ no.(2<_ base_num <_9):
    quit()

num2 _ ''

w___ num1>0:
    num2 _ st.(num1%base_num) + num2
    num1 //_ base_num

print(num2)