___ get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    

    mapping = {}
    for i,line in enumerate(calendar_output.strip().splitlines()):
        __ i == 0:
            continue
        elif i == 1:
            days_length = len(line)
            days = line.split()
        else:
            numbers = [int(line[i:i+2]) __ not line[i:i+2].isspace() else 0 for i in range(0,len(line) - 1,3)]
            print(numbers)


            for day,number in zip(days,numbers):
                __ number != 0:
                    mapping[number] = day

    return mapping




__ __name__ == "__main__":
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
