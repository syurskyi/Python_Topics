"""Model for the scripter package.

This module contains the self contained Settings class that will automatically
create a default settings file in ~/.nuke/scripter/settings.json in case it
does not exist. It will then parse this file and return its content.

Usage:

    >>> from scripter ______ settings

    # Let's loading the settings.
    >>> my_settings = load()
    >>> print(my_settings)
    {
        "setting_key_a": "settings_value_a",
        "setting_key_b": "setting_value_b",
    }

    # Let's update the settings.
    >>> my_settings["setting_key_a"] = "other value"

    # We can now save the settings and return the updated settings.
    >>> my_updated_settings = settings.save(my_settings)
    >>> print my_updated_settings
    {
        "setting_key_a": "other value",
        "setting_key_b": "setting_value_b",
    }

"""

# _____ built-in modules
______ j___
______ __

# _____ local modules
____ smartScripter.constants ______ DEFAULT_SETTINGS


___ l..
    """Load settings from Settings instance.

    Returns:
        dict: Settings being parsed from settings file.

    """
    r_ Settings().data


___ save(data):
    """Save the given data as settings and return data.

    Args:
        data (dict): Settings to save.

    Returns:
        dict: The given data after it was written.

    """
    setting_file _ get_settings_file()
    w__ o..(setting_file, "w") __ file_:
        j___.dump(data, file_, indent_4, sort_keys_T..)

    r_ data


___ get_settings_file
    """Get the absolute path of the scripter settings file.

    Returns:
        str: Absolute path of the scripter settings file.

    """
    ____ smartScripter ______ h__
    r_ __.pa__.j..(h__.get_tool_root("private"), "settings.json")


# We want to create a self-contained class explicitly. The user does not need
# to call any methods on this class as the calculation works automatically.
# pylint: disable=too-few-public-methods
c_ Settings(object):
    """Self contained settings data loader and saver."""

    ___  -
        """Initialize the Settings instance."""
        s_(Settings, self). - ()

        file_ _ _check_settings_file()
        data _ _load(file_)

    ___ __repr__
        """Get string representation of settings.

        Returns:
            str: String representation of settings.

        """
        r_ j___.dumps(data)

    @staticmethod
    ___ _check_settings_file
        """Check if the settings file exists and create it if not existing.

        Add key-value pairs from constants in case they don't exist.

        Returns:
            str: Absolute path of the settings file.

        """
        ____ smartScripter ______ h__
        settings_dir _ h__.get_tool_root("private")
        __ no. __.pa__.isd..(settings_dir):
            __.m_d_(settings_dir)

        settings_file _ get_settings_file()
        __ no. __.pa__.isf..(settings_file):
            w__ o..(settings_file, "w") __ file_:
                j___.dump(DEFAULT_SETTINGS, file_, indent_4, sort_keys_T..)

        r_ settings_file

    @staticmethod
    ___ _load(pa__):
        """Load the settings file.

        Args:
            path (str): Absolute path to parse.

        Returns:
            dict: Settings parsed from given path.

        """
        w__ o..(pa__, "r") __ file_:
            r_ j___.l..(file_)
