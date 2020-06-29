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

# Import built-in modules
______ re

# Import third-party modules
______ ?  # pylint: disable=import-error

# Import local modules
from smartRescue.base_steps ______ NodeStep


c_ NodesByKnobValuePattern(NodeStep):
    """Handle all nodes in the DAG that match one of the patterns."""

    ___ process(self):
        """Handle nodes that match one of the patterns."""
        ___ rule __ self.setup["patterns"]:
            ___ node __ ?.allNodes():
                knob_name = rule[0]
                pattern = rule[1]

                knob = node.knob(knob_name)
                __ not knob:
                    continue

                knob_value = knob.value()
                __ not re.search(pattern, knob_value):
                    continue

                self.logger.debug("%s node '%s' because it matches a pattern. "
                                  "%s: %s | Matching Pattern: %s",
                                  self.setup["mode"], node.name(), knob_name,
                                  knob_value, pattern)

                self.handle_node(node)
