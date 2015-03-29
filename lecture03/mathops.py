'''
Created on Mar 28, 2015

@author: Sameer Adhikari
'''

from math import pow

def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings, or NaN if L is empty.
    """
    # This function is what I had to write
    if not L:
        return float('NaN')
    num = float(len(L))
    lengths = [len(x) for x in L]
    mu = sum(lengths)/num
    sumsquares = sum([(x - mu)*(x - mu) for x in lengths])
    return pow(sumsquares/num, 0.5)
        

if __name__ == '__main__':
    print stdDevOfLengths(['a', 'z', 'p'])
    print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
