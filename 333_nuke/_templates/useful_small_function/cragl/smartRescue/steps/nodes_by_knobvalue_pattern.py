r"""Handle all nodes in the DAG that knob names match one of the patterns.

This will iterate over all nodes and check if the given key (knob name) exists
and checks if the pattern for that knob matches in the knob's value. To check
the node name itself, we can use the node's 'name' knob, which contains the
name of the node.

Args:
    mode (str): Choose how to handle matching nodes.
        disable: Will disable nodes.
        delete: Will delete nodes.
        disconnect: Will disconnect the nodes from the stream.
    patterns (list of list): List of knob names and patterns to match in the
        format:
        [
            [<knobname>, <pattern to match>],
            [<knobname>, <pattern to match>],
            ...
        ]

___________________________________________________________________________

Examples:

Standard:
    1) Disables all 'Text' nodes (i.e. current 'Text2' node) and legacy 'Text'
    nodes (i.e. 'Text') as well as all Tracker nodes (i.e. current
    'Tracker4' node) and all legacy Tracker nodes (i.e. 'Tracker', is there
    no 'Tracker2'?), 'Tracker3'):

    mode: delete
    patterns:
        name -> ^Text\d*$
        name -> ^Tracker\d*+$"

    ------------------------------------------------------------------------

    2) Deletes all 'IBKColour' and 'IBKGizmo' nodes:

    mode: delete
    patterns:
        name -> ^IBK\w+$

    ------------------------------------------------------------------------

    3) Deletes all nodes that have 'heavy' in their label. Explicitly kept open
    by not using '^' at the pattern beginning and not using '$' at the
    pattern end, so that 'heavy' and 'lorem ipsum heavy dolor sit amet' will
    both match:

    mode: delete
    patterns:
        label -> heavy

Advanced:
    1) Disables all 'Text' nodes (i.e. current 'Text2' node) and legacy 'Text'
    nodes (i.e. 'Text') as well as all Tracker nodes (i.e. current
    'Tracker4' node) and all legacy Tracker nodes (i.e. 'Tracker', is there
    no 'Tracker2'?), 'Tracker3'):

    {
        "mode": "delete",
        "patterns": [
            ["name", "^Text\\d*$"],
            ["name", "^Tracker\\d*+$"]
        ]
    }

    ---------------------------------------------------------------------------

    2) Deletes all 'IBKColour' and 'IBKGizmo' nodes:

    {
        "mode": "delete",
        "patterns": [
            ["name", "^IBK\\w+$"]
        ]
    }

    ---------------------------------------------------------------------------

    3) Deletes all nodes that have 'heavy' in their label. Explicitly kept open
    by not using '^' at the pattern beginning and not using '$' at the
    pattern end, so that 'heavy' and 'lorem ipsum heavy dolor sit amet' will
    both match:

    {
        "mode": "delete",
        "patterns": [
          {
            "label": "heavy"
          }
        ]
    }

"""

# _____ built-in modules
______ re

# _____ third-party modules
______ ?  # pylint: disable=______-error

# _____ local modules
____ smartRescue.base_steps ______ NodeStep


c_ NodesByKnobValuePattern(NodeStep):
    """Handle all nodes in the DAG that match one of the patterns."""

    ___ process
        """Handle nodes that match one of the patterns."""
        ___ rule __ setup["patterns"]:
            ___ node __ ?.aN..
                knob_name _ rule[0]
                pattern _ rule[1]

                knob _ node.knob(knob_name)
                __ no. knob:
                    c___

                knob_value _ knob.v..
                __ no. re.search(pattern, knob_value):
                    c___

                logger.debug("@ node '@' because it matches a pattern. "
                                  "@: @ | Matching Pattern: @",
                                  setup["mode"], node.n.. , knob_name,
                                  knob_value, pattern)

                handle_node(node)
