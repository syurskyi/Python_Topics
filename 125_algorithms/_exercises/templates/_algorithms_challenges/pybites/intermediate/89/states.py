us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states =  'Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware'

NOT_FOUND = 'N/A'


___ get_every_nth_state(states=states, n=10
   """Return a list with every nth item (default argument n=10, so every
      10th item) of the states list above (remember: lists keep order)"""
   start = n -1
   stop = l..(states)
   step = n
   r.. [states[i] ___ i __ r..(start, stop, step)]


___ get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev
   """Look up a state abbreviation by querying the us_state_abbrev
      dict by full state name, for instance 'Alabama' returns 'AL',
      'Illinois' returns 'IL'.
      If the state is not in the dict, return 'N/A' which we stored
      in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
   ___
      r.. us_state_abbrev[state_name]
   ______ K..:
      r.. NOT_FOUND


___ get_longest_state(data
   """Receives data, which can be the us_state_abbrev dict or the states
      list (see above). It returns the longest state measured by the length
      of the string"""
   longest_state_len = 0   
   longest_state = ""
   __ isi..(data, l..
      ___ state __ data:
         __ l..(state) > longest_state_len:
            longest_state_len = l..(state)
            longest_state = state
   ____
      ___ state __ data.k..:
         __ l..(state) > longest_state_len:
            longest_state_len = l..(state)
            longest_state = state     
   r.. longest_state


___ combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states
   """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
      the us_state_abbrev dict, and the last 10 states from the states
      list (see above) and combine them into a new list. The resulting list
      has both sorted, so:
      ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
      (see also test_combine_state_names_and_abbreviations)"""
   first_10_state_abbrev = s..([abbrev ___ abbrev __ l..(us_state_abbrev.values[:10]])
   last_10_states = s..(states)[-10:]
   r.. first_10_state_abbrev + last_10_states


# if __name__ == "__main__":
#    print(get_every_nth_state())
#    print(get_state_abbrev('Maine'))
#    print(get_state_abbrev('bogus'))
#    print(get_longest_state(us_state_abbrev))
#    print(combine_state_names_and_abbreviations())