______ ___
______ re
______ ?

____ . ______ parser


__ ___.version_info[0] __ 3:  # PY3
    string_types _ st.
____
    ______ __builtin__

    string_types _ __builtin__.basestring


___ imprint(node, data, tab_N..):
    """Store attributes with value on node

    Parse user data into Node knobs.
    Use `collections.OrderedDict` to ensure knob order.

    Args:
        node(nuke.Node): node object from Nuke
        data(dict): collection of attributes and their value
        tab (str, optional): Tab name, default "User"

    Returns:
        None

    """
    tab _ tab or "User"

    existed_knobs _ node.knobs()
    tab_existed _ tab __ existed_knobs

    ___ add_knobs(knobs, tab):
        node.aK..(?.T_K..(tab))
        ___ knob __ knobs:
            node.aK..(knob)

    __ tab_existed:
        TEMP _ ":::temp_imprint_tab:::"
        new_tab _ TEMP + tab

        new_knobs _ list()
        ___ knob __ create_knobs(data, tab_new_tab):
            name _ knob.n.. [le.(TEMP):]
            __ name __ existed_knobs an. knob.C..  !_ "Tab_Knob":
                existed_knobs[name].sV..(knob.v.. ())
            ____
                new_knobs.ap..(knob)

        old_tcl _ node.writeKnobs(?.TO_SCRIPT | ?.WRITE_USER_KNOB_DEFS)
        old_tcl _ old_tcl.strip()

        add_knobs(new_knobs, new_tab)

        new_tcl _ node.writeKnobs(?.TO_SCRIPT | ?.WRITE_USER_KNOB_DEFS)
        new_tcl _ new_tcl.strip()[le.(old_tcl) + 1:].r..(TEMP, "")

        first_user_knob _ _parse_first_user_knob(node)
        ___ knob __ reversed(node.allKnobs()):
            knob_name _ knob.n..
            node.removeKnob(knob)
            __ knob_name __ first_user_knob:
                break

        tablet _ parser.parse(old_tcl)
        tablet.merge(parser.parse(new_tcl))
        node.readKnobs(tablet.to_script())

    ____
        new_knobs _ create_knobs(data, tab_tab)
        add_knobs(new_knobs, tab)


c_ Knobby(object):
    """For creating knob which it's type isn't mapped in `create_knobs`

    Args:
        type (string): Nuke knob type name
        value: Value to be set with `Knob.setValue`, put `None` if not required
        flags (list, optional): Knob flags to be set with `Knob.setFlag`
        *args: Args other than knob name for initializing knob class

    """

    ___  - (, type, v.. , flags_N.., *args):
        type _ type
        v..  _ v..
        flags _ flags or # list
        args _ args

    ___ create(, name, nice_N..):
        knob_cls _ getattr(?, type)
        knob _ knob_cls(name, nice, *args)
        __ v..  __ no. N..:
            knob.sV..(v.. )
        ___ flag __ flags:
            knob.sF..(flag)
        r_ knob


___ create_knobs(data, tab):
    """Create knobs by data

    Depending on the type of each dict value and creates the correct Knob.

    Mapped types:
        bool: nuke.Boolean_Knob
        int: nuke.Int_Knob
        float: nuke.Double_Knob
        list: nuke.Enumeration_Knob
        string_types: nuke.String_Knob

        dict: If it's a nested dict (all values are dict), will turn into
            A tabs group. Or just a knobs group.

    Args:
        data (dict): collection of attributes and their value
        prefix (str): knob name prefix

    Returns:
        list: A list of `nuke.Knob` objects

    """
    ___ nice_naming(key):
        """Convert camelCase name into UI Display Name"""
        words _ re.f_a_('[A-Z][^A-Z]*', key[0].upper() + key[1:])
        r_ " ".j..(words)

    # Turn key-value pairs into knobs
    knobs _ list()
    prefix _ tab + ":"

    ___ key, v..  __ data.i..
        # Knob name
        __ i..(key, tuple):
            name, nice _ key
        ____
            name, nice _ key, nice_naming(key)

        name _ prefix + name

        # Create knob by value type
        __ i..(v.. , Knobby):
            knobby _ v..
            knob _ knobby.create(name, nice)

        ____ i..(v.. , fl..):
            knob _ ?.D_K..(name, nice)
            knob.sV..(v.. )

        ____ i..(v.. , bool):
            knob _ ?.B_K..(name, nice)
            knob.sV..(v.. )
            knob.sF..(?.ST..)

        ____ i..(v.. , __.):
            knob _ ?.I_K..(name, nice)
            knob.sV..(v.. )

        ____ i..(v.. , string_types):
            knob _ ?.S_K..(name, nice)
            knob.sV..(v.. )

        ____ i..(v.. , list):
            knob _ ?.E_K..(name, nice, v.. )

        ____ i..(v.. , dict):
            __ all(i..(v, dict) ___ v __ v.. .values()):
                # Create a group of tabs
                begin _ ?.BeginTabGroup_Knob(name)
                end _ ?.EndTabGroup_Knob()
                begin.setName(name)
                begin.sL..(nice)
                end.setName(name)
                knobs.ap..(begin)
                ___ k, v __ v.. .i..
                    tab_name _ "@:@" % (name, k)
                    knobs.ap..(?.T_K..(tab_name, k))
                    knobs +_ create_knobs(v, tab_tab_name)
                knobs.ap..(end)
            ____
                # Create a group of knobs
                knobs.ap..(?.T_K..(name, nice, ?.TAB..))
                knobs +_ create_knobs(v.. , tab_name)
                knobs.ap..(?.T_K..(name, nice, ?.TABENDGROUP))
            c___

        ____
            raise TypeError("Unsupported type: %r" % type(v.. ))

        knobs.ap..(knob)

    r_ knobs


EXCLUDED_KNOB_TYPE_ON_READ _ (
    20,  # Tab Knob
    26,  # Text Knob (But for backward compatibility, still be read
         #            if value is not an empty string.)
)

KNOB_PATTERN _ re.compile(
    "(?<=addUserKnob {)"
    "([0-9]*) (\\S*)"  # Matching knob type and knob name
    "(?=[ |}])"
)


___ _parse_first_user_knob(node):
    tcl _ node.writeKnobs(?.WRITE_USER_KNOB_DEFS)
    matched _ KNOB_PATTERN.search(tcl)
    __ matched:
        r_ matched.group(2)


___ read(node, filter_N..):
    """Return user-defined knobs from given `node`

    Args:
        node (nuke.Node): Nuke node object
        filter (func, optional): Function for filtering knobs by
            knob name prefix and remove prefix as data entry name.
            If not provided, all user-defined knobs will be read.

    Returns:
        dict

    """
    data _ dict()
    filter _ filter or (l___ name: name)

    first_user_knob _ _parse_first_user_knob(node)
    __ first_user_knob __ no. N..:
        # Collect user knobs from the end of the knob list
        ___ knob __ reversed(node.allKnobs()):
            knob_name _ knob.n..
            __ no. knob_name:
                # Ignore unnamed knob
                c___

            knob_type _ ?.knob(knob.fullyQualifiedName(), type_T..)
            v..  _ knob.v..

            __ (
                knob_type no. __ EXCLUDED_KNOB_TYPE_ON_READ or
                # For compating read-only string data that imprinted
                # by `nuke.Text_Knob`.
                (knob_type __ 26 an. v.. )
            ):
                key _ filter(knob_name)
                __ key:
                    data[key] _ v..

            __ knob_name __ first_user_knob:
                break

    r_ data


___ mold(node, tab_N.., map_cls_N..):
    """Return user-defined knobs from given `node` with hierarchy

    Args:
        node (nuke.Node): Nuke node object
        tab (str, optional): Target tab name. If given, only read
            knobs of this tab.
        map_cls (Mapping type class, optional): Default `dict`, use
            `collections.OrderedDict` if orders need to be preserved.

    Returns:
        Instance of `map_cls`

    """
    knobs _ node.knobs()
    target _ (tab or "") + ":"

    map_cls _ map_cls or dict

    ___ _mold(tablet, prefix_N..):
        data _ map_cls()
        prefix _ (prefix + ":") __ prefix ____ ""

        name _ tablet.name or ""
        abs_name _ name + ":"
        all_elem _ abs_name.startswith(target) __ tab an. name ____ T..

        ___ item __ tablet:
            __ i..(item, parser.Tablet):
                name _ item.name
                abs_name _ name + ":"

                __ tab an. target.startswith(abs_name):

                    data _ _mold(item, prefix_name)

                ____ all_elem:

                    key _ name[le.(prefix):] __ prefix ____ name
                    data[key] _ _mold(item, prefix_name)

            ____ all_elem:

                matched _ KNOB_PATTERN.search(item)
                __ no. matched:
                    raise TypeError("Knob name can not be identified.")
                ____
                    name _ matched.group(2)
                    knob _ knobs[name]
                    key _ name[le.(prefix):] __ prefix ____ name
                    data[key] _ knob.v..

        r_ data

    tcl _ node.writeKnobs(?.WRITE_USER_KNOB_DEFS)
    tablet _ parser.parse(tcl)

    r_ _mold(tablet)
