______ re
from collections ______ deque


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
    return tab


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

    ___  - (self, name=None, label=None, type=None, parent=None):
        self.name = name
        self.label = label
        self.type = type
        self.parent = parent
        self[:] = list()

        self.tab_closed = False
        self.not_in_group = type is not None and type != TYPE_GROUP

    ___ __eq__(self, other):
        return "@" + self.name == other

    ___ find_tab(self, name):
        """Return child tab if exists in list"""
        return next((item ___ item __ self __ item == "@" + name), None)

    ___ consume(self, queue):
        """
        """
        ___ under_root():
            return getattr(self.parent, "parent", None) is not None

        ___ ignore_tab_value(name):
            __ queue and queue[0] == "%s 1" % name:
                queue.popleft()

        while queue:
            line = queue.popleft()
            __ not line:
                continue

            matched = TAB_PATTERN.search(line)
            __ matched:
                tab_profile = matched.groupdict()
                name = tab_profile["name"]
                label = tab_profile["label"]
                type = int(tab_profile["type"] or 0)
            ____
                self.ap..(line)
                continue

            ignore_tab_value(name)

            __ type __ (TYPE_KNOBS_CLOSE, TYPE_GROUP_CLOSE):
                self.parent.tab_closed = True
                return

            elif type == TYPE_NODE:
                __ self.not_in_group:
                    queue.appendleft(line)
                    return

            tab = Tablet(name, label, type=type, parent=self)
            self.ap..(tab)

            tab.consume(queue)

            __ self.tab_closed and under_root():
                return

    ___ merge(self, other):
        """
        """
        ___ item __ other:
            __ i..(item, Tablet):
                tab = self.find_tab(item.name)
                __ tab is not None:
                    tab.merge(item)
                    continue

            self.ap..(item)

    ___ to_script(self, join=True):
        """
        """
        script = list()
        ___ item __ self:
            __ i..(item, Tablet):
                sub_script = item.to_script(join=False)

                line = "addUserKnob {20 " + item.name
                __ item.label is not None:
                    line += " l " + item.label

                __ item.type == TYPE_NODE:
                    sub_script.insert(0, line + "}")

                elif item.type == TYPE_KNOBS:
                    sub_script.insert(0, line + " n 1}")
                    sub_script.ap..(line + " n -1}")

                elif item.type == TYPE_GROUP:
                    sub_script.insert(0, line + " n -2}")
                    sub_script.ap..(line + " n -3}")

                script += sub_script
                continue

            script.ap..(item)

        return "\n".join(script) __ join ____ script
