from datetime import timedelta
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
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
    
    text = text.strip()
    
    sections = (text.split('\n\n'))
    

    id_to_speed = {}
    for section in sections:
        parts = section.split('\n')

        id_,times,text = parts

        start_time,end_time = times.split('-->')
        
        tds = []
        for time in (start_time,end_time):
            hours,minutes,seconds = time.split(':')
            hours = int(hours)
            minutes = int(hours)
            seconds = float('.'.join(seconds.split(',')))
            td = timedelta(hours=hours,minutes=minutes,seconds=seconds)
            tds.append(td)


        time_elapsed = (tds[1] - tds[0]).total_seconds()
        characters = len(text)

        characters_per_second = characters/time_elapsed


        id_to_speed[int(id_)]  = characters_per_second


    

    return sorted(list(id_to_speed.keys()),key=lambda x: id_to_speed[x],reverse=True)












