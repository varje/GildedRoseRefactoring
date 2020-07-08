# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # better function name would be daily_update
    def update_quality(self):
        # define variables instead of direct text
        brie = "Aged Brie"
        backstage_passes = "Backstage passes to a TAFKAL80ETC concert"
        sulfuras = "Sulfuras, Hand of Ragnaros"
        # will just use direct strings; in real project would use extra property "Conjured"/"Backstage passes" 
        # as by task description can understand that might be eg. "Conjured Aged Brie"
        conjured = "Conjured"

        def decrease_quality(item, points):
            item.quality -= points

        def increase_quality(item, points):
            item.quality -= points

        def decrease_sellin_days(item, days):
            item.sell_in -= days

        def backstage_passes_update(item):
            # "Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches;
            # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less 
            # but Quality drops to 0 after the concert
            if item.sell_in <= 0:
                item.quality = 0
            elif item.sell_in <= 5:
                increase_quality *= 3
            elif item.sell_in <= 10:
                increase_quality *= 2


        for item in self.items:
            # check exceptions
            if item == sulfuras:
                # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
                pass
            if item == brie:
                # "Aged Brie" actually increases in Quality the older it gets
                increase_quality(item, 1)
            if item == backstage_passes:
                backstage_passes_update(item)
            if item == conjured:
                # "Conjured" items degrade in Quality twice as fast as normal items
                decrease_quality(item, 2)
            if item.quality == 0 or item.quality >= 50:
                # The Quality of an item is never negative; The Quality of an item is never more than 50
                decrease_sellin_days(item, 1)
            if item.sell_in < 0:
                # Once the sell by date has passed, Quality degrades twice as fast
                decrease_quality(item, 2)

            # seperate quality and sellin changes, add extra parameter for exceptions
            decrease_quality(item, points)
            decrease_sellin_days(item, days)






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
