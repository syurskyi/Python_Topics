_______ p__

____ srt _______ get_srt_section_ids

text1 """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly.

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit.

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex.
"""
text2 """
18
00:01:12,100 --> 00:01:17,230
If you want a bit more minimalistic view, you can actually hide the sidebar.

19
00:01:18,200 --> 00:01:19,500
If you go to Settings

20
00:01:23,000 --> 00:01:26,150
scroll down to 'Focus Mode'.

21
00:01:28,200 --> 00:01:35,180
You can actually hide the sidebar and have only the description and the code editor.
"""  # noqa E501
text3 '\n'.j..(text1.s.. [:9])
text4 '\n'.j..(text2.s.. [5:])
# testing hours as well
text5 """
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


?p__.m__.p.("text, expected", [
    (text1, [1, 3, 2]),
    (text2, [19, 18, 21, 20]),
    (text3, [1, 2]),
    (text4, [19, 21, 20]),
    (text5, [34, 32, 33]),
])
___ test_srt(text, e..
    ... get_srt_section_ids(text) __ e..