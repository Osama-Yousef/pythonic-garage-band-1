#!/usr/bin/env python

class Band:
    all_bands = []

    def __str__(self):
        '''TODO: Add all members to string. String comprehension possible?'''
        return f'{self.name}'

    def __repr__(self):
        '''TODO: Make this better'''
        return f'{self.name}'

    def __init__(self, name, members):
        self.name = str(name)
        self.members = members
        self.__class__.all_bands.append(self)

    def play_solos(self):
        for member in self.members:
            print(member.play_solo())

    @classmethod
    def to_list(cls):
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
        for _ in range(len(data)/2):
            name = data.pop(0)
            instrument = data.pop(0)
            member = Musician(name, instrument)
            members_list.append(member)

        return Band(band_name, members_list)

class Musician:
    all = []

    def __init__(self, musician_name, instrument):
        self.name = musician_name
        self.instrument = instrument
        self.__class__.all.append(self)

    def __repr__(self, name):
        return self.name

    def __str__(self):
        return f'Plays the {self.instrument}'

    def get_instrument(self):
        return self.instrument()
    
    def play_solo(self):
        return f'{self.name} plays {self.instrument}'

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitar')

# class Bassist(Musician):
#     def __init__(self, name):
#         super().__init__(name, 'bass')

# class Drummer(Musician):
#     def __init__(self, name):
#         super().__init__(name, 'drums')

# # A volcalist 'Is A' Musician
# # 
# class Vocalist(Musician):
#     def __repr__(self):
#         return f'Vocalist {self.name}'
        
#     def __str__(self):
#         return 'I am a Vocalist name {self.name}'
