_______ __
____ p.. _______ P..
_______ b__
_______ __
____ u__.r.. _______ u..
____ ___ _______ B.. __ S..

TMP P.. __.g.. "TMP", "/tmp"
HTML_FILE ? / "enchantment_list_pc.html"

# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")


c_ Enchantment
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """

    ___ - id_name name max_level description
        ? ?
        ? ?
        ? ?
        ? ?
        items    # list

    ___ -s
        r.. _* n.. ( m.. : d..
    
c_ Item
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    ___ - name
        ? ?
        enchantments    # list

    ___ add_enchantment enchantment
        ?.a.. ?
    

    ___ -s
        s__ name.r..('_',' ').t.. + ': '
        sorted_enchantments s.. e.. k.._l.... x ?.i..
        ___ enchantment __ ?
            s__ += _* \n  ?.m.. ?.i..
        r.. s__

___ generate_enchantments soup
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """

    enchantment_dict    # dict
    mapping {'I': 1,'II': 2,'III': 3,'IV': 4,'V': 5}
    table ?.f.. 'table',id="minecraft_items")
    all_values    # list
    ___ table_row __ ? f.. 'tr' 1|
        data ?.f.. 'td'
        values    # list
        ___ i,d __ e.. d..
            value ?.g..
            v__.a.. ?
        
        image_source t__.f.. img data-src
        last_part ?.s.. '/' -1
        last_part __.s.. _ \.|png|sm|enchanted|iron ,'' ?
        
        items last_part.s...s.. '_'
        valid_items    # list
        ___ item __ ?
            __ ?
                __ ? __ fishing
                    valid_items.a..('fishing_rod')
                ____ item __ 'rod':
                    _____
                ____
                    valid_items.a..(item)
                                               
        id_name __.s.. _ \((.+)\)',values 0.group(1)
        name= __.s.. _ \(.+\)','',values[0])
        level i..(mapping[values[1]])
        description values[2]

        enchantment Enchantment(id_name,name,level,description)
        enchantment.items valid_items
        enchantment_dict[id_name] enchantment
    
    print(enchantment_dict)
    r.. enchantment_dict


        
        
        


___ generate_items(data
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    

    item_mapping    # dict
    

    ___ enchantment_id,enchantment __ data.i..

        ___ item __ enchantment.items:
            __ item n.. __ item_mapping:
                item_mapping[item] Item(item)


            item_mapping[item].add_enchantment(enchantment)
    
    
    item_mapping d..(s..(item_mapping.i..,k.._l.... x:x[0]

    r.. item_mapping




___ get_soup(file=HTML_FILE
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    __ isi..(file, P..
        __ n.. file.is_file
            u..(URL, file)

        w__ file.o.. ) __ html_source:
            soup S..(html_source, "html.parser")
    ____
        soup S..(file, "html.parser")

    r.. soup


___ main
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup get_soup()
    enchantment_data generate_enchantments(soup)
    minecraft_items generate_items(enchantment_data)
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
