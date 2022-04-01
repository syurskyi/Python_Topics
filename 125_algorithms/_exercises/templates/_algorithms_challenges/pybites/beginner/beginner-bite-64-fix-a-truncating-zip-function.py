'''
Bert is in charge of organizing an event and got the attendees names, locations and confirmations in 3 lists.
Assuming he got all data and being Pythonic he used zip to stitch them together (see template code) but then he sees
the output:

('Tim', 'DE', False)
('Bob', 'ES', True)
('Julian', 'AUS', True)
('Carmen', 'NL', False)
('Sofia', 'BR', True)
What?! Mike, Kim, and Andre are missing! You heard somebody mention itertools the other day for its power to work
with iterators. Maybe it has a convenient way to solve this problem? Check out the module and patch the get_attendees
function for Bert so it returns all names again. For missing data use dashes (-). After the fix Bert should
see this output:

('Tim', 'DE', False)
('Bob', 'ES', True)
('Julian', 'AUS', True)
('Carmen', 'NL', False)
('Sofia', 'BR', True)
('Mike', 'US', '-')
('Kim', '-', '-')
('Andre', '-', '-')
Good luck, Bert will be grateful if you fix this bug for him! By the way, this won't be the last itertools Bite,
it is a power tool you want to become familiar with!
'''

_______ i..

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.s..
locations = 'DE ES AUS NL BR US'.s..
confirmed = [F.., T.., T.., F.., T..]


___ get_attendees
    ___ participant __ i...z__(names, locations, confirmed, fillvalue='-'):
        print(participant)


__ _____ __ _____
    get_attendees()