_______ pytz
____ d__ _______ d__

MEETING_HOURS = r..(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


___ within_schedule(utc, *timezones):
   """Receive a utc datetime and one or more timezones and check if
      they are all within schedule (MEETING_HOURS)"""
   
   ___ time_z __ timezones:
      
      __ time_z n.. __ TIMEZONES:
         raise ValueError("Please use valid timezone")
                  
      new_tz = pytz.timezone(time_z)
         
      utc_localized = new_tz.localize(utc)
      utc_localized_offset = int(utc_localized.utcoffset().total_seconds()/60/60)
      time_difference = utc.hour + utc_localized_offset
      
      __ time_difference n.. __ MEETING_HOURS:
         r.. False
   r.. True