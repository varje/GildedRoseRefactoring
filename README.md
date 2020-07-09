# Gilded Rose Refactoring Kata
### This repository is cloned from @emilybache GildedRose
### Only includes python code with refactoring and unittests

# Running tests:
cd python  
python -m unittest

# Requirements:

### Main requirements:
1. All items have a SellIn value which denotes the number of days we have to sell the item
1. All items have a Quality value which denotes how valuable the item is
1. At the end of each day system lowers both values for every item

#### Exceptions:

1. Once the sell by date has passed, Quality degrades twice as fast  
1. The Quality of an item is never negative  
1. "Aged Brie" actually increases in Quality the older it gets  
1. The Quality of an item is never more than 50
1. "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
1. "Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
1. "Conjured" items degrade in Quality twice as fast as normal items
1. Do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover for you).
1. An item can never have its Quality increase above 50, however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.


# ReadMe from @emilybache repository:
## Gilded Rose Refactoring Kata

This Kata was originally created by Terry Hughes (http://twitter.com/TerryHughes). It is already on GitHub [here](https://github.com/NotMyself/GildedRose). See also [Bobby Johnson's description of the kata](http://iamnotmyself.com/2011/02/13/refactor-this-the-gilded-rose-kata/).

I translated the original C# into a few other languages, (with a little help from my friends!), and slightly changed the starting position. This means I've actually done a small amount of refactoring already compared with the original form of the kata, and made it easier to get going with writing tests by giving you one failing unit test to start with. I also added test fixtures for Text-Based approval testing with TextTest (see [the TextTests](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/texttests))

As Bobby Johnson points out in his article ["Why Most Solutions to Gilded Rose Miss The Bigger Picture"](http://iamnotmyself.com/2012/12/07/why-most-solutions-to-gilded-rose-miss-the-bigger-picture), it'll actually give you
better practice at handling a legacy code situation if you do this Kata in the original C#. However, I think this kata
is also really useful for practicing writing good tests using different frameworks and approaches, and the small changes I've made help with that. I think it's also interesting to compare what the refactored code and tests look like in different programming languages.

I wrote this article ["Writing Good Tests for the Gilded Rose Kata"](http://coding-is-like-cooking.info/2013/03/writing-good-tests-for-the-gilded-rose-kata/) about how you could use this kata in a [coding dojo](https://leanpub.com/codingdojohandbook).

## How to use this Kata

The simplest way is to just clone the code and start hacking away improving the design. You'll want to look at the ["Gilded Rose Requirements"](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/GildedRoseRequirements.txt) which explains what the code is for. I strongly advise you that you'll also need some tests if you want to make sure you don't break the code while you refactor.

You could write some unit tests yourself, using the requirements to identify suitable test cases. I've provided a failing unit test in a popular test framework as a starting point for most languages.

Alternatively, use the "Text-Based" tests provided in this repository. (Read more about that in the next section)

Whichever testing approach you choose, the idea of the exercise is to do some deliberate practice, and improve your skills at designing test cases and refactoring. The idea is not to re-write the code from scratch, but rather to practice designing tests, taking small steps, running the tests often, and incrementally improving the design. 

## Text-Based Approval Testing

This code comes with comprehensive tests that use this approach. For information about how to run them, see the [texttests README](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/texttests)

## Get going quickly using Cyber-Dojo

I've also set this kata up on [cyber-dojo](https://cyber-dojo.org) for several languages, so you can get going really quickly:

To create an *individual* exercise:
- [C#, NUnit](https://cyber-dojo.org/forker/fork_individual/Fz4xFX?index=3)
- [C++ (g++), GoogleTest](https://cyber-dojo.org/forker/fork_individual/qPPrZy?index=7)
- [Java, Cucumber](https://cyber-dojo.org/forker/fork_individual/SvUf30?index=2) - for this one I've also written some step definitions for you
- [Java, JUnit](https://cyber-dojo.org/forker/fork_individual/aJJEN4?index=2)
- [Python, unittest](https://cyber-dojo.org/forker/fork_individual/NFgFys?index=2)
- [Ruby, RSpec](https://cyber-dojo.org/forker/fork_individual/D3xbUV?index=3)
- [Ruby, testunit](https://cyber-dojo.org/forker/fork_individual/zlElgj?index=9)

To create a *group* exercise:
- [C#, NUnit](https://cyber-dojo.org/forker/fork_group/Fz4xFX?index=3)
- [C++ (g++), GoogleTest](https://cyber-dojo.org/forker/fork_group/qPPrZy?index=7)
- [Java, Cucumber](https://cyber-dojo.org/forker/fork_group/SvUf30?index=2) - for this one I've also written some step definitions for you
- [Java, JUnit](https://cyber-dojo.org/forker/fork_group/aJJEN4?index=2)
- [Python, unittest](https://cyber-dojo.org/forker/fork_group/NFgFys?index=2)
- [Ruby, RSpec](https://cyber-dojo.org/forker/fork_group/D3xbUV?index=3)
- [Ruby, testunit](https://cyber-dojo.org/forker/fork_group/zlElgj?index=9)

## Better Code Hub

I analysed this repo according to the clean code standards on [Better Code Hub](https://bettercodehub.com) just to get an independent opinion of how bad the code is. Perhaps unsurprisingly, the compliance score is low!

[![BCH compliance](https://bettercodehub.com/edge/badge/emilybache/GildedRose-Refactoring-Kata?branch=master)](https://bettercodehub.com/) 
