'''
Created on Mar 24, 2015

@author: Sameer Adhikari
'''

import random

class Drunk(object):

    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return 'The name of this drunk is ' + self.name
    
    

class BasicDrunk(Drunk):
    
    def choose_step(self):
        # Can choose_step either North, South, East, or West with equal probability
        choices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(choices)