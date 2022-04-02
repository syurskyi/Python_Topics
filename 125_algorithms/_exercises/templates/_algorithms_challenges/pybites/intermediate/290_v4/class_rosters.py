_______ csv


___ process_classes(classes: l..) __ l..:
    '''cleans and returns classes according to SIS as list'''
    r.. [cls.s..(' - ')[0].r..('"', '') ___ cls __ classes __ cls]


___ process_row(row
    '''processes row according to SIS format.'''
    classes = process_classes(row[2:])
    r..  ','.j..([cls, '2020', row[0]]) ___ cls __ classes]


___ class_rosters(input_file
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    sis_list = l..()
    w__ o.. input_file, 'r') __ f:
        ___ row __ csv.reader(f
            sis_rows = process_row(row)
            __ sis_rows:
                sis_list.extend(sis_rows)
    r.. sis_list
