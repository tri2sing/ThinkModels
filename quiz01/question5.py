'''
Created on Apr 6, 2015

@author: Sameer Adhikari
'''

import random

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    weightMid1 = 0.25
    weightMid2 = 0.25
    weightFinal = 0.5
    scores = [0] * numTrials
    
    for i in range(numTrials):
        midTerm1 = random.randint(50, 80)
        midTerm2 = random.randint(60, 90)
        finalExam = random.randint(55, 95)
        scores[i] = weightMid1 * midTerm1 + weightMid2 * midTerm2 + weightFinal * finalExam
    
    return scores


def sampleQuizzes():
    """    
    Returns: The probability that the scores lie between [70, 75]
    """
    lowerBound = 70
    upperBound = 75
    scores = generateScores(10000)
    subset = [score for score in scores if score >= lowerBound and score <= upperBound]

    return len(subset)/float(len(scores))
    
    
if __name__ == '__main__':
    print 'Probability = ', sampleQuizzes()