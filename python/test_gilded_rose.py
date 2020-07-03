# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.mock_items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_mock_items_array_length(self):
        items = self.mock_items
        self.assertEqual(len(items), 9)

    def test_each_day_denoting_Sellin_value(self):
        pass

    def test_each_day_denoting_Quality_value(self):
        pass


    def test_quality_degrades_twice_as_fast_after_sell_date_passed(self):
        pass

    def test_quality_is_never_negative(self):
        pass

    def test_Aged_Brie_quality_increase_each_day(self):
        pass

    def test_quality_is_never_over_50(self):
        pass

    def test_Sulfuras_does_not_degrade_in_quality_nor_selling_time(self):
        pass

    def test_Backstage_passes_quality_increases_in_time(self):
        pass

    def test_Backstage_passes_quality_increases_by_2_when_time_is_equal_or_smaller_than_10_days(self):
        pass

    def test_Backstage_passes_quality_increases_by_3_when_time_is_equal_or_smaller_than_5_days(self):
        pass

    def test_Backstage_passes_quality_drops_to_0_after_the_concert(self):
        pass

    def test_Conjured_items_degrade_Quality_twice_as_fast(self):
        pass

    def test_items_except_Sulfuras_can_not_have_quality_above_50(self):
        pass

if __name__ == '__main__':
    unittest.main()
