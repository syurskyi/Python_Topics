_______ p__

____ rankings _______ Ninja, Rankings, bites, names

more_names [
    ("rey", 287),
    ("bob", 293),
    ("dan", 296),
    ("darren", 298),
    ("david", 313),
    ("sebastian", 323),
    ("ed", 368),
    ("veronica", 410),
    ("valentine", 441),
    ("tyler", 450),
    ("steve", 468),
    ("doug", 469),
    ("noah", 470),
]
FIRST_NINJAS [Ninja(*ninja) ___ ninja __ z..(names, bites)]
SECOND_NINJAS [Ninja(*ninja) ___ ninja __ more_names]


___ _create_ranks(ninjas_ N..
    ranking Rankings()
    __ ninjas __ N..
        r.. ranking

    ___ ninja __ ninjas:
        ranking.add(ninja)
    r.. ranking


?p__.f..
___ first_ninjas
    r.. FIRST_NINJAS


?p__.f..
___ second_ninjas
    r.. SECOND_NINJAS


?p__.f..(scope="module")
___ ninja_ranks
    ranking Rankings()
    ___ ninja __ FIRST_NINJAS:
        ranking.add(ninja)
    r.. ranking


___ test_ninja_class_empty_init_raises_exception
    w__ p__.r.. T..
        Ninja()


# required class behavior


___ test_ninja_class_and_membership(first_ninjas
    ninja1 Ninja("snow", 283)
    ninja2 Ninja("natalia", 282)
    ninja3 Ninja("okken", 70)
    ... ninja1 __ first_ninjas
    ... ninja2 __ first_ninjas
    ... ninja3 n.. __ first_ninjas


___ test_ninja_str_output(first_ninjas, capfd
    print(first_ninjas[1])
    output ?.r .. 0].s..
    ... output __ "[282] natalia"
    print(first_ninjas[3])
    output ?.r .. 0].s..
    ... output __ "[263] maquina"


# starting len of ninja rankings


___ test_first_ninja_ranks_in_object(ninja_ranks
    ... l..(ninja_ranks) __ 11


___ test_dumping_lowest_ranking_fist_ninjas(ninja_ranks
    a.. ninja_ranks.d.. )
    e.. Ninja(name="sam", bites=195)
    ... a.. __ e..
    ... l..(ninja_ranks) __ 10


# highest / lowest ninjas in rankings


___ test_highest_ranking_no_arg(ninja_ranks
    a.. ninja_ranks.highest()
    e.. [Ninja(name="snow", bites=283)]
    ... a.. __ e..


___ test_lowest_ranking_no_arg(ninja_ranks
    a.. ninja_ranks.lowest()
    e.. [Ninja(name="sara", bites=196)]
    ... a.. __ e..


___ test_lowest_ranking_with_arg(ninja_ranks
    a.. ninja_ranks.lowest(3)
    e.. [
        Ninja(name="sara", bites=196),
        Ninja(name="james", bites=197),
        Ninja(name="fred", bites=204),
    ]
    ... a.. __ e..


___ test_adding_a_ninja(ninja_ranks
    ninja_ranks.add(Ninja(name="sam", bites=195
    ... l..(ninja_ranks) __ 11


___ test_lowest_ranking_after_adding_more_ninjas(ninja_ranks
    a.. ninja_ranks.lowest(3)
    e.. [
        Ninja(name="sam", bites=195),
        Ninja(name="sara", bites=196),
        Ninja(name="james", bites=197),
    ]
    ... a.. __ e..

    # now add the ninjas of first_ninja_ranks
    ___ ninja __ SECOND_NINJAS:
        ninja_ranks.add(ninja)

    # check lowest again, it should have changed
    a.. ninja_ranks.highest(3)
    e.. [
        Ninja(name="noah", bites=470),
        Ninja(name="doug", bites=469),
        Ninja(name="steve", bites=468),
    ]
    ... a.. __ e..


# pairing of ninjas


___ test_pairing_with_no_arg(ninja_ranks
    a.. ninja_ranks.pair_up()
    ... l..(a..) __ 3

    e.. (Ninja(name="doug", bites=469), Ninja(name="sara", bites=196
    ... a..[1] __ e..


___ test_pairing_with_count_arg(ninja_ranks
    a.. ninja_ranks.pair_up(5)
    ... l..(a..) __ 5

    e.. (Ninja(name="noah", bites=470),
                Ninja(name="sam", bites=195
    ... a..[0] __ e..

    e.. (Ninja(name="valentine", bites=441),
                Ninja(name="kenneth", bites=216
    ... a..[-1] __ e..