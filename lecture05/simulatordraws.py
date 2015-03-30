'''
Created on Mar 29, 2015

@author: Sameer Adhikari
'''

import random


def drawsThreeOfOneColor(balls, numDraws):
    '''
    returns: number of draws to get three of one color.
    '''
    #random.seed(0) # For testing
    numGreen = 0
    numRed = 0    
    length = len(balls)
    for i in range(numDraws):  # perform draws without replacement
        choice = random.randint(0, length - 1)
        color = balls.pop(choice)
        #print 'Popped index %d color %c' % (choice, color)
        if color == 'R':
            numRed += 1
        else:
            numGreen += 1
        length -= 1
    if numRed == 3 or numGreen == 3:
        return True
    else:
        return False

    
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTimesThree = 0
    for i in range(numTrials):
        balls = ['R', 'G', 'R', 'G', 'R', 'G']
        threeOneColor = drawsThreeOfOneColor(balls, 3)
        if threeOneColor == True:
            numTimesThree += 1
    #print 'Num times three of one color = ', numTimesThree
    return numTimesThree/float(numTrials)

if __name__ == '__main__':
    print noReplacementSimulation(10)
    print noReplacementSimulation(100)    
    print noReplacementSimulation(1000)
    print noReplacementSimulation(10000)
    print noReplacementSimulation(100000)
    print noReplacementSimulation(100000)