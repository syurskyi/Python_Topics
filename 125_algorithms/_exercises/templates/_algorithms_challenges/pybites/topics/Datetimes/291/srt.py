____ d__ _______ t.., d__
____ typing _______ List

text1 = """
32
00:59:45,000 --> 00:59:48,150
talking quite normal here

33
01:00:00,000 --> 01:00:07,000
he is talking slooooow

34
02:04:28,000 --> 02:04:30,000
she is talking super fast here!
"""

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
    line_dict = {}
    epoch = '1970-01-01'
    dialog_list = text.s..('\n\n')
    ___ dialog __ dialog_list:
       index, timestamp, line = dialog.s...splitlines()
       begintime, endtime = timestamp.s..(' --> ')
       duration = d__.fromisoformat(f'{epoch} {endtime[:8]}') - d__.fromisoformat(f'{epoch} {begintime[:8]}')
       line_dict[int(index)] = l..(line)/duration.total_seconds()
    r.. s..(line_dict, key=line_dict.get, reverse=True )


print(get_srt_section_ids(text1))

#epoch = '1970-01-01'
#a = datetime.fromisoformat(f'{epoch} 00:05:23.283')

#print(a)
