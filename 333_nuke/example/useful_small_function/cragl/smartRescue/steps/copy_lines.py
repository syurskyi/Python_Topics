"""Copy all lines between first_line and last_line to a backup file.

This is useful to debug at which node of a working file the file itself gets
corrupt and will possibly crash when opening the working file. Keep in mind
that you should set the first line at the beginning of a node and the last
line at the end of a node to prevent from generating working files with
incomplete node structures. For that you will need to view the working file
using a text editor (all .nk files are simply ascii files that you can view
with your text editor).

Args:
    first_line (str): The first line to include in the new file.
    last_line (str): The last line to include in the new file.

___________________________________________________________________________

Examples:

Standard:
    1) This will store the content of line 1 to 37. All lines afterwards will
    be removed:

    first line: 1
    last line: 37

    ------------------------------------------------------------------------

    2) Inserting negative values for the 'last_line' is possible as well. This
    will then copy until the last x lines:

    first line: 1
    last line: -100

    This will copy line 1 until the last 100 lines. For instance, when the
    working file contains 500 lines, then it will copy line 1 till line 400.
    The last 100 lines won't be copied.

Advanced:
    1) This will store the content of line 1 to 37. All lines afterwards will
    be removed:

    {
        "first_line": 1,
        "last_line": 37
    }

    ---------------------------------------------------------------------------

    2) Inserting negative values for the 'last_line' is possible as well. This
    will then copy until the last x lines:

    {
        "first_line": 1,
        "last_line": -100
    }
    This will copy line 1 until the last 100 lines. For instance, when the
    working file contains 500 lines, then it will copy line 1 till line 400.
    The last 100 lines won't be copied.

"""

# Import built-in modules
import os

# Import local modules
from smartRescue.base_steps import BaseStep


class CopyLines(BaseStep):
    """Copy lines between first_line and last_line to backup file."""

    def process(self):
        """Copy lines to backup file."""
        first_line = self.setup["first_line"]
        last_line = self.setup["last_line"]

        self.logger.info("Using lines %s - %s", first_line, last_line)

        path_temp = "{}_".format(self.path)

        with open(self.path, "r") as src, open(path_temp, "w") as dest:
            lines = src.r..
            copy_lines = lines[first_line-1:last_line]
            dest.write("".join(copy_lines))

        os.rename(path_temp, self.path)
