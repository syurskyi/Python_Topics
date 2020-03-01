# %%
'''
### Slots
'''

# %%
'''
Let's start with an example of how we use slots:
'''

# %%
class Location:
    __slots__ = 'name', '_longitude', '_latitude'
    
    def __init__(self, name, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude
        self.name = name
        
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude

# %%
'''
`Location` still has that mapping proxy, and we can still add and remove **class** attributes from `Location`:
'''

# %%
Location.__dict__

# %%
Location.map_service = 'Google Maps'

# %%
Location.__dict__

# %%
'''
But the use of `slots` affects **instances** of the class:
'''

# %%
l = Location('Mumbai', 19.0760, 72.8777)

# %%
l.name, l.longitude, l.latitude

# %%
'''
The **instance** no longer has a dictionary for maintaining state:
'''

# %%
try:
    l.__dict__
except AttributeError as ex:
    print(ex)

# %%
'''
This means we can no longer add attributes to the instance:
'''

# %%
try:
    l.map_link = 'http://maps.google.com/...'
except AttributeError as ex:
    print(ex)

# %%
'''
Now we can actually delete the attribute from the instance:
'''

# %%
del l.name

# %%
'''
And as we can see the instance now longer has that attribute:
'''

# %%
try:
    print(l.name)
except AttributeError as ex:
    print(f'Attribute Error: {ex}')

# %%
'''
However we can still re-assign a value to that same attribute:
'''

# %%
l.name = 'Mumbai'

# %%
l.name

# %%
'''
Mainly we use slots when we expect to have many instances of a class and to gain a performance boost (mostly storage, 
but also attribute lookup speed). 
'''

# %%
