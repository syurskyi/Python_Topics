# download your FB birthday calendar from
# https://www.facebook.com/events/upcoming
#
# = Birthday link under "You can add your events to Microsoft Outlook, Google Calendar or Apple Calendar..."
#
# This gets you a link like: 
# http://facebook.com/ical/b.php?uid=123&key=XYZ
#
# using icalendar, found via:
# http://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python

from collections ______ namedtuple
______ sys

from icalendar ______ Calendar

DEFAULT_CAL = 'cal.ics'

Bday = namedtuple('Bday', 'name month day')


___ get_birthdays(cal
    with open(cal, 'rb') as g:
        gcal = Calendar.from_ical(g.read())
        ___ component in gcal.walk(
            __ component.name __ "VEVENT":
                name = component.get('SUMMARY')
                __ not name:
                    continue
                name = name.replace("'s birthday", "")
                bday = component.get('DTSTART').dt
                yield Bday(name=name, month=bday.month, day=bday.day)


__ __name__ __ '__main__':
    __ le.(sys.argv) < 2:
        cal = DEFAULT_CAL
    ____
        cal = sys.argv[1]

    ___ bday in get_birthdays(cal
        print(bday)
