#!/usr/bin/env python

class Musician:
    all = []

    def __init__(self, style, role, instrument):
        self.role = role
        self.style = style
        self.instrument = instrument
        self.__class__.all.append(self)

    def __repr__(self):
        return f'{self.role} {self.instrument}'

    def __str__(self):
        return f'Plays the {self.instrument} in the {self.style}'

    def get_instrument(self):
        return self.instrument

class Guitarist(Musician):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass

class Keyboards(Musician):
    pass

guitarist = Guitarist('Metal', 'Guitarist', 'Fender')
bassist = Bassist('5 string', 'Bassist', 'Fender')
drummer = Drummer('Zenph', 'Drummer', 'Drums')
keyboards = Keyboards('Megoo', 'Keyboards', 'Keyboards')

class Band:
    all = []

    def __init__(self, band_name, members, type_of):
        self.band_name = band_name
        self.members = members
        self.type_of = type_of

band = Band('Led Zeppelin')
#print(Band.band_name, Musician.)