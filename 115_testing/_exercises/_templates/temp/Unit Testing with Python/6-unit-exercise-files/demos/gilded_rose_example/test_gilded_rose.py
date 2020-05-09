# -*- coding: utf-8 -*-
______ pytest

____ gilded_rose ______ Item, GildedRose

examples _ (("item_name", "initial_quality", "initial_sellin", "updated_quality", "updated_sellin", "comment"),
             (("foo", 0, 0, 0, -1, "typical item"),
             ("foo", 10, 0, 8, -1, "typical item"),
             ("Sulfuras, Hand of Ragnaros", 0, 0, 0, 0, "exceptional item"),
             ("Sulfuras, Hand of Ragnaros", 10, 0, 10, 0, "exceptional item"),
             ("Sulfuras, Hand of Ragnaros", 10, -1, 10, -1, "exceptional item"),
             ("Aged Brie", 0, 0, 2, -1, "brie item"),
             ("Backstage passes to a TAFKAL80ETC concert", 0, 0, 0, -1, "backstage pass item")
           ))
@pytest.mark.parametrize(*examples)
___ test_update_quality(item_name, initial_quality, initial_sellin, updated_quality, updated_sellin, comment
    item _ Item(item_name, initial_sellin, initial_quality)
    gilded_rose _ GildedRose([item])
    gilded_rose.update_quality()
    a.. item.quality __ updated_quality
    a.. item.sell_in __ updated_sellin
