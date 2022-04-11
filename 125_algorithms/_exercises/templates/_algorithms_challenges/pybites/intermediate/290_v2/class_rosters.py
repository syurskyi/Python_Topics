_______ csv


___ class_rosters(input_file
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
     
    school_year 2020
    result    # list
    w__ o.. input_file _ __ f:
        data csv.reader(f)

        ___ row __ data:
            _id row[0]
            ___ i __ r..(2,l..(row:
                class_ row[i]
                __ class_:
                    class_section class_.r.. ' - ')[0]
                    result.a..(f"{class_section},{school_year},{_id}")



    r.. result






