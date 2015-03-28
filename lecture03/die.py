'''
Created on Mar 28, 2015

@author: Sameer Adhikari
'''

import random

class Die(object):
    ''' Class the represent a N-sided die'''
    
    def __init__(self, numSides):
        '''Create a die with given number of sides'''
        self.sides = [i for i in range(1, numSides + 1)]
        
    def roll(self):
        '''Represents the roll of a six side die'''
        return random.choice(self.sides)

    def rollNTimes(self, N):
        '''
        Represent the roll of a die N times.  
        The result ss a string concatenation of the single rolls
        '''
        result = ''
        for i in range(N):
            result = result + str(self.roll())
        return result

if __name__ == '__main__':
    die = Die(6)
    print die.rollNTimes(5)
