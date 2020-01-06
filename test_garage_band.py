# * Band Tests

from garage_band import Band, Musician

def test_band_name_exists():
    '''A Band instance should have a name attribute which returns a string.'''
    pass

def test_band_members_list():
    '''A Band instance should have a members attribute which is a
    list of instances that inherit from Musician base (or super) class.'''
    pass

def test_each_member_plays_solos():
    '''A Band instance should have a play_solos method that asks
    each member musician to play a solo, in the order they were added to band.'''
    pass

def test_band_magic_methods():
    '''A Band instance should have appropriate __str__ and __repr__ methods.'''
    pass

def test_band_a_list():
    '''A Band should have a class method to_list which returns a 
    list of previously created Band instances'''
    pass

def test_band_create_from_data():
    '''A Band should have a static method create_from_data which takes a collection 
    of formatted data and returns a created Band instance. 
    The Band instance should have its members be set to musicians based on info from the input.'''
    pass

# * Musician Subclass Tests

def test_musician_magic_methods():
    '''Each kind of Musician instance should have appropriate __str__ and __repr__ methods.'''
    pass

def test_musician_get_instrument():
    '''Each kind of Musician instance should have a get_instrument method that returns string.'''
    pass

def test_musician_play_solo():
    '''Each kind of Musician instance should have a play_solo method that returns string.'''
    pass
