# %%
'''
### Project 1: TimeZone class
'''

# %%
'''
Let's start with the timezone class. This one will have two instance attributes, offset and name. 
I'm going to create those as read-only properties. Offsets should be provided as a timespan (timedelta) of hours and
 minutes - we'll allow specifying the hour and minute offsets separately in the __init__, but the offset property
  will combine those as a timespan object.
'''

# %%
import numbers
from datetime import timedelta


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')
            
        self._name = str(name).strip()
        
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')
        
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer.')
            
        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')
            
        # for time delta sign of minutes will be set to sign of hours
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')
            
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset
        
    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other):
        return (isinstance(other, TimeZone) and 
                self.name == other.name and 
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)
    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")

# %%
'''
Let's try it out and make sure it's working:
'''

# %%
tz1 = TimeZone('ABC', -2, -15)

# %%
print(tz1.name)

# %%
from datetime import datetime

dt = datetime.utcnow()
print(dt)

# %%
print(dt + tz1.offset)

# %%
'''
As we can see the offset seems to be working (-2:15 from current time)
'''

# %%
'''
(We really should be writing unit tests as we write our code - but I'll show you unit tests in the last section of this 
project, and next project we can code and unit test in parallel)
'''

# %%
