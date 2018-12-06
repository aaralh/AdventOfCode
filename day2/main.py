import sys

# Hacky way to allow importing module beyond top-level package.
sys.path.append("..")
from utils import readFile

def getCharOccurTimes(string: str) -> dict:
    '''
    Loops the string through and return dict char:occuringTime pairs.

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




idsWithTwoRecurringChars = 0
idsWithThreeRecurringChars = 0
boxIds = readFile("input.txt").splitlines()
for boxId in boxIds:
    occuringTimes = getCharOccurTimes(boxId)
    values = occuringTimes.values()
    if 2 in values:
        idsWithTwoRecurringChars += 1

    if 3 in values:
        idsWithThreeRecurringChars += 1

print(idsWithThreeRecurringChars)
print(idsWithTwoRecurringChars)
print(idsWithThreeRecurringChars * idsWithTwoRecurringChars)