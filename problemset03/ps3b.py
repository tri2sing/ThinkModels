# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 
# I have to fill the the shell functions with the solution

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance (removal from patient) probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if random.random() < self.clearProb:
            return True
        else:
            return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        randVal = random.random()
        threshold = self.maxBirthProb * (1 - popDensity) 
        if randVal < threshold:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        if self.viruses:
            return len(self.viruses)
        else:
            return 0


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        if not self.viruses:
            return 0
        survivors = [x for x in self.viruses if x.doesClear() == False]
        if not survivors:
            self.viruses = []
            return 0
        density = len(survivors)/float(self.maxPop)
        children = []
        for x in survivors:
            try:
                child = x.reproduce(density)
                children.append(child)
            except NoChildException:
                pass
        if not children:
            self.viruses = survivors
        else:
            self.viruses = survivors + children
        return len(self.viruses)


#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    timeSteps = 300  # duration for each trial
    # cumulative number of viruses for a step, after each trial, initially 0
    cumStepPop = [0 for i in range(timeSteps)] 
    
    for j in range(numTrials):
        # Create the initial number of viruses
        viruses = [SimpleVirus(maxBirthProb, clearProb) for m in range(numViruses)]
        # Create a patient
        patient = Patient(viruses, maxPop)
        stepPop = [patient.update() for n in range(timeSteps)]
        addPop = [cumStepPop[s] + stepPop[s] for s in range(timeSteps)]
        cumStepPop = addPop
        #print 'Step DONE = ', j
    avgPop = [cumStepPop[t] / numTrials for t in range(timeSteps)]
    print avgPop
    print ''
    pylab.plot([k for k in range (1, timeSteps + 1, 1)], avgPop, label="Virus Count")
    pylab.title("Viruses after each time step")
    pylab.xlabel("Time Step")
    pylab.ylabel("Virus Count")
    pylab.legend()
    pylab.show()
    
        
#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug in self.resistances:
            return self.resistances[drug]
        else:
            return False 

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistKey trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistKey trait from the parent, and probability
        mutProb of switching that resistKey trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistKey to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistKey to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        
        # If the virus is not resistant to any drug and 
        # the list of active drugs is not empty
        if not self.resistances and activeDrugs:
            raise NoChildException
        
        # Determine if the virus is resistant to all active drugs
        for drug in activeDrugs:
            if not self.resistances[drug]:
                raise NoChildException
        
        # Reproduce the virus with a given probability
        randVal = random.random()
        threshold = self.maxBirthProb * (1 - popDensity) 
        if randVal >= threshold:
            raise NoChildException
        
        # Generate child resistances from parent based on probability
        childResists = {}
        for resistKey, resistVal in self.resistances.iteritems():
            randVal = random.random()
            if randVal < self.mutProb: 
                childResists[resistKey] = not resistVal
            else:
                childResists[resistKey] = resistVal
                
        return ResistantVirus(self.maxBirthProb, self.clearProb, childResists, self.mutProb)    

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.prescriptions = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.prescriptions:
            self.prescriptions.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.prescriptions


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        
        count = 0
        for virus in self.viruses:
            resistsAll = True
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    resistsAll = False
                    break
            if resistsAll == True:
                count += 1
        return count


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        if not self.viruses:
            return 0
        survivors = [virus for virus in self.viruses if virus.doesClear() == False]
        if not survivors:
            self.viruses = []
            return 0
        density = len(survivors)/float(self.maxPop)
        children = []
        for x in survivors:
            try:
                child = x.reproduce(density, self.prescriptions)
                children.append(child)
            except NoChildException:
                pass
        if not children:
            self.viruses = survivors
        else:
            self.viruses = survivors + children
        return len(self.viruses)



#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    timeSteps = 300  # duration for each trial
    # cumulative number of viruses for a step, after each trial, initially 0
    cumStepPop = [0 for i in range(timeSteps)] 
    cumResistPop = [0 for i in range(timeSteps)]
    
    for j in range(numTrials):
        # Create the initial number of viruses
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for m in range(numViruses)]
        # Create a patient
        patient = TreatedPatient(viruses, maxPop)
        stepPop = []
        resistPop = []
        for step in range(timeSteps/2):
            stepPop.append(patient.update())
            resistPop.append(patient.getResistPop(['guttagonol']))
        patient.addPrescription('guttagonol')
        for step in range(timeSteps/2, timeSteps):
            stepPop.append(patient.update())
            resistPop.append(patient.getResistPop(['guttagonol']))
        addPop = [cumStepPop[s] + stepPop[s] for s in range(timeSteps)]
        cumStepPop = addPop
        addPop = [cumResistPop[s] + resistPop[s] for s in range(timeSteps)]
        cumResistPop = addPop
        #print 'Step DONE = ', j
    avgTotalPop = [float(cumStepPop[t]) / float(numTrials) for t in range(timeSteps)]
    avgResistPop = [float(cumResistPop[t]) / float(numTrials) for t in range(timeSteps)]
    #print len(avgTotalPop), avgTotalPop
    #print len(avgResistPop), avgResistPop
    #print ''
    pylab.plot([k for k in range (1, timeSteps + 1, 1)], avgTotalPop, label="Total Count")
    pylab.plot([k for k in range (1, timeSteps + 1, 1)], avgResistPop, label="Resist Count")
    pylab.title("Viruses after each time step")
    pylab.xlabel("Time Step")
    pylab.ylabel("Virus Count")
    pylab.legend()
    pylab.show()
  
  
if __name__ == '__main__':
    print 'Started'
    random.seed(0)
    v1 = SimpleVirus(1.0, 0.0)
    #print 'v1.doesClear', v1.doesClear() # Expected answer is False
    #print 'v1.reproduce', v1.reproduce(0.25) # Expected answer is False
    #virus = SimpleVirus(1.0, 0.0)
    #patient = Patient([virus], 100)
    #for i in range(100):
    #    population = patient.update()
    #print 'Number of children', patient.getTotalPop()
    
    #simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)
    #simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
    #simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
    #simulationWithoutDrug(1, 90, 0.8, 0.1, 1)

    #virus = ResistantVirus(0.0, 1.0, {'guttagonol': True}, 0.0)
    #print "Virus is resistant to guttagonol", virus.isResistantTo('guttagonol')
    #patient = TreatedPatient([virus], 10)
    #rpop = patient.getResistPop(['guttagonol'])
    #print "Num resistant viruses in patient = ", rpop
    
    simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
    simulationWithDrug(1, 20, 1.0, 0.0, {'guttagonol': True}, 1.0, 5)
    simulationWithDrug(75, 100, .8, 0.1, {'guttagonol': True}, 0.8, 1)
    #simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)
    print 'Completed'
    
    