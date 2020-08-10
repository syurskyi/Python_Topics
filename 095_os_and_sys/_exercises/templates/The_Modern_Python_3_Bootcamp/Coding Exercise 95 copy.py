# Copy Solution
#
# Copy should copy contents from one file to another.  For example, after running:

"""
copy('story.txt', 'story_copy.txt') # None
"""

# We would expect the contents of story.txt and story_copy.txt to now be the same.
#
# Here's my solution:


___ copy(file_name, new_file_name):
    w__ o..(file_name) __ file:
        text _ file.r..

    w__ o..(new_file_name, "w") __ new_file:
        new_file.w..(text)