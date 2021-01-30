"""Handle nodes in the DAG matching one of the knob rules.

This will search all nodes in the DAG. If any node contains the following knob
and the operator matches the given value then we handle the node as configured.

The following operators are supported:
    ==    equal
    !=    not equal
    <     less than
    <=    less than or equal
    >     greater than
    >=    greater than or equal

Args:
    mode (str): Choose how to handle matching nodes.
        disable: Will disable nodes.
        delete: Will delete nodes.
        disconnect: Will disconnect the nodes from the stream.
    knob_rules (list of dict): Rules to apply to the process in the format:
        [
            {
                "node_class": <name of the class to consider>
                "knob_name": <name of the knob>
                "operator": <operator to use for a match>
                "knob_value": <knob value to match>
            },
            ...
        ]

___________________________________________________________________________

Examples:

Standard:
    1) Delete all nodes of node class 'Defocus' where the 'size' knob is
    'greater than' the value of '50':

    mode: delete
        node class: Defocus
        knob name: size
        operator: >
        knob value: 50

    ------------------------------------------------------------------------

    2) Disable all nodes of the node class 'Merge2' where the 'mix' knob's
    value is 'equal' to '0.3':

    mode: disable
        node class: Merge2
        knob name: mix
        operator: ==
        knob value: 0.3

    3) Disconnect all nodes of the node class 'Defocus' where the 'defocus'
    knob's value is 'greater than' the value of '100' and all nodes of the
    node class 'Blur' where the 'size' knob's value is 'greater than' the
    value of '100':

    mode: disable
        node class: Defocus
        knob name: defocus
        operator: >
        knob value: 100

        node class: Blur
        knob name: size
        operator: >
        knob value: 100

Advanced:

    1) Delete all nodes of node class 'Defocus' where the 'size' knob is
    'greater than' the value of '50':

    {
        "mode": "delete",
        "knob_rules": [
            {
                "node_class": "Defocus",
                "knob_name": "size",
                "operator": ">",
                "knob_value": "50"
            }
        ]
    }

    ---------------------------------------------------------------------------

    2) Disable all nodes of the node class 'Merge2' where the 'mix' knob's
    value is 'equal' to '0.3':

    {
        "mode": "disable",
        "knob_rules": [
            {
                "node_class": "Merge2",
                "knob_name": "mix",
                "operator": "==",
                "knob_value": "0.3"
            }
        ]
    }

    ---------------------------------------------------------------------------

    3) Disconnect all nodes of the node class 'Defocus' where the 'defocus'
    knob's value is 'greater than' the value '100' and all nodes of the node
    class 'Blur' where the 'size' knob's value is 'greater than' the value
    of '100':

    {
        "mode": "disable",
        "knob_rules": [
            {
                "node_class": "Defocus",
                "knob_name": "defocus",
                "operator": ">",
                "knob_value": "100"
            },
            {
                "node_class": "Blur",
                "knob_name": "size",
                "operator": ">",
                "knob_value": "100"
            }
        ]
    }

"""

# _____ built-in modules
______ operator

# _____ third-party modules
______ ?  # pylint: disable=______-error

# _____ local modules
____ smartRescue.base_steps ______ NodeStep


c_ NodesByKnobValues(NodeStep):
    """Handle nodes in the DAG matching the knob names and value conditions."""

    operators _ {
        "==": operator.eq,
        "!=": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge
    }

    ___ process
        """Handle nodes that match one of the knob rules."""
        ___ rule __ setup["knob_rules"]:
            ___ node __ ?.allNodes

                __ node.Class() !_ rule["node_class"]:
                    c___

                knob _ node.knob(rule["knob_name"])
                __ no. knob:
                    c___

                operator_ _ operators.get(rule["operator"])
                __ no. operator_:
                    logger.waring("Non supported operator '@'. Skip "
                                       "step", rule["operator"])

                # At this stage, we must check against different types of knob
                # values. Simply checking against one specific type might run
                # into missing rules that are matching. For instance, we want
                # to be able to check against knobs holding integer values,
                # but also holding string values.
                types _ (
                    float,
                    __.,
                    st.,
                )

                rule_matched _ F..
                ___ type_ __ types:
                    ___
                        __ operator_(knob.v.., type_(rule["knob_value"])):
                            rule_matched _ T..
                            break
                    # We raise any error that occurs here. When any error
                    # occurs while casting the value then this is invalid data
                    # that we must not proceed with as it will be giving us
                    # unwanted results.
                    ______ E..:  # pylint: disable=broad-except
                        c___

                __ rule_matched:
                    logger.info(
                        "@ node '@' (@) because a rule matches the knob "
                        "value. Current value '@'. "
                        "Matching Rule: @.@ @ @",
                        setup["mode"],
                        node.n.. ,
                        node.Class(),
                        knob.v..,
                        rule["node_class"],
                        rule["knob_name"],
                        rule["operator"],
                        rule["knob_value"]
                    )

                    handle_node(node)
