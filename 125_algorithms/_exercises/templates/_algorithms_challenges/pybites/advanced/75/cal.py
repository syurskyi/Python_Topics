___ get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    

    mapping = {}
    ___ i,line __ e..(calendar_output.s...splitlines()):
        __ i __ 0:
            continue
        ____ i __ 1:
            days_length = l..(line)
            days = line.s..
        ____:
            numbers = [int(line[i:i+2]) __ n.. line[i:i+2].isspace() ____ 0 ___ i __ r..(0,l..(line) - 1,3)]
            print(numbers)


            ___ day,number __ z..(days,numbers):
                __ number != 0:
                    mapping[number] = day

    r.. mapping




__ __name__ __ "__main__":
    april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
    """

    print(april_1981)
    print(get_weekdays(april_1981))
