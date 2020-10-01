___ avg_list(first):
    last _ le.(first)
    su. _ 0
    ___ i __ first:
        su. +_ i
    r_ su./last

x _ i..("Insert some integer values: ")
x _ x.sp..()
___ i __ ra..(le.(x)):
    x[i] _ in.(x[i])

average _ avg_list(x)

print("The result of the average =",round(average,2))