_______ p__

____ game _______ get_winner

PLAYERS = ("Rock Gun Lightning Devil Dragon Water Air Paper Sponge "
           "Wolf Tree Human Snake Scissors Fire").s.. 


?p__.m__.p.("args", [('Rock', 'blabla'),
                                  ('blabla', 'Rock')])
___ test_bad_inputs(args
    w__ p__.r..(ValueError
        get_winner(*args)


?p__.m__.p.("player", PLAYERS)
___ test_ties(player
    ... get_winner(player, player) __ 'Tie'


# all 105 outcomes
# http://www.umop.com/rps15.htm

___ test_rock_pounds_out_fire
    ... get_winner('Rock', 'Fire') __ 'Rock'


?p__.m__.p.("player",  'Scissors', 'Snake', 'Human',
                                    'Wolf', 'Sponge' )
___ test_rock_crushes_scissors_snake_human_wolf_and_sponge(player
    ... get_winner('Rock', player) __ 'Rock'


___ test_rock_blocks_growth_of_tree
    ... get_winner('Rock', 'Tree') __ 'Rock'


___ test_fire_melts_scissors
    ... get_winner('Fire', 'Scissors') __ 'Fire'


?p__.m__.p.("player",  'Paper', 'Snake', 'Human',
                                    'Tree', 'Wolf', 'Sponge' )
___ test_fire_burns_paper_snake_human_tree_wolf_and_sponge(player
    ... get_winner('Fire', player) __ 'Fire'


___ test_scissors_swish_through_air
    ... get_winner('Scissors', 'Air') __ 'Scissors'


___ test_scissors_carve_tree
    ... get_winner('Scissors', 'Tree') __ 'Scissors'


?p__.m__.p.("player",  'Paper', 'Snake', 'Human',
                                    'Wolf', 'Sponge' )
___ test_scissors_cut_paper_snake_human_wolf_and_spnge(player
    ... get_winner('Scissors', player) __ 'Scissors'


?p__.m__.p.("player",  'Human', 'Wolf' )
___ test_snake_bites_human_and_wolf(player
    ... get_winner('Snake', player) __ 'Snake'


___ test_snake_swallows_sponge
    ... get_winner('Snake', 'Sponge') __ 'Snake'


?p__.m__.p.("player",  'Tree', 'Paper' )
___ test_snake_nests_in_tree_and_paper(player
    ... get_winner('Snake', player) __ 'Snake'


___ test_snake_breathes_air
    ... get_winner('Snake', 'Air') __ 'Snake'


___ test_snake_drinks_water
    ... get_winner('Snake', 'Water') __ 'Snake'


___ test_human_plants_tree
    ... get_winner('Human', 'Tree') __ 'Human'


___ test_human_tames_wolf
    ... get_winner('Human', 'Wolf') __ 'Human'


___ test_human_cleans_with_sponge
    ... get_winner('Human', 'Sponge') __ 'Human'


___ test_human_writes_paper
    ... get_winner('Human', 'Paper') __ 'Human'


___ test_human_breathes_air
    ... get_winner('Human', 'Air') __ 'Human'


___ test_human_drinks_water
    ... get_winner('Human', 'Water') __ 'Human'


___ test_human_slays_dragon
    ... get_winner('Human', 'Dragon') __ 'Human'


?p__.m__.p.("player",  'Wolf', 'Dragon' )
___ test_tree_shelters_wolf_and_dragon(player
    ... get_winner('Tree', player) __ 'Tree'


___ test_tree_outlives_sponge
    ... get_winner('Tree', 'Sponge') __ 'Tree'


___ test_tree_becomes_paper
    ... get_winner('Tree', 'Paper') __ 'Tree'


___ test_tree_produces_air
    ... get_winner('Tree', 'Air') __ 'Tree'


___ test_tree_drinks_water
    ... get_winner('Tree', 'Water') __ 'Tree'


___ test_tree_imprisons_devil
    ... get_winner('Tree', 'Devil') __ 'Tree'


?p__.m__.p.("player",  'Sponge', 'Paper' )
___ test_wolf_chews_up_sponge_and_paper(player
    ... get_winner('Wolf', player) __ 'Wolf'


___ test_wolf_breathes_air
    ... get_winner('Wolf', 'Air') __ 'Wolf'


___ test_wolf_drinks_water
    ... get_winner('Wolf', 'Water') __ 'Wolf'


?p__.m__.p.("player",  'Dragon', 'Lightning' )
___ test_wolf_outruns_dragon_and_lightning(player
    ... get_winner('Wolf', player) __ 'Wolf'


___ test_wolf_bites_devils_heiny
    ... get_winner('Wolf', 'Devil') __ 'Wolf'


___ test_sponge_soaks_paper
    ... get_winner('Sponge', 'Paper') __ 'Sponge'


___ test_sponge_uses_air_pockets
    ... get_winner('Sponge', 'Air') __ 'Sponge'


___ test_sponge_absorbs_water
    ... get_winner('Sponge', 'Water') __ 'Sponge'


?p__.m__.p.("player",  'Devil', 'Dragon' )
___ test_sponge_cleanses_devil_and_dragon(player
    ... get_winner('Sponge', player) __ 'Sponge'


___ test_sponge_cleans_guns
    ... get_winner('Sponge', 'Gun') __ 'Sponge'


___ test_sponge_conducts_lightning
    ... get_winner('Sponge', 'Lightning') __ 'Sponge'


___ test_paper_fans_air
    ... get_winner('Paper', 'Air') __ 'Paper'


___ test_paper_covers_rock
    ... get_winner('Paper', 'Rock') __ 'Paper'


___ test_paper_floats_on_water
    ... get_winner('Paper', 'Water') __ 'Paper'


?p__.m__.p.("player",  'Devil', 'Dragon' )
___ test_paper_rebukes_devil(player
    ... get_winner('Paper', player) __ 'Paper'


___ test_paper_outlaws_gun
    ... get_winner('Paper', 'Gun') __ 'Paper'


___ test_paper_defines_lightning
    ... get_winner('Paper', 'Lightning') __ 'Paper'


___ test_air_blows_out_fire
    ... get_winner('Air', 'Fire') __ 'Air'


___ test_air_erodes_rock
    ... get_winner('Air', 'Rock') __ 'Air'


___ test_air_evaporates_water
    ... get_winner('Air', 'Water') __ 'Air'


___ test_air_chokes_devil
    ... get_winner('Air', 'Devil') __ 'Air'


___ test_air_tarnishes_gun
    ... get_winner('Air', 'Gun') __ 'Air'


___ test_air_freezes_dragon
    ... get_winner('Air', 'Dragon') __ 'Air'


___ test_air_creates_lightningj
    ... get_winner('Air', 'Lightning') __ 'Air'


?p__.m__.p.("player",  'Devil', 'Dragon' )
___ test_water_drowns_devil_and_dragon(player
    ... get_winner('Water', player) __ 'Water'


___ test_water_erodes_rock
    ... get_winner('Water', 'Rock') __ 'Water'


___ test_water_puts_out_fire
    ... get_winner('Water', 'Fire') __ 'Water'


?p__.m__.p.("player",  'Scissors', 'Gun' )
___ test_water_rusts_scissors_and_gun(player
    ... get_winner('Water', player) __ 'Water'


___ test_water_conducts_lightning
    ... get_winner('Water', 'Lightning') __ 'Water'


___ test_dragon_commands_devil
    ... get_winner('Dragon', 'Devil') __ 'Dragon'


?p__.m__.p.("player",  'Lightning', 'Fire' )
___ test_dragon_breathes_lightning_and_fire(player
    ... get_winner('Dragon', player) __ 'Dragon'


___ test_dragon_rests_on_rock
    ... get_winner('Dragon', 'Rock') __ 'Dragon'


?p__.m__.p.("player",  'Scissors', 'Gun' )
___ test_dragon_is_immune_to_scissors_and_gun(player
    ... get_winner('Dragon', player) __ 'Dragon'


___ test_dragon_spawns_snake
    ... get_winner('Dragon', 'Snake') __ 'Dragon'


___ test_devil_hurls_rocks
    ... get_winner('Devil', 'Rock') __ 'Devil'


___ test_devil_breaths_fire
    ... get_winner('Devil', 'Fire') __ 'Devil'


?p__.m__.p.("player",  'Scissors', 'Gun' )
___ test_devil_is_immune_to_scissors_and_gun(player
    ... get_winner('Devil', player) __ 'Devil'


___ test_devil_casts_lightning
    ... get_winner('Devil', 'Lightning') __ 'Devil'


___ test_devil_eats_snake
    ... get_winner('Devil', 'Snake') __ 'Devil'


___ test_devil_possesses_human
    ... get_winner('Devil', 'Human') __ 'Devil'


?p__.m__.p.("player",  'Gun', 'Scissors' )
___ test_lightning_melts_gun_and_scissors(player
    ... get_winner('Lightning', player) __ 'Lightning'


?p__.m__.p.("player",  'Rock', 'Tree' )
___ test_lightning_splits_rocks_and_trees(player
    ... get_winner('Lightning', player) __ 'Lightning'


___ test_lightning_starts_fire
    ... get_winner('Lightning', 'Fire') __ 'Lightning'


?p__.m__.p.("player",  'Snake', 'Human' )
___ test_lightning_strikes_snake_and_human(player
    ... get_winner('Lightning', player) __ 'Lightning'


?p__.m__.p.("player",  'Rock', 'Tree', 'Fire' )
___ test_gun_targets_rock_tree_and_fire(player
    ... get_winner('Gun', player) __ 'Gun'


___ test_gun_outclasses_scissors
    ... get_winner('Gun', 'Scissors') __ 'Gun'


?p__.m__.p.("player",  'Snake', 'Human', 'Wolf' )
___ test_gun_shoots_snake_human_and_wolf(player
    ... get_winner('Gun', player) __ 'Gun'