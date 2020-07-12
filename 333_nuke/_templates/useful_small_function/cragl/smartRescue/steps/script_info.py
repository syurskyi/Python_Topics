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
______ d_t_
______ __

# Import third-party modules
______ ?  # pylint: disable=______-error

# Import local modules
____ smartRescue.base_steps ______ NodeStep

# Template to use for info creation.
_TEMPLATE _ """Report for {working_file_name}
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
    path_knobs _ (
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
        r_ "{:%Y/%m/%d - %H:%M:%S}".f..(d_t_.d_t_.now())

    @staticmethod
    ___ number_nodes(recursive_F..):
        """Return the total number of nodes.

        Args:
            recursive (bool, optional): If True process recursively, including
                also nodes inside groups.

        Returns:
            int: The total number of nodes.

        """
        r_ le.(?.allNodes(recurseGroups_recursive))

    @staticmethod
    ___ frame_range():
        """Get the first and last frame of the working file.

        Returns:
            int, int, The first and last frame of the working file.

        """
        first_frame _ int(?.root()["first_frame"].value())
        last_frame _ int(?.root()["last_frame"].value())
        r_ first_frame, last_frame

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
            __ knob_name __ "format":
                format_ _ "{} ({}x{} {})"
                format_knob _ knob.v..
                r_ format_.f..(format_knob.name(), format_knob.width(),
                                      format_knob.height(),
                                      format_knob.pixelAspect())
            # Implement extraction for other nodes in here.
            # elif knob_name == "xxx":
            #     # Extract values.
            r_ knob.v.. or "---"

        root_values _ []
        ___ knob_name __ setup["root_info"]:
            knob _ ?.root().knob(knob_name)
            __ no. knob:
                continue

            value _ _format_value(knob_name, knob)
            root_values.ap..((knob_name, value))

        r_ tuple(root_values)

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
        footage _ []
        ___ node __ ?.allNodes(recurseGroups_T..):
            ___ knob_name __ path_knobs:
                path_knob _ node.knob(knob_name)
                __ no. path_knob:
                    continue
                path _ path_knob.evaluate() or "---"
                footage.ap..((node.name(), path))

        r_ tuple(footage)

    @staticmethod
    ___ all_node_classes():
        """Get a set of all node classes

        Returns:
            set: All node classes

        """
        all_nodes _ ?.allNodes(recurseGroups_T..)
        r_ sorted(set(node.Class() ___ node __ all_nodes))

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
        stats _ []
        list_node_classes _ setup["number_nodes_by_class"]
        __ list_node_classes:
            node_classes _ list_node_classes
        ____
            node_classes _ all_node_classes()

        ___ node_class __ sorted(node_classes):
            counter _ 0
            ___ node __ ?.allNodes(recurseGroups_T..):
                __ node.Class() __ node_class:
                    counter +_ 1
            stats.ap..((node_class, counter))

        r_ tuple(stats)

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
        r_ "{}: {}".f..(tuple_[0], tuple_[1])

    ___ process
        """Generate the working file info."""
        copy_basename _ "{}_info.txt".f..(basename)
        info_path _ __.path.join(parent_dir, copy_basename)

        logger.info("Creating information file %s", info_path)

        w__ o..(info_path, "w") __ dest:
            separator _ "-" * 50
            first_frame, last_frame _ frame_range()
            root_values _ "\n".join(
                [tuple_to_human_readable(root_value)
                 ___ root_value __ root_values()]
            )
            footages _ "\n".join(
                [tuple_to_human_readable(footage)
                 ___ footage __ footage_paths()]
            )
            node_classes_stats _ "\n".join(
                [tuple_to_human_readable(stat)
                 ___ stat __ len_nodes_by_class()]
            )

            content _ _TEMPLATE.f..(
                working_file_name_basename,
                date_date,
                separator_separator,
                first_frame_first_frame,
                last_frame_last_frame,
                root_values_root_values,
                number_nodes_number_nodes(),
                number_nodes_recursive_number_nodes(recursive_T..),
                footages_footages,
                node_classes_stats_node_classes_stats
            )
            dest.write(content)
