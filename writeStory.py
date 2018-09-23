import string
import random
import operator

FILENAME = "messages.txt"
NUM_WORDS = 500

def contentsAsStringList(FILENAME):
    f = open(FILENAME,"r", encoding = "utf-8")
    contents = f.read()
    contentsList = contents.split()
    f.close()
    return contentsList

def nextWordProbabilities(word, FILENAME):
    f = open(FILENAME,"r", encoding = "utf-8")
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
    #print("Total instances of " + word + ": " + str(totalInstances))
    for entry in nextWordInstances:
        probabilities[entry] = nextWordInstances[entry] * (100.0 / totalInstances)
    sortedProbabilities = sorted(probabilities.items(), key=operator.itemgetter(1))
    return sortedProbabilities

def getNextWord(word, FILENAME):
    sortedProbs = nextWordProbabilities(word, FILENAME)
    return sortedProbs[-1][0]

contents = contentsAsStringList
startingWord = input("Enter starting word: ")
word = startingWord
story = ""
k = 0
while(True):
    if (k == NUM_WORDS):
        break
    story += word
    story += " "
    if not nextWordProbabilities(word, FILENAME):
        word = random.choice(contents)
    else:
        word = getNextWord(word, FILENAME)
    k += 1

print(story)
