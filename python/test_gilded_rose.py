# -*- coding: utf-8 -*-
import unittest
import copy

from gilded_rose import Item, GildedRose
# from test_items import mock_items

# help function for data creation
def help_for_creating_data(test_items):
    updated_items = copy.deepcopy(test_items)
    original_obj = GildedRose(test_items)
    updated_obj = GildedRose(updated_items)
    updated_obj.update_quality()
    return updated_items

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        vest = "+5 Dexterity Vest"
        elixir = "Elixir of the Mongoose"
        mock_normal_items = [
            Item(name=vest, sell_in=10, quality=20),
            Item(name=elixir, sell_in=5, quality=7)
        ]

        mock_sellin_passed_items = [
            Item(name=vest, sell_in=0, quality=20),
            Item(name=elixir, sell_in=-2, quality=2)
        ]

        mock_sellin_passed_items = [
            Item(name=vest, sell_in=0, quality=20),
            Item(name=elixir, sell_in=-2, quality=2)
        ]

        mock_quality_negative_or_0 = [
            Item(name=vest, sell_in=0, quality=0),
            Item(name=elixir, sell_in=-2, quality=-10)
        ]





        #   Item(name="Superbad noodle sword", sell_in=0, quality= -20) 
        #     Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        #     Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        # Item(name="Aged Brie", sell_in=2, quality=0),
        # Item(name="Conjured Mana Cake", sell_in=3, quality=6)
            
        #     Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        #     Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        #     Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        self.mock_normal_items = mock_normal_items
        self.mock_sellin_passed_items = mock_sellin_passed_items
        self.mock_quality_negative_or_0 = mock_quality_negative_or_0

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        self.assertEqual("foo", items[0].name)

    def test_mock_items_array_length(self):
        items = self.mock_normal_items
        self.assertEqual(len(items), 2)

    def test_each_day_denoting_Sellin_value(self):
        original_items = self.mock_normal_items
        updated_items = help_for_creating_data(original_items)
        self.assertEqual(([item.sell_in-1 for item in original_items]), ([item.sell_in for item in updated_items]))

    def test_each_day_denoting_Quality_value(self):
        original_items = self.mock_normal_items
        updated_items = help_for_creating_data(original_items)
        self.assertEqual(([item.quality-1 for item in original_items]), ([item.quality for item in updated_items]))


    def test_quality_degrades_twice_as_fast_after_sell_date_passed(self):
        original_items = self.mock_sellin_passed_items
        updated_items = help_for_creating_data(original_items)
        self.assertEqual(([item.quality-2 for item in original_items]), ([item.quality for item in updated_items]))


    def test_quality_is_never_negative(self):
        original_items = self.mock_quality_negative_or_0
        updated_items = help_for_creating_data(original_items)
        self.assertEqual([0, 0], ([item.quality for item in updated_items]))

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
