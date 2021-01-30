_____ subprocess
_____ sys


"""
this module provides functionality used by other modules inside the utilities package
"""


___ open_folder(pa__):
    """
    reveal path in explorer
    :param path: String path to reveal in explorer
    :return: None
    """

    __ sys.platform == "darwin":
        subprocess.check_call(["open", pa__])
    __ sys.platform == "linux2":
        subprocess.check_call(["gnome-open", pa__])
    __ sys.platform == "windows":
        subprocess.check_call(["explorer", pa__])
