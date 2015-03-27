'''
Created on Mar 24, 2015

@author: sadhikar
'''

class Location(object):

    def __init__(self, x, y):
        '''x and y are floats'''
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def change_location(self, xdelta, ydelta):
        '''xdelta and ydelta are floats'''
        return Location(self.x + xdelta, self.y + ydelta)
    
    def distance_from(self, other):
        xdist = other.x - self.x
        ydist = other.y - self.y
        return (xdist**2 + ydist**2)**0.5
       
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>' 