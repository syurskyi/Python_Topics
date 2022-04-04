_______ __
____ dataclasses _______ dataclass, field
____ p.. _______ P..
____ t___ _______ L..
____ u__.r.. _______ u..

____ bs4 _______ BeautifulSoup __ Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = P..(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


@dataclass
c_ Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    id_name: s..
    name: s..
    max_level: i..
    description: s..
    items: L..[s..] = field(default_factory=l..)

    ___ __post_init__
        name = name.r..('_', ' ')

    ___  -r
        r.. f'{name} ({max_level}): {description}'


@dataclass()
c_ Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    name: s..
    enchantments: L..[s..] = field(default_factory=l..)

    # def __post_init__(self):
    #     self.name = self.name.replace('_',' ').title()

    ___  -r
        en = _*   [{chant.max_level}] {chant.id_name}'
              ___ chant __ s..(enchantments, key=l.... x : x.id_name)]
        r.. f'{name.r..("_"," ").t..}: \n' + '\n'.j..(en)


# Lookup values of the first five roman numerals
LEVEL_TRANSLATE = {'I': 1,
                   'II': 2,
                   'III': 3,
                   'IV': 4,
                   'V': 5}


___ generate_enchantments(soup
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    res = d..()
    ___ row __ soup.select('table#minecraft_items > tr'
        data_items = row.find_all('td')
        __ data_items __ N.. o. l..(data_items) __ 0:
            _____
        enchant, maxlevel, descr, id, item, version = data_items
        id_name = enchant.em.text
        name = enchant.a.text
        max_level = LEVEL_TRANSLATE[maxlevel.text.s..]
        description = descr.text
        item_url = item.img.attrs.g.. 'data-src')
        items = __.sub(r'.*/(?:enchanted_)?(?:iron_)?([^/]+?)(?:_sm)?\.png', r'\1', item_url)
        items = items.r..('fishing_rod', 'FISHING=ROD')
        items = l.. m..(l.... s: s.r..('FISHING=ROD', 'fishing_rod'), items.s..('_')))

        res[id_name] = Enchantment(id_name,
                                   name,
                                   max_level,
                                   description,
                                   items
                                   )

    r.. res


___ generate_items(data
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    res = d..()
    ___ enchantment __ data.v..
        ___ i __ enchantment.items:
            __ i __ res.k..:
                res[i].enchantments.a..(enchantment)
            ____
                res[i] = Item(i, [enchantment])
    r.. d..(s..(res.i.., key=l.... t: t[0]


___ get_soup(file=HTML_FILE
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    __ isi..(file, P..
        __ n.. HTML_FILE.is_file
            u..(URL, HTML_FILE)

        w__ file.o.. ) __ html_source:
            soup = Soup(html_source, "html.parser")
    ____
        soup = Soup(file, "html.parser")

    r.. soup


___ main
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    ___ item __ minecraft_items:
        print(minecraft_items[item], "\n")


__ _______ __ _______
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
