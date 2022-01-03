____ d__ _______ t..
____ typing _______ List


___ get_srt_section_ids(text: s..) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    
    text = text.s..
    
    sections = (text.s..('\n\n'))
    

    id_to_speed    # dict
    ___ section __ sections:
        parts = section.s..('\n')

        id_,times,text = parts

        start_time,end_time = times.s..('-->')
        
        tds    # list
        ___ time __ (start_time,end_time):
            hours,minutes,seconds = time.s..(':')
            hours = int(hours)
            minutes = int(hours)
            seconds = float('.'.j..(seconds.s..(',')))
            td = t..(hours=hours,minutes=minutes,seconds=seconds)
            tds.a..(td)


        time_elapsed = (tds[1] - tds[0]).total_seconds()
        characters = l..(text)

        characters_per_second = characters/time_elapsed


        id_to_speed[int(id_)]  = characters_per_second


    

    r.. s..(l..(id_to_speed.keys()),key=l.... x: id_to_speed[x],r.._T..












