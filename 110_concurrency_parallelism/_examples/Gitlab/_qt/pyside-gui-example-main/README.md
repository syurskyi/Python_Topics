# PySide GUI Example

This is a simple example program demonstrating the use of PySide2 and Pyinstaller.

![Screenshot](./doc/readme-screenshot.png)

- Uses PySide2 to display a dark-themed window showing colorzied output from a Python logger
- Does work in the background using QThread and QObject.moveToThread
- Automatically writes timestamped log files to `~/.ThisApplication/logs`
- Handles exceptions (via `sys.excepthook`) by writing a callstack to the log and alerting the user
- Loads config values from a bundled config.yaml, overridden by `~/.ThisApplication/config.yaml`, with values in the 'env' section overridden by environment variables
- Uses PyInstaller to build a standalone Windows executable, with config file bundled
- Uses Inno Setup to build an installer for the standalone executable, with a version number (from `version.py`) stamped in

This is old code and I can make no guarantees that it does any of these things in a particularly sane way.

- Install: `pipenv install`
- Run: `pipenv run main.py`
- Build Windows Installer: `build.bat`

Requires Python 3 and pipenv.
