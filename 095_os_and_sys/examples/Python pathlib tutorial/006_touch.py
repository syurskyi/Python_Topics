 # The touch() creates a new empty file; it is an equivalent of the Linux touch command.
# touch.py

#!/usr/bin/python3

from pathlib import Path

Path('myfile.txt').touch()

# We create a new empty myfile.txt.