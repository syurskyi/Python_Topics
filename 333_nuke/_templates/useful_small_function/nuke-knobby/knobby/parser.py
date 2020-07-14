______ re
____ collections ______ deque


___ parse(script):
    """Parse Nuke node's TCL script string into nested list structure

    Args:
        script (str): Node knobs TCL script string

    Returns:
        Tablet: A list containing knob scripts or tab knobs that has parsed
            into list

    """
    queue _ deque(script.split("\n"))
    tab _ Tablet()
    tab.consume(queue)
    r_ tab


TYPE_NODE _ 0
TYPE_KNOBS _ 1
TYPE_GROUP _ -2
TYPE_KNOBS_CLOSE _ -1
TYPE_GROUP_CLOSE _ -3

TAB_PATTERN _ re.compile(
    'addUserKnob {20 '
    '(?P<name>\\S+)'
    '(| l (?P<label>".*"|\\S+))'
    '(| n (?P<type>1|-[1-3]))'
    '}'
)


c_ Tablet(list):
    """
    """

    ___  - (self, name_N.., label_N.., type_N.., parent_N..):
        name _ name
        label _ label
        type _ type
        parent _ parent
        self[:] _ list()

        tab_closed _ F..
        not_in_group _ type __ no. N.. an. type !_ TYPE_GROUP

    ___ __eq__(self, other):
        r_ "@" + name __ other

    ___ find_tab(self, name):
        """Return child tab if exists in list"""
        r_ next((item ___ item __ self __ item __ "@" + name), N..)

    ___ consume(self, queue):
        """
        """
        ___ under_root():
            r_ getattr(parent, "parent", N..) __ no. N..

        ___ ignore_tab_value(name):
            __ queue an. queue[0] __ "@ 1" % name:
                queue.popleft()

        while queue:
            line _ queue.popleft()
            __ no. line:
                c___

            matched _ TAB_PATTERN.search(line)
            __ matched:
                tab_profile _ matched.groupdict()
                name _ tab_profile["name"]
                label _ tab_profile["label"]
                type _ in.(tab_profile["type"] or 0)
            ____
                ap..(line)
                c___

            ignore_tab_value(name)

            __ type __ (TYPE_KNOBS_CLOSE, TYPE_GROUP_CLOSE):
                parent.tab_closed _ T..
                r_

            ____ type __ TYPE_NODE:
                __ not_in_group:
                    queue.appendleft(line)
                    r_

            tab _ Tablet(name, label, type_type, parent_self)
            ap..(tab)

            tab.consume(queue)

            __ tab_closed an. under_root():
                r_

    ___ merge(self, other):
        """
        """
        ___ item __ other:
            __ i..(item, Tablet):
                tab _ find_tab(item.name)
                __ tab __ no. N..:
                    tab.merge(item)
                    c___

            ap..(item)

    ___ to_script(self, join_T..):
        """
        """
        script _ list()
        ___ item __ self:
            __ i..(item, Tablet):
                sub_script _ item.to_script(join_F..)

                line _ "addUserKnob {20 " + item.name
                __ item.label __ no. N..:
                    line +_ " l " + item.label

                __ item.type __ TYPE_NODE:
                    sub_script.insert(0, line + "}")

                ____ item.type __ TYPE_KNOBS:
                    sub_script.insert(0, line + " n 1}")
                    sub_script.ap..(line + " n -1}")

                ____ item.type __ TYPE_GROUP:
                    sub_script.insert(0, line + " n -2}")
                    sub_script.ap..(line + " n -3}")

                script +_ sub_script
                c___

            script.ap..(item)

        r_ "\n".j..(script) __ j.. ____ script
