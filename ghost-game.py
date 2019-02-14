
# This problem was asked by Two Sigma.

# Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, 
# or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

# Player 1: g
# Player 2: h
# Player 1: o
# Player 2: s
# Player 1: t [loses]
# Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

# For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.


dictionaryArray = ["cat", "calf", "dog", "bear"]
solutionList = []
firstLetterOccurences = {}



def getPossibleStartingLetters():
    for i in range(len(dictionaryArray)):
        wordFirstLetter = dictionaryArray[i][0]
        word = dictionaryArray[i]
        if wordFirstLetter not in firstLetterOccurences:
            firstLetterOccurences[wordFirstLetter] = [word]
        else:
            list = firstLetterOccurences[wordFirstLetter]
            list.append(word)

# returns true if all words have even size
def checkIfEveryWordIsEven(list):
    for i in range(len(list)):
        wordSize = len(list[i])
        if wordSize % 2 != 0:
            return False
    return True
        


def main():
    getPossibleStartingLetters()
    for key, value in firstLetterOccurences.iteritems():
        if checkIfEveryWordIsEven(value):
            solutionList.append(key)

    print "The solutions are: " + str(solutionList)

main()


