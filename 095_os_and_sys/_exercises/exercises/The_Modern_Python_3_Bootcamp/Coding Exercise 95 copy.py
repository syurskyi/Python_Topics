# Copy Solution
#
# Copy should copy contents from one file to another.  For example, after running:

"""
copy('story.txt', 'story_copy.txt') # None
"""

# We would expect the contents of story.txt and story_copy.txt to now be the same.
#
# Here's my solution:


def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text)