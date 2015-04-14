# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3c import *
#from problemset03.ps3b import *

def singleTrial(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05,
                mutProb=0.005, stepsBeforeDrug=0, stepsAfterDrug=150):
    '''
    '''
    resistances = {'guttagonol': False}
    totalViruses = 0 
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for m in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
    for step in range(stepsBeforeDrug):
        totalViruses = patient.update()
    patient.addPrescription('guttagonol')
    for step in range(stepsBeforeDrug, stepsBeforeDrug + stepsAfterDrug):
        totalViruses = patient.update()
    return totalViruses


#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    stepsBefore = [300, 150, 75, 0]
    for k in range(len(stepsBefore)):
        totals = [0] * numTrials
        for i in range(numTrials):
            totals[i] = singleTrial(stepsBeforeDrug=stepsBefore[k])
        print 'Done with steps before treatment = ' + str(stepsBefore[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Steps before = ' + str(stepsBefore[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   


#simulationDelayedTreatment(250)

def simulationVirusListLength(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    virusListLength = [50, 100, 150, 200]
    for k in range(len(virusListLength)):
        totals = [0] * numTrials
        for i in range(numTrials):
            totals[i] = singleTrial(numViruses=virusListLength[k], stepsBeforeDrug=150)
        print 'Done with virus list length = ' + str(virusListLength[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Virus List Length = ' + str(virusListLength[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

#simulationVirusListLength(250)

def simulationMaxPopCount(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    maxPop = [1000, 1500, 2000, 2500]
    for k in range(len(maxPop)):
        totals = [0] * numTrials
        for i in range(numTrials):
            totals[i] = singleTrial(maxPop=maxPop[k], stepsBeforeDrug=150)
        print 'Done with max pop count = ' + str(maxPop[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Max Pop Count = ' + str(maxPop[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

#simulationMaxPopCount(125)

def simulationMaxBirthProb(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    maxBirthProb = [0.1, 0.2, 0.3, 0.4]
    for k in range(len(maxBirthProb)):
        totals = [0] * numTrials
        for i in range(numTrials):
            totals[i] = singleTrial(maxBirthProb=maxBirthProb[k], stepsBeforeDrug=150)
        print 'Done with max birth prob = ' + str(maxBirthProb[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Max Birth Prob = ' + str(maxBirthProb[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

#simulationMaxBirthProb(100)

def simulationClearProb(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    clearProb = [0.05, 0.1, 0.15, 0.2]
    for k in range(len(clearProb)):
        totals = [0] * numTrials
        for i in range(numTrials):
            totals[i] = singleTrial(clearProb=clearProb[k], stepsBeforeDrug=150)
        print 'Done with clear prob = ' + str(clearProb[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Clear Prob = ' + str(clearProb[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

simulationClearProb(100)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
