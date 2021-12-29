
def get_index_different_char(chars):
    


    


    alnum_count = not_alnum_count =  0 
    alnum_index = not_alnum_index = None
    for i,char in enumerate(chars):
        
        char = str(char)
        if char.isalnum():
            alnum_index = i
            alnum_count += 1
        else:
            not_alnum_index = i
            not_alnum_count += 1
    


    return alnum_index if alnum_count == 1 else not_alnum_index









        






