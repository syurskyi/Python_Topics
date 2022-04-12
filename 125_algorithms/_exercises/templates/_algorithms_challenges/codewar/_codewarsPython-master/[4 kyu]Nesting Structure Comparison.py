___ same_structure_as(original,other
    __ t..(original) __ ('str','int') a.. t..(other) __ ('str','int'
        __ ''.j.. m..(s..,original __ ''.j.. m..(s..,other:
            r.. T..
        __ ''.j.. m..(s..,original __ ''.j.. m..(s..,other ||-1
            r.. T..
        ____
            r..  F..

    __ t..(original) !_ t..(other
        r.. F..

    __ l..(original) !_ l..(other
        r.. F..
    ___ ori,oth __ z..(original,other
        __ t..(ori) !_ t..(oth
            r.. F..
        ____ t..(ori) __ t..(oth) a.. isi..(ori,l..
            __ n.. same_structure_as(ori,oth) o. l..(ori) !_ l..(oth
                r.. F..
    r.. T..


print(same_structure_as([1,[1,1]],[2,[2,2],[2,3]]
print(same_structure_as([1,' ',' ' ,  ' ',' ',1]
