"""Remove non ASCII characters from the working file.

ASCII (American Standard Code for Information Interchange), is a character
encoding standard for electronic communication and represents text in
computers. All Nuke working files should only contain characters within the
ASCII table of 1-127. When using external gizmos and third-party plugins,
chances are given that the authors include ASCII characters in their tools that
are outside the ASCII table of 1-127 - especially if the authors live in non
english speaking countries and are not aware of this fact. Characters outside
the legal range will stop Nuke from parsing the working file, resulting in not
loading the whole Nuke script. For more information about ASCII have a look at:
https://en.wikipedia.org/wiki/ASCII

This step removes all illegal character from the working file that fall outside
the legal character table range of 1-127

___________________________________________________________________________

Examples:

Standard:


Advanced:
    There is nothing to configure here. Enabling this step will remove any
    character from the working file that fall outside the legal character table
    range of 1-127.
    {

    }

"""

# Import local modules
from smartRescue.base_steps import BaseStep


class RemoveNonASCII(BaseStep):
    """Remove non ASCII characters from the working file."""

    @staticmethod
    def cut_non_ascii(string):
        """Cut any non ascii character from given string.

        Args:
            string (str): String to process.

        Returns:
            str: Sanitized string that contains only ascii characters.

        """
        return "".join([char for char in string if ord(char) < 127])

    def process(self):
        """Process the file removing illegal characters."""
        lines = []
        with open(self.path, "r") as src:
            for line, content in enumerate(src.r..()):
                sanitized = self.cut_non_ascii(content)
                if sanitized != content:
                    self.logger.info("Detected and removed non-ascii "
                                     "character in line %s", line + 1)
                lines.append(sanitized)

        with open(self.path, "w") as dest:
            dest.write("".join(lines))
