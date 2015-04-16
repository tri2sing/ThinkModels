'''
Created on Apr 15, 2015

@author: Sameer Adhikari
'''

# generate all combinations of N items
def powerSet(items):
    '''
    When all the subsets go into one bag, we represent the powerset as a set of bit vectors that range 
    in value from 0 to 2^N - 1.  For a given vector, when a bit is 1, that item is included in the subset.
     Since there are N items, and its bit can be one of two possibilities, there must be 2^N possibilities.
     This one provided by the instructors.
    '''
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2 ** N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
#for subset in powerSet([1, 2, 3, 4]):
#    print subset


def decimalToTernary(n, numDigits):
    """
    requires: n is a natural number less than 3**numDigits
    returns: a ternary string of length numDigits representing the the decimal number n.
    """
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 3**numDigits
    tStr = ''
    while n > 0:
        tStr = str(n % 3) + tStr
        n = n//3
    while numDigits - len(tStr) > 0:
        tStr = '0' + tStr
    return tStr

for i in range(3**2):
    print i, ' = ', decimalToTernary(i, 2)

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
      We represent the two bags as a list of "trinary" bits, 0, 1, or 2.
      A 0 means that an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2). 
      With the "trinary" bits, there are N bits that can each be one of three possibilities
      thus there must be 3^N possible combinations.
      This one implemented by me to submit it class
      Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(3 ** N):
        bag1 = []
        bag2 = []
        ternary = decimalToTernary(i, N)
        for j in xrange(N):
            tbit = int(ternary[j])
            if tbit % 3 == 1:
                bag1.append(items[j])
            elif tbit % 3 == 2:
                bag2.append(items[j])
        yield bag1, bag2
                            
for subset in yieldAllCombos(['a', 'b']):
    print subset
