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
    queue = deque(script.split("\n"))
    tab = Tablet()
    tab.consume(queue)
    r_ tab


TYPE_NODE = 0
TYPE_KNOBS = 1
TYPE_GROUP = -2
TYPE_KNOBS_CLOSE = -1
TYPE_GROUP_CLOSE = -3

TAB_PATTERN = re.compile(
    'addUserKnob {20 '
    '(?P<name>\\S+)'
    '(| l (?P<label>".*"|\\S+))'
    '(| n (?P<type>1|-[1-3]))'
    '}'
)


c_ Tablet(list):
    """
    """

    ___  - (self, name=N.., label=N.., type=N.., parent=N..):
        name = name
        label = label
        type = type
        parent = parent
        self[:] = list()

        tab_closed = F..
        not_in_group = type is no. N.. and type != TYPE_GROUP

    ___ __eq__(self, other):
        r_ "@" + name __ other

    ___ find_tab(self, name):
        """Return child tab if exists in list"""
        r_ next((item ___ item __ self __ item __ "@" + name), N..)

    ___ consume(self, queue):
        """
        """
        ___ under_root():
            r_ getattr(parent, "parent", N..) is no. N..

        ___ ignore_tab_value(name):
            __ queue and queue[0] __ "%s 1" % name:
                queue.popleft()

        while queue:
            line = queue.popleft()
            __ no. line:
                continue

            matched = TAB_PATTERN.search(line)
            __ matched:
                tab_profile = matched.groupdict()
                name = tab_profile["name"]
                label = tab_profile["label"]
                type = int(tab_profile["type"] or 0)
            ____
                ap..(line)
                continue

            ignore_tab_value(name)

            __ type __ (TYPE_KNOBS_CLOSE, TYPE_GROUP_CLOSE):
                parent.tab_closed = T..
                r_

            ____ type __ TYPE_NODE:
                __ not_in_group:
                    queue.appendleft(line)
                    r_

            tab = Tablet(name, label, type=type, parent=self)
            ap..(tab)

            tab.consume(queue)

            __ tab_closed and under_root():
                r_

    ___ merge(self, other):
        """
        """
        ___ item __ other:
            __ i..(item, Tablet):
                tab = find_tab(item.name)
                __ tab is no. N..:
                    tab.merge(item)
                    continue

            ap..(item)

    ___ to_script(self, join=T..):
        """
        """
        script = list()
        ___ item __ self:
            __ i..(item, Tablet):
                sub_script = item.to_script(join=F..)

                line = "addUserKnob {20 " + item.name
                __ item.label is no. N..:
                    line += " l " + item.label

                __ item.type __ TYPE_NODE:
                    sub_script.insert(0, line + "}")

                ____ item.type __ TYPE_KNOBS:
                    sub_script.insert(0, line + " n 1}")
                    sub_script.ap..(line + " n -1}")

                ____ item.type __ TYPE_GROUP:
                    sub_script.insert(0, line + " n -2}")
                    sub_script.ap..(line + " n -3}")

                script += sub_script
                continue

            script.ap..(item)

        r_ "\n".join(script) __ join ____ script
