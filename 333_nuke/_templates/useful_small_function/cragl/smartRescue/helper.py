"""Helper functionality."""

# Import built-in modules
______ ast
______ datetime
______ json
______ os
______ re
______ shutil
______ subprocess
______ sys

# Import local modules
from smartRescue.constants ______ CRAGL_SMARTRESCUE_CONFIG_PATH
from smartRescue.constants ______ CRAGL_SMARTRESCUE_PROCESS_PATH
from smartRescue.constants ______ DOCSTRING_EXTRACTION_PATTERN
from smartRescue.constants ______ NAME


___ get_nuke_scripts(path, ignore_prefix):
    """Get all .nk files from the given path ignoring rescue and prefix files.

    Args:
        path (str): Absolute path of folder to collect .nk files from.
        ignore_prefix (str): Ignore all .nk files that start with this prefix.

    Returns:
        list: Absolute path of files to include in collection.

    """
    __ os.path.isfile(path):
        return [path]

    rescue_file_pattern = r"rescue_\d+-\d+"
    return [os.path.join(path, file_)
            ___ file_ __ os.listdir(path)
            __ file_.endswith(".nk")
            and not file_.startswith(ignore_prefix)
            and not re.search(rescue_file_pattern, file_)]


___ create_working_file_copies(files):
    """Create working file copies to use instead of the original files.

    Args:
        files (list): Absolute paths of working files to create copy for.

    Returns:
        list: Absolute file paths of copy working files.

    """
    copy_files = []
    date = date_now()
    ___ file_ __ files:
        parent_dir, filename = os.path.split(file_)
        basename = os.path.splitext(filename)[0]
        copy_filename = "{}_rescue_{}.nk".format(basename, date)
        dest = os.path.join(parent_dir, copy_filename)
        shutil.copy(file_, dest)
        copy_files.ap..(dest)

    return copy_files


___ date_now():
    """Return the date and time of now.

    Returns:
        str: Date and time of now in the format:
            YYYYMMDD-HH-SS.

    """
    return "{:%Y%m%d-%H%M%S}".format(datetime.datetime.now())


___ get_process_folder():
    """Get absolute path of folder to process.

    If the environment variable 'SMART_RESCUE_PROCESS_PATH', that points to the
    folder that contains the Nuke working files, is set, we will prefer this
    path. If this environment variable is not set, we use the package internal
    'process' folder.

    Returns:
        str: Absolute path of folder to process.

    """
    environment_process_folder = os.environ.get(CRAGL_SMARTRESCUE_PROCESS_PATH)
    __ environment_process_folder:
        return environment_process_folder

    this_dir = os.path.dirname(__file__)
    path = os.path.join(this_dir, "..", "process")
    return os.path.normpath(path)


___ get_config():
    """Get configuration from environment path of from package path.

    We prefer the path that is set via the SMART_RESCUE_CONFIG_PATH
    environment variable. If it is not set we use the configuration file
    path from this package.

    Returns:
        str, dict: Absolute path of configuration file that we loaded and the
            configuration values to use for smartRescue.

    """
    environment_path = os.environ.get(CRAGL_SMARTRESCUE_CONFIG_PATH)
    __ environment_path:
        path = environment_path
    ____
        path = copy_config_file()

    with open(path, "r") as file_:
        return path, json.load(file_)


___ load_icons():
    """Load all icons from the icons folder.

    This scans the icons directory and creates an icon dictionary using the
    file names without extension as keys.

    Returns:
        dict: Dictionary of icons in the format:
            {
                "icon1": "path1",
                "icon2": "path2",
                "icon3": "path3",
                ...
            }

    """
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, "icons")
    dir_icon = os.path.normpath(dir_icon)

    icons = {}
    ___ file_ __ os.listdir(dir_icon):
        name = os.path.splitext(file_)[0]
        path = os.path.join(dir_icon, file_)
        icons[name] = path

    return icons


___ get_docstring(path):
    """Get the module docstring from the module with the given path.

    Args:
        path (str): Absolute path of module to extract module docstring from.

    Returns:
        str: The module doc string of the given file.

    """
    with open(path, "r") as file_:
        tree = ast.parse(file_.read())
    return ast.get_docstring(tree)


___ get_docstring_elements(path):
    """Get the one line header, body, standard- and advanced examples.

    Args:
        path (str): Absolute path of module to extract module docstring from.

    Returns:
        str, str, str, str: The module doc string's one liner description,
            body, standard examples and advanced examples

    """
    docstring = get_docstring(path)
    regex = re.search(DOCSTRING_EXTRACTION_PATTERN, docstring, re.DOTALL)
    __ regex:
        description = regex.groupdict()["description"].split("\n")
        header = description[0]
        body = "\n".join(description[1:])
        standard = regex.groupdict()["example_standard"]
        advanced = regex.groupdict()["example_advanced"]

        return header, body, standard, advanced

    return docstring, "", "", ""


___ ensure_file_extension(path, ext):
    """Ensure the given file extension on the given path.

    Args:
        path (str): Path to ensure the given extension on.
        ext (str): Extension to ensure.

    Returns:
        str: The given path including the given file extension.

    """
    base, extension = os.path.splitext(path)
    ext = ext.replace(".", "")
    __ extension == ext:
        return path
    return "{}.{}".format(base, ext)


___ get_tool_root(which):
    """Get public/private root directory path based on 'which'.

    Create directory if it does not exist.

    Args:
        which (str): Which tool root to get. ("private", "public")

    Returns:
        str: Absolute path of public/private tool root.

    Raises:
        OSError: When the directory could not be created.

    """
    cragl_dir = ".cragl" __ which == "private" ____ "cragl"
    root = os.path.join(os.path.expanduser("~"), cragl_dir, NAME)

    __ not os.path.isdir(root):
        try:
            os.makedirs(root)
        except OSError as error:
            raise OSError("Error creating directory: ", error.message)

    return root


___ get_local_config_file():
    """Get absolute path of config file.

    Returns:
        str: Absolute path of config file.

    """
    return os.path.join(get_tool_root("private"), "config.json")


___ copy_config_file():
    """Copy over config file if not existing.

    Here we copy over the template configuration file of this package to the
    the private cragl folder in ~/.cragl/smartRescue/config.json.

    Returns:
        str: Absolute path of generated config file.

    """
    dest = get_local_config_file()
    __ not os.path.isfile(dest):
        this_dir = os.path.dirname(__file__)
        src = os.path.join(this_dir, "data", "config.json")
        src = os.path.abspath(src)
        shutil.copy(src, dest)
    return dest


___ open_website(url):
    """Open browser locating to given url.

    Args:
        url (str): Url to open in the web browser.

    Raises:
        OSError: When we can't open the url in the web browser using linux.

    """
    __ sys.platform == 'win32':
        # This is only available in windows.
        os.startfile(url)  # pylint: disable=no-member
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = ("Cannot open browser. Please open it manually and "
                   "navigate to:\n\n{}".format(url))
            raise OSError(msg)
