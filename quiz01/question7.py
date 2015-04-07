'''
Created on Apr 6, 2015

@author: Sameer Adhikari
'''

import random
import pylab

EMPTY = 0
WHITE = 1
BLACK = 2


def createCollection(size):
    '''
    Generate a collection that randomly half white labels and half black labels.
    Size: an even integer (no error checking for now)
    
    Returns: the collection with half white labels and half black labels.
    '''
    collection = [EMPTY] * size
    count = 0

    while count < size / 2:
        target = random.randint(0, size - 1)
        if collection[target] == EMPTY:
            collection[target] = WHITE
            count += 1
    
    for i in range(size):
        if collection[i] == EMPTY:
            collection[i] = BLACK
                
    return collection


def LV(collection):
    '''
    Point to a random location in collection. If it is white, then exit. 
    If it is black, then repeat (e.g. choose another random location, and test).
    
    Returns: number of tries to find a white label
    '''
    size = len(collection)
    attempts = 1
    while collection[random.randint(0, size - 1)] != WHITE:
        attempts += 1
    return attempts


def MC(collection, maxAttempts):
    '''
    Point to a random location in the list. If the location is white, then return 1. 
    If it is black, then examine the next item in the list. 
    If it is white, return 2, and if it is black, continue with the next item in the list.
    
    Returns: number of locations examined to find white label within maxAttempts, else 0
    '''
    size = len(collection)
    attempts = 1
    target = random.randint(0, size - 1)
    while attempts < maxAttempts and collection[target] != WHITE:
        attempts += 1
        target += 1
    if collection[target] != WHITE:
        return 0
    else:
        return attempts

    
if __name__ == '__main__':
    random.seed(7)
    labels = createCollection(1000)
    print labels
    size = len(labels)
    
    histogram = [0] * size
    for i in range(size):
        result = LV(labels)
        histogram[result] += 1
    
    print len(histogram)
    print histogram
    pylab.plot([i for i in range(1, size)], histogram[1:])
    pylab.title('LV')
    pylab.xlim(1, 50)
    pylab.show()

    histogram = [0] * size
    for i in range(size):
        result = MC(labels, 5)
        histogram[result] += 1
    
    print len(histogram)
    print histogram
    pylab.plot([i for i in range(1, size)], histogram[1:])
    pylab.title('MC')
    pylab.xlim(1, 50)
    pylab.show()

