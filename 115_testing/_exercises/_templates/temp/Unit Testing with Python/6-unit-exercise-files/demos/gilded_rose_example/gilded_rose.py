# -*- coding: utf-8 -*-

c_ GildedRose o..

    ___  -   items
        items _ items

    ___ update_quality
        ___ item __ items:
            __ item.name !_ "Aged Brie" an. item.name !_ "Backstage passes to a TAFKAL80ETC concert":
                __ item.quality > 0:
                    __ item.name !_ "Sulfuras, Hand of Ragnaros":
                        item.quality _ item.quality - 1
            ____:
                __ item.quality < 50:
                    item.quality _ item.quality + 1
                    __ item.name __ "Backstage passes to a TAFKAL80ETC concert":
                        __ item.sell_in < 11:
                            __ item.quality < 50:
                                item.quality _ item.quality + 1
                        __ item.sell_in < 6:
                            __ item.quality < 50:
                                item.quality _ item.quality + 1
            __ item.name !_ "Sulfuras, Hand of Ragnaros":
                item.sell_in _ item.sell_in - 1
            __ item.sell_in < 0:
                __ item.name !_ "Aged Brie":
                    __ item.name !_ "Backstage passes to a TAFKAL80ETC concert":
                        __ item.quality > 0:
                            __ item.name !_ "Sulfuras, Hand of Ragnaros":
                                item.quality _ item.quality - 1
                    ____:
                        item.quality _ item.quality - item.quality
                ____:
                    __ item.quality < 50:
                        item.quality _ item.quality + 1

    
c_ Item:
    ___  -   name, sell_in, quality
        name _ name
        sell_in _ sell_in
        quality _ quality

    ___ __repr__
        r_ "%s, %s, %s" % (name, sell_in, quality)
