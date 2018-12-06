from typing import List
import sys

# Hacky way to allow importing module beyond top-level package.
sys.path.append("..")
from utils import readFile

def getCharOccurTimes(string: str) -> dict:
    '''
    Loops the string through and return dict char:occuringAmount pairs.

    Arguments:
    string -- String to loop through.
    '''
    chars = {}
    for char in boxId:
        value = chars.get(char)
        if value != None:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def getNumberOfRepeatedChars(strings: List[str]) -> tuple:
    '''
    Calculates rows that contains chars repeating 2 or 3 times.
    Returns amounts in tuple.
    Arguments:
    strings -- List of strings which is looped through.
    '''
    idsWithTwoRecurringChars = 0
    idsWithThreeRecurringChars = 0
    for boxId in boxIds:
        occuringTimes = getCharOccurTimes(boxId)
        values = occuringTimes.values()
        if 2 in values:
            idsWithTwoRecurringChars += 1

        if 3 in values:
            idsWithThreeRecurringChars += 1
    return (idsWithTwoRecurringChars, idsWithThreeRecurringChars)

def getMostSimilarStrings(strings: List[str]) -> tuple:
    '''
    Returns strings pair with max dissimilarity of one.

    Arguments:
    strings -- List of strings to loop through.
    '''
    for s1 in strings:
        for s2 in strings:
            if s1 == s2:
                continue
            dissimilarity = 0
            for i in range(len(s1)):
                if dissimilarity > 1:
                    break
                if(s1[i] != s2[i]):
                    dissimilarity += 1
            if dissimilarity == 1:
                return (s1, s2)

boxIds = readFile("input.txt").splitlines()
result = getMostSimilarStrings(boxIds)
print(result)