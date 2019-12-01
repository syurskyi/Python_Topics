# # %%
# '''
# ### Read-Only and Computed Properties
# '''
#
# # %%
# '''
# Although write-only properties are not that common, read-only properties (i.e. that define a getter but not a setter)
# are quite common for a number of things.
# '''
#
# # %%
# '''
# Of course, we can create read-only properties, but since nothing is private, at best we are "suggesting" to the users
# of our class they should treat the property as read-only. There's always a way to hack around that of course.
# But still, it's good to be able to at least explicitly indicate to a user that a property is meant to be read-only.
# '''
#
# # %%
# '''
# The use case I'm going to focus on in this video, is one of computed properties. Those are properties that may not
# actually have a backing variable, but are instead calculated on the fly.
# '''
#
# # %%
# '''
# Consider this simple example of a `Circle` class where we can read/write the radius of the circle, but want a computed
# property for the area. We don't need to store the area value, we can alway calculate it given the current radius value.
# '''
#
# # %%
# f___ ma.. ______ pi
#
# c_ Circle
#     ___ - ____ radius
#         ____.r... _ r...
#
#     0p_
#     ___ area ____
#         print('calculating area...')
#         r_ pi *  ____.r... ** 2
#
# # %%
# c _ ?(1)
# print(c.area)
#
# # %%
# '''
# We could certainly just use a class method `area()`, but the area is more a property of the circle, so it makes more
# sense to just retrive it as a property, without the extra `()` to make the call.
# '''
#
# # %%
# '''
# The advantage of how we did this is that shoudl the radius of the circle ever change, the area property will
# immediately reflect that.
# '''
#
# # %%
# c.r... _ 2
# print ?.a..
#
# # %%
# '''
# On the other hand, it's also a weakness - every time we need the area of the circle, it gets recalculated,
# even if the radius has not changed!
# '''
#
# # %%
# print ?.a..
# print ?.a..
#
# # %%
# '''
# So now we can use properties to fix this problem without breaking our interface!
# We are going to cache the area value, and only-recalculate it if the radius has changed.
# In order for us to know if the radius has changed, we are going to make it into a property, and the setter will keep
# track of whether the radius is set, in which case it will invalidate the cached area value.
# '''
#
# # %%
# c_ Circle
#     ___ - ____ radius
#         ____.r... _ r...
#         ____._area _ N...
#
#     0p_
#     ___ radius ____
#         r_ ____._ra...
#
#     @r....setter
#     ___ radius ____ value
#         # if radius value is set we invalidate our cached _area value
#         # we could make this more intelligent and see if the radius has actually changed
#         # but keeping it simple
#         ____._area _ N...
#         # we could even add validation here, like value has to be numeric, non-negative, etc
#         ____._radius _ v...
#
#     0p_
#     ___ area ____
#         i_ ____._area i_ N...:
#             # value not cached - calculate it
#             print('Calculating area...')
#             ____._ar.. _ pi *  ____.r... ** 2
#         r_ ____._ar..
#
# # %%
# c _ ? 1
#
# # %%
# print ?.a..
#
# # %%
# print ?.area
#
# # %%
# c.r... _ 2
#
# # %%
# print ?.a..
#
# # %%
# print ?.a..
#
# # %%
# '''
# There are a lot of other uses for calculate properties.
# Some properties may even do a lot work, like retrieving data from a database, making a call to some external API,
# and so on.
# '''
#
# # %%
# '''
# ### Example
# '''
#
# # %%
# '''
# Let's write a class that takes a URL, downloads the web page for that URL and provides us some metrics on that URL -
# like how long it took to download, the size (in bytes) of the page.
# '''
#
# # %%
# '''
# Although I am going to use the `urllib` module for this, I strongly recommend you use the `requests` 3rd party library
# instead: http://docs.python-requests.org
# '''
#
# # %%
# ______ urllib
# f___ time ______ perf_counter
#
# # %%
# c_ WebPage:
#     ___ - ____  url
#         ____.u.. _ u..
#         ____._page _ N...
#         ____._load_time_secs _ N...
#         ____._page_size _ N...
#
#     0p_
#     ___ url ____
#         r_ ____._u..
#
#     0__.s..
#     ___ url(____, value):
#         ____._url _ value
#         ____._page _ N...
#         # we'll lazy load the page - i.e. we wait until some property is requested
#
#     0p_
#     ___ page ____
#         i_ ____._page i_ N...
#             ____.download_page()
#         r_ ____._page
#
#     0p_
#     ___ page_size ____
#         i_ ____._page i_ N...:
#             # need to first download the page
#             ____.download_page
#         r_ ____._pa...
#
#     0p_
#     ___ time_elapsed ____
#         i_ ____._pa.. i_ N...:
#             ____.do.._pa..
#         r_ ____._load_time_secs
#
#     ___ download_page(____):
#         ____._page_size _ N...
#         ____._load_time_secs _ N...
#         start_time _ pe.._cou..
#         w___ ur__.re__.ur__ ____.u.. a_ f
#             ____._pa.. _ f.re..
#         end_time _ pe.._co..
#
#         ____._page_size _ le. ____._pa..
#         ____._l... _ en._ti.. - st.._ti..
#
# # %%
# urls _ [
#     'https://www.google.com',
#     'https://www.python.org',
#     'https://www.yahoo.com'
# ]
#
# ___ url i_ urls:
#     page _ W... u..
#     print _ |url \tsize_|f... pa__.pa.._si.. "_" | \telapsed_|pa__.ti.._el.. ;.2_| secs
#
# # %%
