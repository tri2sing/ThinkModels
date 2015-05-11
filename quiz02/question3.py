import sys
import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    if CURRENTRABBITPOP == MAXRABBITPOP:
        return # Do nothing
    prabbitborn  = 1.0 - float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
    if random.random() < prabbitborn:
        CURRENTRABBITPOP = CURRENTRABBITPOP + 1 # Rabbit reproduces
           
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    if CURRENTFOXPOP <= 10:
        return # Nothing happens
    
    if CURRENTRABBITPOP <= 10 and random.randint() < 0.1:
        CURRENTFOXPOP = CURRENTFOXPOP - 1  # Fox dies
        return

    # At this point the rabbit population is guaranteed > 10
    pfoxeats = float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
    if random.random() < pfoxeats:
        CURRENTRABBITPOP = CURRENTRABBITPOP - 1
        if random.random() < 1.0/3.0:
            CURRENTFOXPOP = CURRENTFOXPOP + 1 # Fox reproduces
    else: # Fox does not get to eat
        if random.random() < 0.1:
            CURRENTFOXPOP = CURRENTFOXPOP - 1 # Fox dies
        
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    numrabbits = [0] * numSteps
    numfoxes = [0] * numSteps
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        numrabbits[i] = CURRENTRABBITPOP
        numfoxes[i] = CURRENTFOXPOP
    
    return numrabbits, numfoxes


def test():
    numSteps = 200
    numrabbits, numfoxes = runSimulation(numSteps)
    print numrabbits
    print numfoxes
    pylab.title("Simulation of rabbit and fox population growth")
    pylab.xlabel('Steps')
    pylab.ylabel('Population Size')
    xvals = [i for i in range(numSteps)]
#    pylab.plot(xvals, numrabbits, label='rabbits')
#    pylab.plot(xvals, numfoxes, label = 'foxes')
    pylab.subplot(2, 1, 1)
    coeffrabbits = pylab.polyfit(range(len(numrabbits)), numrabbits, 2)
    pylab.plot(pylab.polyval(coeffrabbits, range(len(numrabbits))), label='rabbits')
    pylab.subplot(2, 1, 2)
    coeffoxes = pylab.polyfit(range(len(numfoxes)), numfoxes, 2)
    pylab.plot(pylab.polyval(coeffoxes, range(len(numfoxes))), label='foxes')
    pylab.legend()
    pylab.show()

if __name__ == '__main__':    
    test()
