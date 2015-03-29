import random

class IntDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}' #res[:-1] removes the last comma


def collision_prob(numBuckets, numInsertions):
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision using a formula.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return 1 - prob

def sim_insertions(numBuckets, numInsertions):
    '''
    Run a simulation for numInsertions insertions into the hash table.
    '''
    choices = range(numBuckets)
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return False
        else:
            used.append(hashVal)
    return True

def observe_prob(numBuckets, numInsertions, numTrials):
    '''
    Given the number of buckets and the number of items to insert, 
    runs a simulation numTrials times to observe the probability of a collision.
    '''
    probs = []
    for t in range(numTrials):
        probs.append(sim_insertions(numBuckets, numInsertions))
    return 1 - sum(probs)/float(numTrials)

def main():
    hash_table = IntDict(25)
    hash_table.addEntry(15, 'a')
    random.seed(1) # Uncomment for consistent results
    for i in range(20):
        hash_table.addEntry(int(random.random() * (10 ** 9)), i)
    hash_table.addEntry(15, 'b')
    print hash_table.buckets  #evil
    print '\n', 'hash_table =', hash_table
    print hash_table.getValue(15)

if __name__ == '__main__':
    #main()
    
    print 'Generic test of probability of hash collisions'
    print 'HAsh function is a simple modulo operator'
    print 'Mathematical probability of collision: ', collision_prob(1000, 50)
    print 'Mathematical probability of collision: ', collision_prob(1000, 200)
    print 'Simulation probability of collision: ', observe_prob(1000, 50, 1000)
    print 'Simulation probability of collision: ', observe_prob(1000, 200, 1000)
    # To check the probabilities that two people have the same birthday
    # Simplification: assume that there are 365 days in a year.
    # Simplification: all birthdays are eqaually likely
    # We can emulate it using hash collisions: 
    # Number of days = number of buckets = 365
    # Number of people = number of insertions 
    
    print ''
    print 'Probability of two people having same birthday is a room of N people'
    print 'Mathematical probability of collision: ', collision_prob(365, 30)
    print 'Mathematical probability of collision: ', collision_prob(365, 250)
    print 'Simulation probability of collision: ', observe_prob(365, 30, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 250, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 250, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 150, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 100, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 100, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 90, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 80, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 70, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 60, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 59, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 58, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 57, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 56, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 55, 1000)
    print 'Simulation probability of collision: ', observe_prob(365, 50, 1000)
    
    
    



