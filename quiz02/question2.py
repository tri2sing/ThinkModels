'''
Created on May 5, 2015

@author: Sameer Adhikari
'''

import pylab

a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
try:
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'

print ''
print 'Mean, Variance'    
l1 = [0,1,2,3,4,5,6,7,8]
print pylab.mean(l1), pylab.var(l1)

l2 = [5,10,10,10,15]
print pylab.mean(l2), pylab.var(l2)

l3 = [0,1,2,4,6,8]
print pylab.mean(l3), pylab.var(l3)

l4 = [6,7,11,12,13,15]
print pylab.mean(l4), pylab.var(l4)

l5 = [9,0,0,3,3,3,6,6]
print pylab.mean(l5), pylab.var(l5)

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

print ''
print 'Possible Variance'    
print possible_variance(l1)
print possible_variance(l2)
print possible_variance(l3)
print possible_variance(l4)
print possible_variance(l5)

