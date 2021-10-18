#  A relative path starts from some given working directory, avoiding the need to provide the full absolute path. For instance, data.txt is a relative path to the /home/users/jano/data.txt from the perspective of the /home/users/jano/ directory.
#
# In other words, when we are located in the /home/users/jano/ directory, we can relate to the file simply by its name data.txt, without the need to specify the full path.
# relative_path.py
#
#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

home = Path.home()

relative = path.relative_to(home)
print(relative)

# The example prints the relative path of an archive file given the home directory.
#
# $ relative_path.py
# Downloads\wordpress-5.1.tar.gz
#
# This is the output.