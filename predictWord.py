import string
from heapq import nlargest
import operator

FILENAME = "messages.txt"

def contentsAsStringList(FILENAME):
    f = open(FILENAME,"r")
    contents = f.read()
    contentsList = contents.split()
    f.close()
    return contentsList

def nextWordProbabilities(word, FILENAME):
    f = open(FILENAME,"r")
    contents = f.read()
    contentsList = contents.split()
    totalInstances = 0
    nextWordInstances = {}
    for i in range(len(contentsList)):
        if contentsList[i].lower() == word.lower():
            totalInstances += 1
            if (contentsList[i+1].lower() not in nextWordInstances):
                nextWordInstances[contentsList[i+1].lower()] = 1
            else:
                nextWordInstances[contentsList[i+1].lower()] += 1
    f.close()
    probabilities = {}
    print("Total instances of " + word + ": " + str(totalInstances))
    for entry in nextWordInstances:
        probabilities[entry] = nextWordInstances[entry] * (100.0 / totalInstances)
    sortedProbabilities = sorted(probabilities.items(), key=operator.itemgetter(1))
    return sortedProbabilities

def getNextWord(word, FILENAME):
    sortedProbs = nextWordProbabilities(word, FILENAME)
    return sortedProbs[-1][0]

q=False

while(q == False):
    word = input("Enter a word: ")
    word = word.lower()
    probs = nextWordProbabilities(word, FILENAME)
    length = len(probs)
    print("* " + word + " {} [{} %]".format(probs[-1][0], round(probs[-1][1],2)))
    runnersUp = min([length+1,7]) 
    print("Runners up:")
    for i in range(length-2, length-runnersUp,-1):
        print(word + " {} [{} %]".format(probs[i][0], round(probs[i][1],2)))
    want2quit = input("Again? [y/n]: ")
    if (want2quit == "n"):
        q=True
        
    


