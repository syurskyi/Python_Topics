import subprocess
import sys


"""
this module provides functionality used by other modules inside the utilities package
"""


def open_folder(path):
    """
    reveal path in explorer
    :param path: String path to reveal in explorer
    :return: None
    """

    if sys.platform == "darwin":
        subprocess.check_call(["open", path])
    if sys.platform == "linux2":
        subprocess.check_call(["gnome-open", path])
    if sys.platform == "windows":
        subprocess.check_call(["explorer", path])
