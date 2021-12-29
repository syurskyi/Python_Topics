___ avg_list(first):
    last  l..(first)
    s..  0
    ___ i __ first:
        s.. + i
    r.. s../last

x  input("Insert some integer values: ")
x  x.s.. 
___ i __ r..(l..(x)):
    x[i]  i..(x[i])

average  avg_list(x)

print("The result of the average =",round(average,2))