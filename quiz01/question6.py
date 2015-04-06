'''
Created on Apr 6, 2015

@author: Sameer Adhikari
'''

def probTest(limit):
    '''
    You roll a six-sided die with sides with numbers 1 through 6 several times.
    The probability of first seeing a 1 on the n-th roll decreases as n increases.
    
    Returns: The smallest number of rolls such that this probability is less than some limit. 
    '''
    probability = 1.0/6.0
    rolls = 1
    while probability > limit:
        probability *= (5.0/6.0)
        rolls += 1
    return rolls

if __name__ == '__main__':
    print 'Rolls = ', probTest(1.0/6.0)
    print 'Rolls = ', probTest(5.0/36.0)
    print 'Rolls = ', probTest(25.0/216.0)
    print 'Rolls = ', probTest(0.005)
