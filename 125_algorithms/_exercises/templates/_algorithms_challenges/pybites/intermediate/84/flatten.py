___ flatten(list_of_lists):
    

    
    new_list = []
    
    for l in list_of_lists:
        __ type(l) in (tuple,list):
            new_list.extend(flatten(l))
        else:
            new_list.append(l)
    

    return new_list










