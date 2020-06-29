"""Model for the scripter package.

This module contains the self contained Settings class that will automatically
create a default settings file in ~/.nuke/scripter/settings.json in case it
does not exist. It will then parse this file and return its content.

Usage:

    >>> from scripter import settings

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

# Import built-in modules
______ json
______ os

# Import local modules
from smartScripter.constants ______ DEFAULT_SETTINGS


___ load():
    """Load settings from Settings instance.

    Returns:
        dict: Settings being parsed from settings file.

    """
    return Settings().data


___ save(data):
    """Save the given data as settings and return data.

    Args:
        data (dict): Settings to save.

    Returns:
        dict: The given data after it was written.

    """
    setting_file = get_settings_file()
    with open(setting_file, "w") as file_:
        json.dump(data, file_, indent=4, sort_keys=True)

    return data


___ get_settings_file():
    """Get the absolute path of the scripter settings file.

    Returns:
        str: Absolute path of the scripter settings file.

    """
    from smartScripter ______ helper
    return os.path.join(helper.get_tool_root("private"), "settings.json")


# We want to create a self-contained class explicitly. The user does not need
# to call any methods on this class as the calculation works automatically.
# pylint: disable=too-few-public-methods
class Settings(object):
    """Self contained settings data loader and saver."""

    ___ __init__(self):
        """Initialize the Settings instance."""
        super(Settings, self).__init__()

        file_ = self._check_settings_file()
        self.data = self._load(file_)

    ___ __repr__(self):
        """Get string representation of settings.

        Returns:
            str: String representation of settings.

        """
        return json.dumps(self.data)

    @staticmethod
    ___ _check_settings_file():
        """Check if the settings file exists and create it if not existing.

        Add key-value pairs from constants in case they don't exist.

        Returns:
            str: Absolute path of the settings file.

        """
        from smartScripter ______ helper
        settings_dir = helper.get_tool_root("private")
        __ not os.path.isdir(settings_dir):
            os.makedirs(settings_dir)

        settings_file = get_settings_file()
        __ not os.path.isfile(settings_file):
            with open(settings_file, "w") as file_:
                json.dump(DEFAULT_SETTINGS, file_, indent=4, sort_keys=True)

        return settings_file

    @staticmethod
    ___ _load(path):
        """Load the settings file.

        Args:
            path (str): Absolute path to parse.

        Returns:
            dict: Settings parsed from given path.

        """
        with open(path, "r") as file_:
            return json.load(file_)
