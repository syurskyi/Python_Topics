INDENTS = 4

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


___ print_hanging_indents(poem):
    

    lines = poem.s..('\n')


    ___ i __ r..(1,l..(lines)):

        line = lines[i]

        line = line.lstrip()
        __ lines[i] __ '':
            continue
        __ lines[i -1] != '':
            print(' ' * INDENTS + line)
        ____:
            print(line)









__ __name__ __ "__main__":
    


    print_hanging_indents(shakespeare_unformatted)
