'''
Created on Apr 5, 2015

@author: Sameer Adhikari
'''

import pylab
import random
import math

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)    


class Simulator(object):

    def oneWalk(self, field, drunk, numSteps):
        start = field.getLoc(drunk)
        for i in range(numSteps):
            field.moveDrunk(drunk)    
        end = field.getLoc(drunk)
        return start.distanceFrom(end)
    
    def oneVector(self, field, drunk, numSteps):
        start = field.getLoc(drunk)
        for s in range(numSteps):
            field.moveDrunk(drunk)
        return(field.getLoc(drunk).getX() - start.getX(),
               field.getLoc(drunk).getY() - start.getY())

    def manyWalks(self, drunk, numSteps, numTrias):
        origin = Location(0, 0)
        distances = []
        for i in range(numTrias):
            field = Field()
            field.addDrunk(drunk, origin)
            distance = self.oneWalk(field, drunk, numSteps)
            distances.append(distance)
        return distances

    def manyVectors(self, drunk, numSteps, numTrias):
        origin = Location(0, 0)
        vectors = []
        for i in range(numTrias):
            field = Field()
            field.addDrunk(drunk, origin)
            vector = self.oneVector(field, drunk, numSteps)
            vectors.append(vector)
        return vectors
        
    def runWalks(self, drunk, numTrias):
        for numSteps in [0, 1, 10, 100, 1000, 10000]:
            distances = self.manyWalks(drunk, numSteps, numTrias)
            print 'Random walk of steps = ' + str(numSteps)
            print 'Average distance = ', str(sum(distances)/len(distances))
            print 'Max distance = ', str(max(distances))
            print 'Min distance = ', str(min(distances))
            print
        
    def runVectors(self, drunk, numTrias):
        for numSteps in [0, 1, 10, 100, 1000, 1000]:
            vectors = self.manyVectors(drunk, numSteps, numTrias)
        return vectors
            
if __name__ == '__main__':
        numTrials = 1000
        sim = Simulator()

        drunk = ColdDrunk('ColdDrunk')
        vectors = sim.runVectors(drunk, numTrials)
        pylab.title(str(drunk))
        pylab.scatter(*zip(*vectors))
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.show()
        
        drunk = EDrunk('DDrunk')
        vectors = sim.runVectors(drunk, numTrials)
        pylab.title(str(drunk))
        pylab.scatter(*zip(*vectors))
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.show()

        drunk = EDrunk('EDrunk')
        vectors = sim.runVectors(drunk, numTrials)
        pylab.title(str(drunk))
        pylab.scatter(*zip(*vectors))
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.show()
        
        drunk = EDrunk('PhotoDrunk')
        vectors = sim.runVectors(drunk, numTrials)
        pylab.title(str(drunk))
        pylab.scatter(*zip(*vectors))
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.show()

        drunk = EDrunk('UsualDrunk')
        vectors = sim.runVectors(drunk, numTrials)
        pylab.title(str(drunk))
        pylab.scatter(*zip(*vectors))
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.show()

        
        

