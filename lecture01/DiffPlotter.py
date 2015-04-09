'''
Created on Mar 24, 2015

@author: Sameer Adhikari
'''
import pylab
import numpy as np

class Plotter(object):
    '''
    '''
    
    def __init__(self, path=''):
        '''
        '''
        self.lines = open(path).readlines()
        self.high = []
        self.low = []
        
    def process_data(self):
        '''
        '''
        if self.lines:
            for line in self.lines:
                fields = line.split() 
                if len(fields) == 3 and fields[0].isdigit():
                    self.high.append(int(fields[1]))
                    self.low.append(int(fields[2]))    
        
    
    def plot_diffs(self):
        '''
        '''
        diffs = list(np.array(self.high) - np.array(self.low))
        pylab.plot(range(1,32), diffs)
        pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
        pylab.xlabel('Days')
        pylab.ylabel('Temperature Ranges')
        pylab.show()


    def print_data(self):
        '''
        '''
        for i in range(len(self.high)):
            print str(i + 1) + ':' + str(self.high[i]) + ' ' + str(self.low[i])
            

if __name__ == '__main__':
    plotter = Plotter('C:\\Users\\sadhikar\\Documents\\workspacepython\\ThinkModels\\Inputs\\JulyTemps.txt')
    plotter.process_data()
    plotter.print_data()
    plotter.plot_diffs()
    