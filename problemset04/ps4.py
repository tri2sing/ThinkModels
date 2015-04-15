# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3c import *
# from problemset03.ps3b import *

def trialOnePrescription(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05,
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


def singleTrialKWArgs(**kwargs):
    '''
    numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05, mutProb=0.005, stepsBeforeDrug=0, stepsAfterDrug=150
    '''
    numViruses = kwargs['numViruses'] if 'numViruses' in kwargs else 100
    maxPop = kwargs['maxPop'] if 'maxPop' in kwargs else 1000
    maxBirthProb = kwargs['maxBirthProb'] if 'maxBirthProb' in kwargs else 0.1
    clearProb = kwargs['clearProb'] if 'clearProb' in kwargs else 0.5
    mutProb = kwargs['mutProb'] if 'mutProb' in kwargs else 0.05
    stepsBeforeDrug = kwargs['stepsBeforeDrug'] if 'stepsBeforeDrug' in kwargs else 0
    stepsAfterDrug = kwargs['stepsAfterDrug'] if 'stepsAfterDrug' in kwargs else 150
    
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
            totals[i] = trialOnePrescription(stepsBeforeDrug=stepsBefore[k])
        print 'Done with steps before treatment = ' + str(stepsBefore[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Steps before = ' + str(stepsBefore[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   


# simulationDelayedTreatment(250)

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
            totals[i] = trialOnePrescription(numViruses=virusListLength[k], stepsBeforeDrug=150)
        print 'Done with virus list length = ' + str(virusListLength[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Virus List Length = ' + str(virusListLength[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

# simulationVirusListLength(250)

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
            totals[i] = trialOnePrescription(maxPop=maxPop[k], stepsBeforeDrug=150)
        print 'Done with max pop count = ' + str(maxPop[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Max Pop Count = ' + str(maxPop[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

# simulationMaxPopCount(125)

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
            totals[i] = trialOnePrescription(maxBirthProb=maxBirthProb[k], stepsBeforeDrug=150)
        print 'Done with max birth prob = ' + str(maxBirthProb[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Max Birth Prob = ' + str(maxBirthProb[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

# simulationMaxBirthProb(100)

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
            totals[i] = trialOnePrescription(clearProb=clearProb[k], stepsBeforeDrug=150)
        print 'Done with clear prob = ' + str(clearProb[k])
        pylab.subplot(2, 2, k + 1)
        pylab.title('Clear Prob = ' + str(clearProb[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

# simulationClearProb(100)


def simulationGivenFactor(numTrials=0, stepsBeforeDrug=150, factorName='', factorValues=[]):
    '''
    '''
    print 'numTrials = ', numTrials
    print 'stepsBeforeDrugs = ', stepsBeforeDrug
    print 'factorName = ', factorName
    print 'factorValues = ', factorValues
    
    pylab.figure()
    numValues = len(factorValues)
    for k in range(numValues):
        totals = [0] * numTrials
        for i in range(numTrials):
            args = {}
            args[str(factorName)] = factorValues[k]
            args['stepsBeforeDrug'] = stepsBeforeDrug
            totals[i] = trialOnePrescription(**args)
        print 'Done with'  + factorName + ' = ' + str(factorValues[k])
        pylab.subplot(numValues / 2, numValues - (numValues / 2), k + 1)
        pylab.title(factorName + ' = ' + str(factorValues[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   
    

#simulationGivenFactor(numTrials=10, stepsBeforeDrug=150, factorName='numViruses', factorValues=[50, 100, 150, 200])
#simulationGivenFactor(numTrials=10, stepsBeforeDrug=150, factorName='maxPop', factorValues=[1000, 1500, 2000, 2500])
#simulationGivenFactor(numTrials=10, stepsBeforeDrug=150, factorName='maxBirthProb', factorValues=[0.1, 0.2, 0.3, 0.4])
#simulationGivenFactor(numTrials=10, stepsBeforeDrug=150, factorName='clearProb', factorValues=[0.05, 0.1, 0.15, 0.2])


def trialTwoPrescriptions(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05, mutProb=0.005, 
                          stepsBeforeFirstDrug=150, stepsBetweenTwoDrugs=0, stepsAfterSecondDrug=150,
                          ):
    '''
    '''
    resistances = {'guttagonol': False, 'grimpex': False}
    totalViruses = 0 
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for m in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
    for _ in range(stepsBeforeFirstDrug):
        totalViruses = patient.update()
    patient.addPrescription('guttagonol')
    for _ in range(stepsBeforeFirstDrug, stepsBeforeFirstDrug + stepsBetweenTwoDrugs):
        totalViruses = patient.update()
    patient.addPrescription('grimpex')
    for _ in range(stepsBeforeFirstDrug + stepsBetweenTwoDrugs, stepsBeforeFirstDrug + stepsBetweenTwoDrugs + stepsAfterSecondDrug):
        totalViruses = patient.update()
    return totalViruses

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
    pylab.figure()
    stepsBetweenTwoDrugs = [300, 150, 75, 0]
    numValues = len(stepsBetweenTwoDrugs)
    for k in range(numValues):
        totals = [0] * numTrials
        for i in range(numTrials):
            totals[i] = trialTwoPrescriptions(stepsBetweenTwoDrugs=stepsBetweenTwoDrugs[k])
        print 'Done with steps between treatments = ' + str(stepsBetweenTwoDrugs[k])
        pylab.subplot(numValues / 2, numValues - (numValues / 2), k + 1)
        pylab.title('Steps between = ' + str(stepsBetweenTwoDrugs[k]))
        pylab.ylabel('Number of Trials')
        pylab.hist(totals, 11)
    pylab.show()   

simulationTwoDrugsDelayedTreatment(250)