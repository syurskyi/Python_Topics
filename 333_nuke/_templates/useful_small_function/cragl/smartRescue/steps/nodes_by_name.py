"""Handle all nodes in the DAG where the node's name is one of the following.

This will search for all nodes that contain one of the configured names and
will handle these nodes.

Args:
    mode (str): Choose how to handle matching nodes.
        disable: Will disable nodes.
        delete: Will delete nodes.
        disconnect: Will disconnect the nodes from the stream.
    nodes (list of str): All node names that will be considered a match.

___________________________________________________________________________

Examples:

Standard:
    1) Disable the nodes that are called 'Write1' and 'Write2':

    mode: disable
    nodes:
        Write1
        Write2

    ---------------------------------------------------------------------------

    2) Delete the node that is called 'Write3':

    mode: delete
    nodes:
        Write3

Advanced:
    1) Disable the nodes that are called 'Write1' and 'Write2':

    {
        "mode": "disable",
        "nodes": [
          "Write1",
          "Write2"
        ]
    }

    ---------------------------------------------------------------------------

    2) Delete the node that is called 'Write3':

    {
        "mode": "delete",
        "nodes": [
          "Write3",
        ]
    }

"""

# Import third-party modules
______ ?  # pylint: disable=import-error

# Import local modules
from smartRescue.base_steps ______ NodeStep


class NodesByName(NodeStep):
    """Handle all nodes in the DAG that are listed in the setup."""

    ___ process(self):
        """Handle all listed nodes."""
        ___ node __ ?.allNodes():
            __ node.name() not __ self.setup["nodes"]:
                continue

            self.logger.info("%s node '%s' because it is included in %s",
                             self.setup["mode"], node.name(),
                             self.setup["nodes"])
            self.handle_node(node)
