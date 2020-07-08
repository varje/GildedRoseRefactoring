# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # better function name would be daily_update
    def update_quality(self):
        # define variables instead of direct text
        # simplification: using direct strings; in real project would take in account spaces, tabs, capital letters etc
        brie = "Aged Brie"
        sulfuras = "Sulfuras, Hand of Ragnaros"

        # help functions
        def decrease_sellin_days(item):
            item.sell_in -= 1

        def decrease_quality(item, points):
            item.quality -= points

        def increase_quality(item, points):
            item.quality += points

        def backstage_passes_update(item):
            # "Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches;
            # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less 
            # but Quality drops to 0 after the concert
            if item.sell_in < 0:
                item.quality = 0
            elif item.sell_in <= 5:
                increase_quality(item, 3)
            elif item.sell_in <= 10:
                increase_quality(item, 2)
            else:
                increase_quality(item, 1)
        
        def change_quality(item):
            if item.quality <= 0:
                # The Quality of an item is never negative
                # although item quality can not go below 0, this is to catch items which start with below 0 quality
                item.quality = 0
            elif item.quality >= 50:
                # The Quality of an item is never more than 50
                # although item quality can not go above 50, this is to catch items which start with above 50 quality
                item.quality = 50
            elif item == sulfuras:
                # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
                pass
            elif item.name == brie:
                # "Aged Brie" actually increases in Quality the older it gets
                increase_quality(item, 1)
            elif item.name.startswith("Backstage passes"):
                # simplification: using startswith with exact string; real project would handle spaces-tabs, capital letters etc.
                # as backstage_passes have quite complicated rules, will make subfunction
                backstage_passes_update(item)
            elif item.name.startswith("Conjured"):
                # simplification: using startswith with exact string; real project would handle spaces-tabs, capital letters etc.
                # "Conjured" items degrade in Quality twice as fast as normal items
                decrease_quality(item, 2)
            elif item.sell_in < 0:
                # Once the sell by date has passed, Quality degrades twice as fast
                # will assume that this goes only for normal items, not conjured
                decrease_quality(item, 2)
            else:
                # normal case
                decrease_quality(item, 1)

        for item in self.items:
            # check exceptions
            # as exceptions go only for quality, will call out two subfunctions seperately
            decrease_sellin_days(item)
            change_quality(item)






            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
