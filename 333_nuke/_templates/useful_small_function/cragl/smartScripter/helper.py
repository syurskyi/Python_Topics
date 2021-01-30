"""Helper functionality for this package."""

# _____ built-in modules
______ logging
______ j___
______ __
______ subprocess
______ ___

# _____ third-party modules
______ ?  # pylint: disable=______-error

# PySide ______ switch
___
    ____ ? ______ ?C..
______ ImportError:
    ____ ? ______ ?C..

# _____ local modules
____ smartScripter ______ model
____ smartScripter.constants ______ PY, TCL, NEW_STACK
____ smartScripter.info ______ __product__


___ load_icons
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
    this_dir _ __.pa__.d_n_( -f)
    dir_icon _ __.pa__.j..(this_dir, "icons")
    dir_icon _ __.pa__.n_p_(dir_icon)

    icons _ {}
    ___ file_ __ __.l_d_(dir_icon):
        name _ __.pa__.s_t_(file_)[0]
        pa__ _ __.pa__.j..(dir_icon, file_)
        icons[name] _ pa__

    r_ icons


___ execute(language, command):
    """Execute the given command using the given language.

    Args:
        language (str): Language of the command to execute in.
        command (str): Command to execute

    """
    ___
        __ language __ PY:
            # The command comes from the current user itself, which makes
            # running exec in here not so evil.
            exec command  # pylint: disable=exec-used
        ____ language __ TCL:
            ?.tcl(st.(command))
    ______ E..:
        raise ValueError


___ set_style_sheet(widget, style_"styles.qss"):
    """Apply css style sheet to given widget.

    Args:
        widget (qtwidgets.QWidget): Widget to apply styles to.
        style (str): Name of styles file to apply.

    """
    this_dir _ __.pa__.j..(__.pa__.d_n_( -f))

    styles _ __.pa__.j..(this_dir, "styles", style)
    styles _ __.pa__.n_p_(styles)

    __ __.pa__.isf..(styles):
        w__ o..(styles) __ file_:
            widget.setStyleSheet(file_.read())


___ get_session_icons(ext_".png"):
    """Get all images from all paths in Nuke's plugin path with extension.

    Args:
        ext (str): Image extension files to scan for. Can include the leading
            dot but this is not mandatory.

    Returns:
        list: Absolute paths of all images that were found in all directories
            of Nuke's plugin path that contain the given file extension.

    """
    paths _ [pa__ ___ pa__ __ ?.pluginPath() __ __.pa__.isd..(pa__)]

    icon_dir _ __.pa__.j..(__.pa__.d_n_( -f), "icons")
    paths.ap..(icon_dir)

    icons _ # list
    ___ pa__ __ paths:
        _icons _ (__.pa__.j..(pa__, image) ___ image __ __.l_d_(pa__) __
                  image.endswith(ext))
        icons.extend(_icons)

    r_ icons


___ get_logger
    """Get logger object on the fly.

    Returns:
        logging.Logger: Logger instance.

    """
    r_ logging.getLogger(__name__)


___ add_to_history(command):
    """Add the given command to the history.

    Args:
        command (str): Command to add to the history.

    Returns:
        dict: The settings using the updated history.

    """
    settings _ model.l..()

    # Remove the command from the history in case it already exists so that
    # we don't add up with duplicated commands in our history. If we execute
    # once command, then another and then again the first command, then we
    # want to add this command to the top.
    ___
        settings["history"].r__(command)
    ______ ValueError:
        p..

    settings["history"].ap..(command)
    r_ model.save(settings)


___ clear_history
    """Clear all history commands from the settings file.

    Returns:
        dict: Updated hostory with empty history list.

    """
    settings _ model.l..()
    del settings["history"][:]
    model.save(settings)
    r_ settings


___ clear_combo(combo):
    """Ensure that the given combo has no elements.

    Using a single 'clear' does sometimes not clear all elements. Here we force
    the given combo to loose all its elements. We must however skip the "new"
    item because when we delete all elements, then the "new" item *will* be
    selected which will then trigger showing the 'New Stack' window.

    Args:
        combo (QtWidgets.QComboBox): ComboBox to flush.

    """
    w__ combo.count() > 2:
        __ combo.currentText __ NEW_STACK:
            c___
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
    seen _ set()
    seen_add _ seen.add
    r_ [x ___ x __ sequence __ no. (x __ seen or seen_add(x))]


___ open_website(url):
    """Open browser locating to given url."""
    __ ___.pl.. __ 'win32':
        # Under windows, the os module has this member.
        __.startfile(url)  # pylint: disable=no-member
    ____ ___.pl.. __ 'darwin':
        subprocess.P..(['open', url])
    ____
        ___
            subprocess.P..(['xdg-open', url])
        ______ OSError:
            msg _ ("Cannot open browser. Please open it manually and "
                   "navigate to:\n\n{}".f..(url))
            ____ smartScripter ______ dialogs
            dialogs.show_message_box(N.., msg)


___ assemble_command_path(command_name):
    """Assemble command path from current settings and command name."""

    settings _ model.l..()
    stack_root _ settings["stack_root"]
    current_stack _ settings["current_stack"]

    r_ __.pa__.j..(stack_root, current_stack, command_name)


___ get_all_stacks
    """Get all stack folders.

    Returns:
        list: Names of all stack folders.

    """
    settings _ model.l..()
    stack_root _ settings["stack_root"]

    r_ [name ___ name __ __.l_d_(stack_root)
            __ __.pa__.isd..(__.pa__.j..(stack_root, name))]


___ load_tooltips(parent, section):
    """Set tooltip for given parent from given section.

    Args:
        parent (QWidgets.QWidget): QWidget object to load tooltip for.
        section (str): Section from tooltips.json file.

    """
    # Load tooltips file.
    this_dir _ __.pa__.d_n_( -f)
    tooltips_file _ __.pa__.j..(this_dir, "data", "tooltips.json")
    tooltips_file _ __.pa__.n_p_(tooltips_file)
    __ no. __.pa__.isf..(tooltips_file):
        r_

    # Parse tool tips file.
    w__ o..(tooltips_file) __ json_file:
        ___
            ttdata _ j___.l..(json_file)
        ______ ValueError:
            r_

    # Find the tooltip.
    ___ widget __ parent.findChildren(?C...QObject):
        ___ element __ ttdata[section]:
            __ element["tt"] __ widget.property("tt"):
                widget.setToolTip("<strong>{}</strong><br />{}".f..(
                    element["ttt"], element["ttc"]))


___ get_tool_root(which):
    """Get public/private root directory path based on 'which'.

    Create directory if it does not exist.

    Args:
        which (str): Which tool root to get. ("private", "public")

    Returns:
        str: Absolute path of public/private tool root.

    """
    __ which __ "private":
        cragl_dir _ ".cragl"
    ____
        cragl_dir _ "cragl"

    root _ __.pa__.j..(__.pa__.e__("~"), cragl_dir, __product__)

    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______ IOError __ error:
            print "Error creating directory: ", error.m..

    r_ root


SESSION_ICONS _ get_session_icons()


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
        r_ [pa__ ___ pa__ __ SESSION_ICONS
                __ pa__.endswith("{}.png".f..(icon))][0]
    ______ IndexError:
        r_ load_icons()["command"]


___ reveal_in_explorer(pa__):
    """Reveal the given path in the explorer."""
    __ ___.pl.. __ 'darwin':
        subprocess.check_call(['open', '--', pa__])
    ____ ___.pl.. __ 'linux2':
        subprocess.P..(['xdg-open', pa__])
    ____ ___.pl.. __ 'windows' or ___.pl.. __ 'win32':
        ___
            subprocess.check_call(['explorer', pa__])
        # We want to catch all errors in here explicitly.
        ______ E.. __ error:  # pylint: disable=broad-except
            ____ smartScripter ______ dialogs
            m.. _ ("Unable to reveal the directory. Please open the "
                       "directory manually in your explorer. "
                       "{}".f..(error.m..))
            dialogs.show_message_box(m..)
