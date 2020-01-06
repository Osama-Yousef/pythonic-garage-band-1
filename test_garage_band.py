# * Band Tests

from garage_band import Band, Musician, read_band_data_file, Drummer, Bassist, Guitarist
import pytest

#the_band = create_from_data(read_band_data_file())
monkeys = Band('Blah', [Drummer('Dude'), Guitarist('Eddy')])
tool = Band.create_from_data(read_band_data_file())

def test_band_name_exists():
    '''A Band instance should have a name attribute which returns a string.'''
    assert tool.name == 'The Monkeys'

def test_all_bands():
    '''A Band instance should have a members attribute which is a
    list of instances that inherit from Musician base (or super) class.'''
    assert Band.all_bands == ['Blah','The Monkeys']

# def test_guitarist_play_solo():
#     '''A Band instance should have a play_solos method that asks
#     each member musician to play a solo, in the order they were added to band.'''
#     assert Guitarist('Eddy').play_solo() == 'Eddy plays a guitar solo'

def test_band_a_list():
    '''A Band should have a class method to_list which returns a 
    list of previously created Band instances'''
    assert Band.to_list() == ['Blah','The Monkeys']

def test_band_play_solos():
    band_solos = tool.play_solos()
    assert 'Micky Dolenz plays a guitar solo' in band_solos
    assert 'Michael Nesmith plays a drums solo' in band_solos
    assert 'Davy Jones plays a banjo solo' in band_solos
    assert 'Peter Tork plays a cymbals solo' in band_solos

def test_band_create_from_data():
    '''A Band should have a static method create_from_data which takes a collection 
    of formatted data and returns a created Band instance. 
    The Band instance should have its members be set to musicians based on info from the input.'''
    Band.create_from_data(read_band_data_file())
    assert Band.to_list() == ['Blah','The Monkeys', 'The Monkeys']

# * Musician Subclass Tests

def test_musician_get_instrument():
    '''Each kind of Musician instance should have a get_instrument method that returns string.'''
    assert Guitarist('Eddy').get_instrument() == 'guitar'
    assert Drummer('Eddy').get_instrument() == 'drums'
    assert Bassist('Eddy').get_instrument() == 'bass'

def test_musician_play_solo():
    '''Each kind of Musician instance should have a play_solo method that returns string.'''
    assert Guitarist('Eddy').play_solo() == 'Eddy plays a guitar solo'
    assert Drummer('Eddy').play_solo() == 'Eddy plays a drums solo'
    assert Bassist('Eddy').play_solo() == 'Eddy plays a bass solo'
