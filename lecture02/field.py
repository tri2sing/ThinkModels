'''
Created on Mar 24, 2015

@author: sadhikar
'''

class Field(object):

    def __init__(self):
        # Track drunks on the field and their locations
        self.drunks = {}
     
    def add_drunk(self, drunk, location):
        if drunk in self.drunks:
            raise ValueError('Drunk already on field, cannot add again')   
        else:
            self.drunks[drunk] = location
            
    def get_drunk_location(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            return self.drunks[drunk]
        
    def move_drunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            xdist, ydist = drunk.choose_step()
            self.drunks[drunk] = self.drunks[drunk].change_location(xdist, ydist)