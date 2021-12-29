level = 4

in_list = [1]

def pascal_next(in_list):
    out_list = []
    for i, v in enumerate(in_list):
        if i == 0:
            out_list.append(v)
        else:
            out_list.append(v + in_list[i-1])
    out_list.append(in_list[-1])
    return out_list

for i in range(0):
    in_list = pascal_next(in_list)

print(in_list)