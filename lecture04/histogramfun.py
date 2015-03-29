import pylab

# You may have to change this path
WORDLIST_FILENAME = "C:\\Users\\sadhikar\\Documents\\workspacepython\\ThinkModels\\inputs\\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # words: list of strings
    words = []
    for line in inFile:
        words.append(line.strip().lower())
    print "  ", len(words), "words loaded."
    return words

def plotVowelProportionHistogram(words, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in words
    using the specified number of bins in numBins
    """
    # This function was what I had o write
    vowels = ['a', 'e', 'i', 'o', 'u'] # The input words are all converted to lower case.
    ratios = [(sum(word.count(v) for v in vowels)/float(len(word))) for word in words] 
    pylab.hist(ratios, bins=numBins)
    pylab.title('Ratio of vowels to total characters in a word')
    pylab.xlabel('Bin')
    pylab.ylabel('Num vaues in bin')
    pylab.show()

if __name__ == '__main__':
    wordsList = loadWords()
    plotVowelProportionHistogram(wordsList, 10)
