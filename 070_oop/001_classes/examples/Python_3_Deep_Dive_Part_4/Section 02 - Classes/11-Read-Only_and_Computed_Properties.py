# %%
'''
### Read-Only and Computed Properties
'''

# %%
'''
Although write-only properties are not that common, read-only properties (i.e. that define a getter but not a setter) 
are quite common for a number of things.
'''

# %%
'''
Of course, we can create read-only properties, but since nothing is private, at best we are "suggesting" to the users 
of our class they should treat the property as read-only. There's always a way to hack around that of course.
But still, it's good to be able to at least explicitly indicate to a user that a property is meant to be read-only.
'''

# %%
'''
The use case I'm going to focus on in this video, is one of computed properties. Those are properties that may not 
actually have a backing variable, but are instead calculated on the fly.
'''

# %%
'''
Consider this simple example of a `Circle` class where we can read/write the radius of the circle, but want a computed
property for the area. We don't need to store the area value, we can alway calculate it given the current radius value.
'''

# %%
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def area(self):
        print('calculating area...')
        return pi * (self.radius ** 2)

# %%
c = Circle(1)
print(c.area)

# %%
'''
We could certainly just use a class method `area()`, but the area is more a property of the circle, so it makes more 
sense to just retrive it as a property, without the extra `()` to make the call.
'''

# %%
'''
The advantage of how we did this is that shoudl the radius of the circle ever change, the area property will 
immediately reflect that.
'''

# %%
c.radius = 2
print(c.area)

# %%
'''
On the other hand, it's also a weakness - every time we need the area of the circle, it gets recalculated, 
even if the radius has not changed!
'''

# %%
print(c.area)
print(c.area)

# %%
'''
So now we can use properties to fix this problem without breaking our interface!
We are going to cache the area value, and only-recalculate it if the radius has changed.
In order for us to know if the radius has changed, we are going to make it into a property, and the setter will keep 
track of whether the radius is set, in which case it will invalidate the cached area value.
'''

# %%
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        # if radius value is set we invalidate our cached _area value
        # we could make this more intelligent and see if the radius has actually changed
        # but keeping it simple
        self._area = None
        # we could even add validation here, like value has to be numeric, non-negative, etc
        self._radius = value
        
    @property
    def area(self):
        if self._area is None:
            # value not cached - calculate it
            print('Calculating area...')
            self._area = pi * (self.radius ** 2)
        return self._area

# %%
c = Circle(1)

# %%
print(c.area)

# %%
print(c.area)

# %%
c.radius = 2

# %%
print(c.area)

# %%
print(c.area)

# %%
'''
There are a lot of other uses for calculate properties.
Some properties may even do a lot work, like retrieving data from a database, making a call to some external API, 
and so on.
'''

# %%
'''
### Example
'''

# %%
'''
Let's write a class that takes a URL, downloads the web page for that URL and provides us some metrics on that URL - 
like how long it took to download, the size (in bytes) of the page.
'''

# %%
'''
Although I am going to use the `urllib` module for this, I strongly recommend you use the `requests` 3rd party library 
instead: http://docs.python-requests.org
'''

# %%
import urllib
from time import perf_counter

# %%
class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
        
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        # we'll lazy load the page - i.e. we wait until some property is requested
        
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page is None:
            # need to first download the page
            self.download_page()
        return self._page_size
        
    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs
            
    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time

# %%
urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = WebPage(url)
    print(f'{url} \tsize={format(page.page_size, "_")} \telapsed={page.time_elapsed:.2f} secs')

# %%
