#!/usr/bin/env python

class Band:
    '''Parent class which creates band instance'''
    all_bands = []

    def __init__(self, name, members):
        '''Takes in band name, members, and appends band to all_bands'''
        self.name = str(name)
        self.members = members
        self.__class__.all_bands.append(self)

    def __str__(self):
        '''Return band name'''
        return f'{self.name}'

    def __repr__(self):
        '''TODO: Make this better'''
        return f'{self.name} with members {self.members}'

    def play_solos(self):
        '''Prints str of band member play_solo method'''
        for member in self.members:
            solo = member.play_solo()
            print(solo)

    @classmethod
    def to_list(cls):
        '''Returns all Band instances from all_bands list'''

        return cls.all_bands

    @staticmethod
    def create_from_data(data):
        """
        Return created Band instance w/ associated, newly created, band member instances
        by parsing a string with 'Band Name, Musician Name_1, Instrument_1, Musician Name_2, Instrument_2'
        """
        data = data.split(',')
        band_name = data.pop(0)
        members_list = []
        for _ in range(len(data)//2):
            name = data.pop(0).strip()
            instrument = data.pop(0).strip()
            member = Musician(name, instrument)
            members_list.append(member)

        return Band(band_name, members_list)

class Musician:
    """
    Parent class Musician:
    __init__ - magic method, creates musician class from provided parameters
    __repr__ - magic method, returns str of musician object
     __str__ - magic method, returns str describing instantiated musician properties
    get_instrument() - method, returns instrument as str
         play_solo() - method, returns str '{name} plays {instrument}
    """

    all = []

    def __init__(self, musician_name, instrument):
        self.name = musician_name
        self.instrument = instrument
        self.__class__.all.append(self)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'Plays the {self.instrument}'

    def get_instrument(self):
        return self.instrument()
    
    def play_solo(self):
        return f'{self.name} plays {self.instrument}'

class Guitarist(Musician):
    '''From Musician class, creates guitarist class'''
    def __init__(self, name):
        super().__init__(name, 'guitar')

class Bassist(Musician):
    '''From Musician class, creates Bassist class'''
    def __init__(self, name):
        super().__init__(name, 'bass')

class Drummer(Musician):
    '''From Musician class, creates Drummer class'''
    def __init__(self, name):
        super().__init__(name, 'drums')

def read_band_data_file(file='./assets/band_data.txt'):
    '''Read data from file, used for creating bands'''
    
    with open(file, 'r') as reader:
        
        return reader.read()

if __name__ == "__main__":
    tools = Band.create_from_data(read_band_data_file())
    
    tools.play_solos()
