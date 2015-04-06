'''
Created on Mar 28, 2015

@author: sadhikar
'''

from lecture03.die import Die

class Simulator(object):
    '''Represents the entity that rolls the die'''

    def num_tries_to_get_target(self, sides, target):
        '''
        Represents rolling a die N times till output matches target
        target: pattern to obtain in rolling the dies
        return: number of attempts 
        '''    
        N = len(target) # A die has to roll N times to equal the length of the target pattern
        numTries = 0
        die = Die(sides)
        while True:
            result = die.rollNTimes(N)
            numTries += 1
            if result == target:
                return numTries
    
    def runSimulation(self, sides, target, numTrials):  
        totalTries = 0
        for i in range(numTrials):
            totalTries += self.num_tries_to_get_target(sides, target)
        print 'Average number of tries per trial =', totalTries/float(numTrials)
        
if __name__ == '__main__':
    simu = Simulator()
    sides = 6
    simu.runSimulation(sides, '11111', 100)
    simu.runSimulation(sides, '12345', 100)           