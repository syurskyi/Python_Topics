x _ in.(i..("Insert some numbers: "))
y _ 0

z _ x

w___ x !_ 0:
    digit _ x%10
    x _ x//10
    y _ y*10
    y _ y+digit
print("The reversed of ",z," = ",y)