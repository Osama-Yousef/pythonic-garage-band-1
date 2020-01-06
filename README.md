# Lab 04 - pythonic-garage-band

**Author**: Aaron Imbrock
**Version**: 2.0.0

## Overview

Use a python class to model a Band made up of different kinds of musicians. Start with a Guitarist, Bassist, and Drummer. Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

## Requirements

* Python3.8
  * pytest

## Features

* Band Tests
  * A Band instance should have a name attribute which is a string.
  * A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
  * A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
  * A Band instance should have appropriate __str__ and __repr__ methods.
  * A Band should have a class method to_list which returns a list of previously created Band instances
  * A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
* Musician Subclass Tests
  * Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
  * Each kind of Musician instance should have a get_instrument method that returns string.
  * Each kind of Musician instance should have a play_solo method that returns string.

## API and Unit Tests

* Band Tests
  * test_band_name_exists - A Band instance should have a name attribute which returns a string.
  * test_band_members_list - A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
  * test_each_member_plays_solos - A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
  * test_band_magic_methods - A Band instance should have appropriate __str__ and __repr__ methods.
  * test_band_a_list - A Band should have a class method to_list which returns a list of previously created Band instances
  * test_band_create_from_data - A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
* Musician Subclass Tests
  * test_musician_magic_methods - Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
  * test_musician_get_instrument - Each kind of Musician instance should have a get_instrument method that returns string.
  * test_musician_play_solo - Each kind of Musician instance should have a play_solo method that returns string.

## Change Log

12-05-2019 09:15pm - Built Band, Musician, Guitarist, Bassist, and Drummer classes.
12-14-2019 22:17PM - 
