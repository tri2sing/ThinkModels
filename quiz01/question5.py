'''
Created on Apr 6, 2015

@author: Sameer Adhikari
'''

import random

def sampleQuizzes():
    numTrials = 10000
    weightMid1 = 0.25
    weightMid2 = 0.25
    weightFinal = 0.5
    lowerBound = 70
    upperBound = 75
    scores = [0] * numTrials
    
    for i in range(numTrials):
        midTerm1 = random.randint(50, 80)
        midTerm2 = random.randint(60, 90)
        finalExam = random.randint(55, 95)
        scores[i] = weightMid1 * midTerm1 + weightMid2 * midTerm2 + weightFinal * finalExam
    
    subset = [score for score in scores if score >= lowerBound and score <= upperBound]
    
    return len(subset)/float(len(scores))
    
if __name__ == '__main__':
    print 'Probability = ', sampleQuizzes()