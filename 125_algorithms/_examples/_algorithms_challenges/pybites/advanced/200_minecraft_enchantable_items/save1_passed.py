from collections import defaultdict
from dataclasses import dataclass, field
from functools import total_ordering
from pathlib import Path
from re import compile, search
from typing import Any, DefaultDict, List
from u__.r.. import u..

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}


@dataclass
@total_ordering
class Enchantment:
    """Minecraft enchantment"""

    id_name: str
    name: str
    max_level: int
    description: str
    items: List[str] = field(default_factory=list)

    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"

    def __lt__(self, other):
        return self.id_name < other.id_name


@dataclass
class Item:
    """Minecraft enchantable item"""

    name: str
    enchantments: List[Enchantment] = field(default_factory=list)

    def __str__(self):
        enchants = sorted(self.enchantments)
        enc_list = [f"\n  [{enc.max_level}] {enc.id_name}" for enc in enchants]
        return f"{self.name.title()}: {''.join(enc_list)}"


def clean_up_names(item_names):
    """Cleans up item names

    :param item_names: String of item names
    :return: String of cleaned up item names
    """
    unwanted = (".png", "_sm", "iron_", "enchanted_")

    if "fishing_rod" in item_names:
        item_names = item_names.replace("fishing_rod", "fishingrod")

    for chars in unwanted:
        if chars in item_names:
            item_names = item_names.replace(chars, "")

    item_names = item_names.split("_")
    item_names = [
        "fishing_rod" if item == "fishingrod" else item for item in item_names
    ]

    return " ".join(item_names)


def enchantable_items(soup):
    """Scrapes BeautifulSoup object for items

    :param soup: BeautifulSoup object
    :return: List of enchantable items lists
    """
    table = soup.find("table", {"id": "minecraft_items"})
    items = [
        clean_up_names(img["data-src"].split("/")[-1]).split()
        for img in table.find_all("img")
    ]

    return items


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects

    :param soup: BeautifulSoup object
    :return: DefaultDict of Enchantment objects
    """
    item_list = enchantable_items(soup)
    data = parse_html(soup)
    enchant_data: DefaultDict[Any, Enchantment] = defaultdict(Enchantment)

    for i, row in enumerate(data):
        id_name, name = split_title(row[0])
        max_level = ROMAN[row[1]]
        description = row[2]
        items = item_list[i]
        enchant = Enchantment(id_name, name, max_level, description, items)
        enchant_data[id_name] = enchant

    return enchant_data


def generate_items(data):
    """Generates a dictionary of Item objects

    :param data: DefaultDict of Enchantment objects
    :return: DefaultDict of Item objects
    """
    mc_items: DefaultDict[Any, Item] = defaultdict(Item)
    unique_items = gen_item_set(data)

    for item in unique_items:
        mc_items[item] = Item(item.replace("_", " "))

    for enchant in data:
        for item in data[enchant].items:
            mc_items[item].enchantments.append(data[enchant])

    return mc_items


def gen_item_set(data):
    """Returns a set of item names

    :param data: Dictionary of Enchantment objects
    :return: Set of sorted item object name strings
    """
    mc_items = set()
    for enchantment in data.keys():
        for item in data[enchantment].items:
            mc_items.add(item)

    return sorted(mc_items)


def get_soup(file=HTML_FILE):
    """Retrieves source HTML and returns a BeautifulSoup object

    :param file: Path file object
    :return: BeautifulSoup object
    """
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            u..(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


def parse_html(soup):
    """Parses BeautifulSoup object and returns the table

    :param soup: BeautifulSoup object
    :return: List of the rows that make up the table
    """
    table = soup.find("table", {"id": "minecraft_items"})
    data = [
        [td.get_text() for td in row.find_all("td")] for row in table.find_all("tr")
    ]

    return data[1:]


def split_title(title):
    """
    Splits the title string

    :param title: String of the enchantment title
    :return: Tuple(id_names, names)
    """
    pattern = compile(r"(.*)\((.*)\)")
    names, id_names = search(pattern, title).groups()
    return id_names, names


if __name__ == "__main__":
    main()