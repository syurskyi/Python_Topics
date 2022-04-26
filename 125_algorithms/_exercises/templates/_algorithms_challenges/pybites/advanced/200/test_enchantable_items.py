_______ p__

____ enchantable_items _______ (
    Enchantment,
    Item,
    generate_items,
    get_soup,
    generate_enchantments,
)

mock_html """
<table id="minecraft_items" class="std_table">
<tr>
<th data-search="1" width="175">Enchantment<br>(<em>Minecraft ID Name</em>)</th>
<th data-search="1">Max Level</th>
<th class="hidden-xs">Description</th>
<th data-search="1"><span class="hidden-xs">Minecraft </span>ID</th>
<th class="hidden-xs">Items</th>
<th>Version</th>
</tr>
<tr>
<td><a href="/enchantments/aqua_affinity.php">Aqua Affinity</a><br>(<em>aqua_<wbr>affinity</em>)</td>
<td>I</td>
<td class="hidden-xs">Speeds up how fast you can mine blocks underwater</td>
<td>6</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/armor_recipes/images/enchanted_iron_helmet.png" alt="aqua affinity" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/bane_of_arthropods.php">Bane of Arthropods</a><br>(<em>bane_<wbr>of_<wbr>arthropods</em>)</td>
<td>V</td>
<td class="hidden-xs">Increases attack damage against arthropods</td>
<td>18</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/enchantments/images/sword_axe_sm.png" alt="bane of arthropods" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/blast_protection.php">Blast Protection</a><br>(<em>blast_<wbr>protection</em>)</td>
<td>IV</td>
<td class="hidden-xs">Reduces blast and explosion damage</td>
<td>3</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/enchantments/images/armor_sm.png" alt="blast protection" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/channeling.php">Channeling</a><br>(<em>channeling</em>)</td>
<td>I</td>
<td class="hidden-xs">Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)</td>
<td>68</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/weapon_recipes/images/enchanted_trident.png" alt="channeling" width="40" height="40"></td>
<td>1.13</td>
</tr>
</table>
"""


?p__.f.. s.._"module"
___ enchantment_mock
    enchant Enchantment(
        "python_developer",
        "Python Developer",
        10,
        "Ability automate really boring and repetitive tasks at work",
    )
    r.. enchant


?p__.f.. s.._"module"
___ item_mock(enchantment_mock
    item Item("clamytoe")
    r.. item


?p__.f.. s.._"module"
___ mock_soup
    r.. get_soup(mock_html)


?p__.f.. s.._"module"
___ mock_data(mock_soup
    r.. generate_enchantments(mock_soup)


?p__.f.. s.._"module"
___ mocked_generate_items(mock_data
    r.. generate_items(mock_data)


?p__.f.. s.._"module"
___ coders_dataset
    soup get_soup()
    mc_data generate_enchantments(soup)
    items generate_items(mc_data)
    r.. items


___ test_enchantment_class(enchantment_mock
    ... enchantment_mock.n.. __ "Python Developer"
    ... enchantment_mock.items __ []


___ test_enchantment_class_add_items(enchantment_mock, item_mock
    enchantment_mock.items.a..(item_mock.name)
    ... l..(enchantment_mock.items) __ 1
    bob Item("bob")
    enchantment_mock.items.a..(bob.name)
    ... l..(enchantment_mock.items) __ 2
    ... enchantment_mock.items __ ["clamytoe", "bob"]
    ... enchantment_mock.max_level __ 10


___ test_enchantment_class_print(enchantment_mock, capfd
    print(enchantment_mock)
    output ?.r .. 0 .s..("\n" 0
    ... (
        output
        __ "Python Developer (10): Ability automate really boring and repetitive tasks at work"
    )


___ test_item_class(item_mock, enchantment_mock
    item_mock.enchantments.a..(enchantment_mock)
    ... item_mock.enchantments[0].n.. __ "Python Developer"


___ test_item_class_print(item_mock, capfd
    print(item_mock)
    output ?.r .. 0 .s..
    ... ? __ "Clamytoe: \n  [10] python_developer"


___ test_enchantment_print(mock_data, capfd
    print(mock_data["channeling"])
    output ?.r .. 0 .s..("\n" 0
    ... (
        output
        __ "Channeling (1): Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)"
    )


?p__.m__.p.(
    "enchant, expected",
    [
        ("aqua_affinity", 1),
        ("bane_of_arthropods", 5),
        ("blast_protection", 4),
        ("channeling", 1),
    ],
)
___ test_roman_numeral_conversion(mock_data, enchant, e..
    ... mock_data[enchant].max_level __ e..


___ test_generate_enchantments_with_mock(mock_data
    ... isi..(mock_data, d..)
    ... l..(mock_data.keys __ 4
    ... (
        mock_data["channeling"].d..
        __ "Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)"
    )


___ test_generate_enchantments_from_source
    soup get_soup()
    data generate_enchantments(soup)
    ... l..(data.keys __ 38
    ... data["efficiency"].max_level __ 5


?p__.m__.p.(
    "item, expected",
    [
        ("armor", "Blast Protection"),
        ("axe", "Bane of Arthropods"),
        ("helmet", "Aqua Affinity"),
        ("sword", "Bane of Arthropods"),
        ("trident", "Channeling"),
    ],
)
___ test_gen_items_mocked(mocked_generate_items, item, e..
    ... mocked_generate_items[item].enchantments[0].n.. __ e..


?p__.m__.p.(
    "item, expected",
    [
        (
            "armor",
            [
                "blast_protection",
                "binding_curse",
                "fire_protection",
                "projectile_protection",
                "protection",
                "thorns",
            ],
        ),
        (
            "axe",
            [
                "bane_of_arthropods",
                "efficiency",
                "fortune",
                "sharpness",
                "silk_touch",
                "smite",
            ],
        ),
        ("boots", ["depth_strider", "feather_falling", "frost_walker", "soul_speed"]),
        ("bow", ["flame", "infinity", "power", "punch"]),
        ("chestplate", ["vanishing_curse", "mending", "unbreaking"]),
        ("crossbow", ["multishot", "piercing", "quick_charge"]),
        (
            "fishing_rod",
            ["vanishing_curse", "luck_of_the_sea", "lure", "mending", "unbreaking"],
        ),
        ("helmet", ["aqua_affinity", "respiration"]),
        (
            "pickaxe",
            [
                "vanishing_curse",
                "efficiency",
                "fortune",
                "mending",
                "silk_touch",
                "unbreaking",
            ],
        ),
        ("shovel", ["efficiency", "fortune", "silk_touch"]),
        (
            "sword",
            [
                "bane_of_arthropods",
                "vanishing_curse",
                "fire_aspect",
                "knockback",
                "looting",
                "mending",
                "sharpness",
                "smite",
                "sweeping",
                "unbreaking",
            ],
        ),
        ("trident", ["channeling", "impaling", "loyalty", "riptide"]),
    ],
)
___ test_gen_items(coders_dataset, item, e..
    ... [enc.id_name ___ enc __ coders_dataset[item].enchantments] __ e..


?p__.m__.p.(
    "item, expected",
    [
        (
            "armor",
            "Armor: \n  [1] binding_curse\n  [4] blast_protection\n  [4] fire_protection\n  [4] projectile_protection\n  [4] protection\n  [3] thorns",
        ),
        (
            "axe",
            "Axe: \n  [5] bane_of_arthropods\n  [5] efficiency\n  [3] fortune\n  [5] sharpness\n  [1] silk_touch\n  [5] smite",
        ),
        (
            "boots",
            "Boots: \n  [3] depth_strider\n  [4] feather_falling\n  [2] frost_walker\n  [3] soul_speed",
        ),
        ("bow", "Bow: \n  [1] flame\n  [1] infinity\n  [5] power\n  [2] punch"),
        (
            "chestplate",
            "Chestplate: \n  [1] mending\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        ("crossbow", "Crossbow: \n  [1] multishot\n  [4] piercing\n  [3] quick_charge"),
        (
            "fishing_rod",
            "Fishing Rod: \n  [3] luck_of_the_sea\n  [3] lure\n  [1] mending\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        ("helmet", "Helmet: \n  [1] aqua_affinity\n  [3] respiration"),
        (
            "pickaxe",
            "Pickaxe: \n  [5] efficiency\n  [3] fortune\n  [1] mending\n  [1] silk_touch\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        ("shovel", "Shovel: \n  [5] efficiency\n  [3] fortune\n  [1] silk_touch"),
        (
            "sword",
            "Sword: \n  [5] bane_of_arthropods\n  [2] fire_aspect\n  [2] knockback\n  [3] looting\n  [1] mending\n  [5] sharpness\n  [5] smite\n  [3] sweeping\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        (
            "trident",
            "Trident: \n  [1] channeling\n  [5] impaling\n  [3] loyalty\n  [3] riptide",
        ),
    ],
)
___ test_item_print(coders_dataset, item, e.., capfd
    print(coders_dataset[item])
    output ?.r .. 0 .s..
    ... ? __ e..
