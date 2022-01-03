____ d__ _______ d__, t..

____ logtimes _______ loglines, convert_to_datetime, time_between_shutdowns


___ test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    ... convert_to_datetime(line1) __ d__(2014, 7, 3, 23, 24, 31)
    ... convert_to_datetime(line2) __ d__(2015, 10, 3, 10, 12, 51)
    ... convert_to_datetime(line3) __ d__(2016, 9, 3, 2, 11, 22)


___ test_time_between_events():
    diff = time_between_shutdowns(loglines)
    ... t..(diff) __ t..
    ... s..(diff) __ '0:03:31'
