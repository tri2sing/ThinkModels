'''
Created on Apr 13, 2015

@author: Sameer Adhikari
'''

from ps3c import *

viruses = [ResistantVirus(maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False}, mutProb=0.005)] * 5
for virus in viruses:
    print virus
viruses = [ResistantVirus(maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False}, mutProb=0.005) for i in range(5)] 
for virus in viruses:
    print virus
print 'hello'




