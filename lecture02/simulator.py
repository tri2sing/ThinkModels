'''
Created on Mar 25, 2015

@author: Sameer Adhikari
'''

from lecture02.drunk import BasicDrunk
from lecture02.location import Location
from lecture02.field import Field

class Simulator(object):

    def one_walk(self, field, drunk, num_steps):
        start = field.get_drunk_location(drunk)
        for i in range(num_steps):
            field.move_drunk(drunk)    
        end = field.get_drunk_location(drunk)
        return start.distance_from(end)
    
    def many_walks(self, num_steps, num_trials):
        drunk = BasicDrunk('RandomDrunk')
        origin = Location(0, 0)
        distances = []
        for i in range(num_trials):
            field = Field()
            field.add_drunk(drunk, origin)
            distance = self.one_walk(field, drunk, num_steps)
            distances.append(distance)
        return distances
    
    def run_simulation(self, num_trials):
        for num_steps in [0, 1, 10, 100, 1000, 10000]:
            distances = self.many_walks(num_steps, num_trials)
            print 'Random walk of steps = ' + str(num_steps)
            print 'Average distance = ', str(sum(distances)/len(distances))
            print 'Max distance = ', str(max(distances))
            print 'Min distance = ', str(min(distances))
            print
        
            
if __name__ == '__main__':
    sim = Simulator()
    sim.run_simulation(100)