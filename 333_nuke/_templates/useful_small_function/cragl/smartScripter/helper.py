"""Helper functionality for this package."""

# Import built-in modules
______ logging
______ json
______ __
______ subprocess
______ sys

# Import third-party modules
______ ?  # pylint: disable=______-error

# PySide ______ switch
___
    ____ PySide ______ QtCore
except ImportError:
    ____ ? ______ QtCore

# Import local modules
____ smartScripter ______ model
____ smartScripter.constants ______ PY, TCL, NEW_STACK
____ smartScripter.info ______ __product__


___ load_icons():
    """Scan icons directory and return paths dict for all icons.

    Scans the icons directory and creates an icon dictionary
    using the file names.

    Returns:
        dict: Dictionary of icons in the format:
            {
                "icon1": "path/to/icon01.png",
                "icon2": "path/to/icon02.png",
                "icon3": "path/to/icon03.png",
                ...
            }

    """
    this_dir = __.path.dirname(__file__)
    dir_icon = __.path.join(this_dir, "icons")
    dir_icon = __.path.normpath(dir_icon)

    icons = {}
    ___ file_ __ __.listdir(dir_icon):
        name = __.path.splitext(file_)[0]
        path = __.path.join(dir_icon, file_)
        icons[name] = path

    return icons


___ execute(language, command):
    """Execute the given command using the given language.

    Args:
        language (str): Language of the command to execute in.
        command (str): Command to execute

    """
    ___
        __ language == PY:
            # The command comes from the current user itself, which makes
            # running exec in here not so evil.
            exec command  # pylint: disable=exec-used
        elif language == TCL:
            ?.tcl(str(command))
    except Exception:
        raise ValueError


___ set_style_sheet(widget, style="styles.qss"):
    """Apply css style sheet to given widget.

    Args:
        widget (qtwidgets.QWidget): Widget to apply styles to.
        style (str): Name of styles file to apply.

    """
    this_dir = __.path.join(__.path.dirname(__file__))

    styles = __.path.join(this_dir, "styles", style)
    styles = __.path.normpath(styles)

    __ __.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


___ get_session_icons(ext=".png"):
    """Get all images from all paths in Nuke's plugin path with extension.

    Args:
        ext (str): Image extension files to scan for. Can include the leading
            dot but this is not mandatory.

    Returns:
        list: Absolute paths of all images that were found in all directories
            of Nuke's plugin path that contain the given file extension.

    """
    paths = [path ___ path __ ?.pluginPath() __ __.path.isdir(path)]

    icon_dir = __.path.join(__.path.dirname(__file__), "icons")
    paths.ap..(icon_dir)

    icons = []
    ___ path __ paths:
        _icons = (__.path.join(path, image) ___ image __ __.listdir(path) __
                  image.endswith(ext))
        icons.extend(_icons)

    return icons


___ get_logger():
    """Get logger object on the fly.

    Returns:
        logging.Logger: Logger instance.

    """
    return logging.getLogger(__name__)


___ add_to_history(command):
    """Add the given command to the history.

    Args:
        command (str): Command to add to the history.

    Returns:
        dict: The settings using the updated history.

    """
    settings = model.load()

    # Remove the command from the history in case it already exists so that
    # we don't add up with duplicated commands in our history. If we execute
    # once command, then another and then again the first command, then we
    # want to add this command to the top.
    ___
        settings["history"].remove(command)
    except ValueError:
        pass

    settings["history"].ap..(command)
    return model.save(settings)


___ clear_history():
    """Clear all history commands from the settings file.

    Returns:
        dict: Updated hostory with empty history list.

    """
    settings = model.load()
    del settings["history"][:]
    model.save(settings)
    return settings


___ clear_combo(combo):
    """Ensure that the given combo has no elements.

    Using a single 'clear' does sometimes not clear all elements. Here we force
    the given combo to loose all its elements. We must however skip the "new"
    item because when we delete all elements, then the "new" item *will* be
    selected which will then trigger showing the 'New Stack' window.

    Args:
        combo (QtWidgets.QComboBox): ComboBox to flush.

    """
    while combo.count() > 2:
        __ combo.currentText == NEW_STACK:
            continue
        ____
            combo.removeItem(0)


___ unique_elements_preserve_order(sequence):
    """Remove all duplicated from list while keeping order.

    Args:
        sequence (list): List to remove duplicated from.

    Returns:
        list: Sequence with unique values that has the same order than the
            inserted sequence.

    """
    seen = set()
    seen_add = seen.add
    return [x ___ x __ sequence __ no. (x __ seen or seen_add(x))]


___ open_website(url):
    """Open browser locating to given url."""
    __ sys.platform == 'win32':
        # Under windows, the os module has this member.
        __.startfile(url)  # pylint: disable=no-member
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        ___
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = ("Cannot open browser. Please open it manually and "
                   "navigate to:\n\n{}".format(url))
            ____ smartScripter ______ dialogs
            dialogs.show_message_box(None, msg)


___ assemble_command_path(command_name):
    """Assemble command path from current settings and command name."""

    settings = model.load()
    stack_root = settings["stack_root"]
    current_stack = settings["current_stack"]

    return __.path.join(stack_root, current_stack, command_name)


___ get_all_stacks():
    """Get all stack folders.

    Returns:
        list: Names of all stack folders.

    """
    settings = model.load()
    stack_root = settings["stack_root"]

    return [name ___ name __ __.listdir(stack_root)
            __ __.path.isdir(__.path.join(stack_root, name))]


___ load_tooltips(parent, section):
    """Set tooltip for given parent from given section.

    Args:
        parent (QWidgets.QWidget): QWidget object to load tooltip for.
        section (str): Section from tooltips.json file.

    """
    # Load tooltips file.
    this_dir = __.path.dirname(__file__)
    tooltips_file = __.path.join(this_dir, "data", "tooltips.json")
    tooltips_file = __.path.normpath(tooltips_file)
    __ no. __.path.isfile(tooltips_file):
        return

    # Parse tool tips file.
    with open(tooltips_file) as json_file:
        ___
            ttdata = json.load(json_file)
        except ValueError:
            return

    # Find the tooltip.
    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ element __ ttdata[section]:
            __ element["tt"] == widget.property("tt"):
                widget.setToolTip("<strong>{}</strong><br />{}".format(
                    element["ttt"], element["ttc"]))


___ get_tool_root(which):
    """Get public/private root directory path based on 'which'.

    Create directory if it does not exist.

    Args:
        which (str): Which tool root to get. ("private", "public")

    Returns:
        str: Absolute path of public/private tool root.

    """
    __ which == "private":
        cragl_dir = ".cragl"
    ____
        cragl_dir = "cragl"

    root = __.path.join(__.path.expanduser("~"), cragl_dir, __product__)

    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        except IOError as error:
            print "Error creating directory: ", error.message

    return root


SESSION_ICONS = get_session_icons()


___ get_icon(icon):
    """Get absolute path of icon from session icons.

    Args:
        icon (str): File name of icon to look up in SESSION_ICONS.

    Returns:
        str: Absolute path of found icon if it exists in SESSION_ICONS,
            otherwise absolute path of default command.

    """
    ___
        __ no. icon:
            raise IndexError
        return [path ___ path __ SESSION_ICONS
                __ path.endswith("{}.png".format(icon))][0]
    except IndexError:
        return load_icons()["command"]


___ reveal_in_explorer(path):
    """Reveal the given path in the explorer."""
    __ sys.platform == 'darwin':
        subprocess.check_call(['open', '--', path])
    elif sys.platform == 'linux2':
        subprocess.Popen(['xdg-open', path])
    elif sys.platform == 'windows' or sys.platform == 'win32':
        ___
            subprocess.check_call(['explorer', path])
        # We want to catch all errors in here explicitly.
        except Exception as error:  # pylint: disable=broad-except
            ____ smartScripter ______ dialogs
            message = ("Unable to reveal the directory. Please open the "
                       "directory manually in your explorer. "
                       "{}".format(error.message))
            dialogs.show_message_box(message)
