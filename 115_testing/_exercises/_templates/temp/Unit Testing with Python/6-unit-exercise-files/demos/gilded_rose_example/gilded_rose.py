# -*- coding: utf-8 -*-

c_ GildedRose(object):

    ___  -   items):
        items _ items

    ___ update_quality
        for item in items:
            if item.name !_ "Aged Brie" and item.name !_ "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name !_ "Sulfuras, Hand of Ragnaros":
                        item.quality _ item.quality - 1
            else:
                if item.quality < 50:
                    item.quality _ item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality _ item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality _ item.quality + 1
            if item.name !_ "Sulfuras, Hand of Ragnaros":
                item.sell_in _ item.sell_in - 1
            if item.sell_in < 0:
                if item.name !_ "Aged Brie":
                    if item.name !_ "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name !_ "Sulfuras, Hand of Ragnaros":
                                item.quality _ item.quality - 1
                    else:
                        item.quality _ item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality _ item.quality + 1

    
c_ Item:
    ___  -   name, sell_in, quality):
        name _ name
        sell_in _ sell_in
        quality _ quality

    ___ __repr__
        r_ "%s, %s, %s" % (name, sell_in, quality)
