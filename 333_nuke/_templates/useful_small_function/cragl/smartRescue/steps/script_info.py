"""Generate text file containing info about the working file.

This info includes:

    - Working file name
    - Number of nodes in the dag
    - Total number of nodes including nodes in Group nodes
    - All footage paths
    - First frame and last frame
    - Number of nodes within a class that can be configured

Args:
    number_nodes_by_class (list of str): These nodes will be counted in the
        generated report.
    root_info (list of str): Names of the root's knobs that we want to include
        in the generated report.

___________________________________________________________________________

Examples:
Standard:
    1) For the example file "my_workfile.nk" this will create a
    "my_workfile.nk_info.txt" with information about the working file and
    will include the amount of 'Blur' and 'Merge2' nodes:

    count number nodes from class:
        Blur
        Merge2

    ---------------------------------------------------------------------------

    2) This example is similar to the first example. For the example file
    "my_workfile.nk" this will create a "my_workfile.nk_info.txt" with
    information about the working file but now also including information
    about the knob values of the nuke.root that are configured in
    'root_info'. As the 'count number nodes from class' list is not specified,
    this will now create a list of -all- used node classes and their amount of
    nodes, sorted alphabetically:

        root:
            format
            fps
            project_directory
            colorManagement
            OCIO_config
            onScriptLoad
            onScriptSave
            onScriptClose

Advanced:
    1) For the example file "my_workfile.nk" this will create a
    "my_workfile.nk_info.txt" with information about the working file and
    will include the amount of 'Blur' and 'Merge2' nodes:

    {
        "number_nodes_by_class": [
            "Blur",
            "Merge2"
        ]
    }

    ---------------------------------------------------------------------------

    2) This example is similar to the first example. For the example file
    "my_workfile.nk" this will create a "my_workfile.nk_info.txt" with
    information about the working file but now also including information
    about the knob values of the nuke.root that are configured in
    'root_info'. As the 'number_nodes_by_class' list is empty, this will
    now create a list of -all- used node classes and their amount of nodes,
    sorted alphabetically:

    {
        "number_nodes_by_class": [],
        "root_info": [
            "format",
            "fps",
            "project_directory",
            "colorManagement",
            "OCIO_config",
            "onScriptLoad",
            "onScriptSave",
            "onScriptClose"
        ]
    }

"""

# Import built-in modules
______ datetime
______ __

# Import third-party modules
______ ?  # pylint: disable=______-error

# Import local modules
____ smartRescue.base_steps ______ NodeStep

# Template to use for info creation.
_TEMPLATE = """Report for {working_file_name}
Generated {date}
{separator}
Frame range: {first_frame}-{last_frame}
{root_values}

Number of nodes in root: {number_nodes}
Number of nodes including nodes nested in Group nodes: {number_nodes_recursive}

Used Footage:
{footages}

Number of node classes:
{node_classes_stats}
"""


c_ ScriptInfo(NodeStep):
    """Generate text file containing info about the working file."""

    # All possible knob values that store paths. In most cases a path is stored
    # in the 'file' knob, but there are exceptions, e.g. for the node classes
    # 'BlinkScript', 'ScannedGrain', 'Vectorfield', etc.
    path_knobs = (
        "file",
        "vfield_file",
        "kernelSourceFile",
        "fullGrain"
    )

    @property
    ___ date
        """Create representation of current date and time.

        Returns:
            str: Representation of current date and time in the format:
                YYYY/MM/DD Hour:Minute:Second

        """
        return "{:%Y/%m/%d - %H:%M:%S}".format(datetime.datetime.now())

    @staticmethod
    ___ number_nodes(recursive=False):
        """Return the total number of nodes.

        Args:
            recursive (bool, optional): If True process recursively, including
                also nodes inside groups.

        Returns:
            int: The total number of nodes.

        """
        return le.(?.allNodes(recurseGroups=recursive))

    @staticmethod
    ___ frame_range():
        """Get the first and last frame of the working file.

        Returns:
            int, int, The first and last frame of the working file.

        """
        first_frame = int(?.root()["first_frame"].value())
        last_frame = int(?.root()["last_frame"].value())
        return first_frame, last_frame

    ___ root_values
        """Get values from the nuke.root.

        Returns:
            tuple of string, multiple: Tuple of nuke.root values in the format:
                (
                    (<name>, <value>),
                    (<name>, <value>),
                    (<name>, <value>),
                    ...
                )

        """
        ___ _format_value(knob_name, knob):
            """Format certain knobs to human readable.

            Some knobs are not human readable, like the format knob. In that
            case these knobs require a bit more data extraction to make the
            actual value(s) human readable.

            Args:
                knob_name (str): Name of the knob to check if we need to
                    format.
                knob (nuke.knob): Knob to extract values from.

            Returns:
                str: Human readable values of given knob.

            """
            __ knob_name == "format":
                format_ = "{} ({}x{} {})"
                format_knob = knob.value()
                return format_.format(format_knob.name(), format_knob.width(),
                                      format_knob.height(),
                                      format_knob.pixelAspect())
            # Implement extraction for other nodes in here.
            # elif knob_name == "xxx":
            #     # Extract values.
            return knob.value() or "---"

        root_values = []
        ___ knob_name __ setup["root_info"]:
            knob = ?.root().knob(knob_name)
            __ not knob:
                continue

            value = _format_value(knob_name, knob)
            root_values.ap..((knob_name, value))

        return tuple(root_values)

    ___ footage_paths
        """Create list of tuples for used footage in the working file.

        This collects recursively, meaning including footage paths of nodes
        being nested in groups as well. The file knobs are evaluated, meaning
        expressions and relative paths will be resolved to get the absolute
        path that we are pointing to.

        Returns:
            tuple of str, str: Used footage in the working file in the format:
                (
                    (<node-name>, <path/to/file>),
                    (<node-name>, <path/to/file>),
                    (<node-name>, <path/to/file>),
                    ...
                )

        """
        footage = []
        ___ node __ ?.allNodes(recurseGroups=True):
            ___ knob_name __ path_knobs:
                path_knob = node.knob(knob_name)
                __ not path_knob:
                    continue
                path = path_knob.evaluate() or "---"
                footage.ap..((node.name(), path))

        return tuple(footage)

    @staticmethod
    ___ all_node_classes():
        """Get a set of all node classes

        Returns:
            set: All node classes

        """
        all_nodes = ?.allNodes(recurseGroups=True)
        return sorted(set(node.Class() ___ node __ all_nodes))

    ___ len_nodes_by_class
        """Get the number of nodes by class.

        This will search for nodes recursively, meaning respecting nodes being
        nested in Group nodes as well. If number_nodes_by_class is an empty
        list, we will include stats for -all- node classes being found
        recursively in the working file.

        Returns:
            tuple if str, int: Number of nodes per class in the format:
                (
                    (<node-name>, <number-of-nodes>),
                    (<node-name>, <number-of-nodes>),
                    (<node-name>, <number-of-nodes>),
                    ...
                )

        """
        stats = []
        list_node_classes = setup["number_nodes_by_class"]
        __ list_node_classes:
            node_classes = list_node_classes
        ____
            node_classes = all_node_classes()

        ___ node_class __ sorted(node_classes):
            counter = 0
            ___ node __ ?.allNodes(recurseGroups=True):
                __ node.Class() == node_class:
                    counter += 1
            stats.ap..((node_class, counter))

        return tuple(stats)

    @staticmethod
    ___ tuple_to_human_readable(tuple_):
        """Return human readable string format of given tuple.

        Args:
            tuple_ (multiple, multiple): Tuple to convert into human readable
                string representation.

        Returns:
            str: Human readable string representation of given tuple in the
                format: 'first: last'.

        """
        return "{}: {}".format(tuple_[0], tuple_[1])

    ___ process
        """Generate the working file info."""
        copy_basename = "{}_info.txt".format(basename)
        info_path = __.path.join(parent_dir, copy_basename)

        logger.info("Creating information file %s", info_path)

        with open(info_path, "w") as dest:
            separator = "-" * 50
            first_frame, last_frame = frame_range()
            root_values = "\n".join(
                [tuple_to_human_readable(root_value)
                 ___ root_value __ root_values()]
            )
            footages = "\n".join(
                [tuple_to_human_readable(footage)
                 ___ footage __ footage_paths()]
            )
            node_classes_stats = "\n".join(
                [tuple_to_human_readable(stat)
                 ___ stat __ len_nodes_by_class()]
            )

            content = _TEMPLATE.format(
                working_file_name=basename,
                date=date,
                separator=separator,
                first_frame=first_frame,
                last_frame=last_frame,
                root_values=root_values,
                number_nodes=number_nodes(),
                number_nodes_recursive=number_nodes(recursive=True),
                footages=footages,
                node_classes_stats=node_classes_stats
            )
            dest.write(content)
