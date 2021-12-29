import os
from pathlib import Path
import bisect
import re
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
HTML_FILE = TMP / "enchantment_list_pc.html"

# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """

    def __init__(self,id_name,name,max_level,description):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"
    
class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    def __init__(self,name):
        self.name = name
        self.enchantments = []

    def add_enchantment(self,enchantment):
        self.enchantments.append(enchantment)
    

    def __str__(self):
        string = self.name.replace('_',' ').title() + ': '
        sorted_enchantments = sorted(self.enchantments,key=lambda x: x.id_name)
        for enchantment in sorted_enchantments:
            string += f'\n  [{enchantment.max_level}] {enchantment.id_name}'
        return string

def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """

    enchantment_dict = {}
    mapping = {'I': 1,'II': 2,'III': 3,'IV': 4,'V': 5}
    table = soup.find('table',id="minecraft_items")
    all_values = []
    for table_row in table.find_all('tr')[1:]:
        data = table_row.find_all('td')
        values = []
        for i,d in enumerate(data):
            value = d.getText()
            values.append(value)
        
        image_source = table_row.find('img')['data-src']
        last_part = image_source.split('/')[-1]
        last_part = re.sub(r'\.|png|sm|enchanted|iron','',last_part)
        
        items = last_part.strip().split('_')
        valid_items = []
        for item in items:
            if item:
                if item == 'fishing':
                    valid_items.append('fishing_rod')
                elif item == 'rod':
                    continue
                else:
                    valid_items.append(item)
                                               
        id_name = re.search(r'\((.+)\)',values[0]).group(1)
        name= re.sub(r'\(.+\)','',values[0])
        level = int(mapping[values[1]])
        description = values[2]

        enchantment = Enchantment(id_name,name,level,description)
        enchantment.items = valid_items
        enchantment_dict[id_name] = enchantment
    
    print(enchantment_dict)
    return enchantment_dict


        
        
        


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    

    item_mapping = {}
    

    for enchantment_id,enchantment in data.items():

        for item in enchantment.items:
            if item not in item_mapping:
                item_mapping[item] = Item(item)


            item_mapping[item].add_enchantment(enchantment)
    
    
    item_mapping = dict(sorted(item_mapping.items(),key=lambda x:x[0]))

    return item_mapping




def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not file.is_file():
            urlretrieve(URL, file)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
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
