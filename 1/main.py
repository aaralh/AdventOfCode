from typing import List


def readFile(fileName: str) -> str:
    '''
    Return contents of file with given name.

    Arguments:
    fileName -- Name of the file.
    '''
    with open(fileName, 'r', newline='') as inputFile:
        return inputFile.read()


def calculateCurrentFrequency(frequencyList: List[int], currentFrequency: int) -> int:
    '''
    Return frequency after applying all changes in frequencyList.

    Arguments:
    frequencyList -- Frequency list which will be looped through.
    '''
    for value in frequencyList:
        currentFrequency = currentFrequency + int(value)

    return currentFrequency


def calculateFrequencySeenTwice(frequencyList: List[int]) -> int:
    '''
    Loops through frequencyList first twice seen frequency is found and returns it.

    Arguments:
    frequencyList -- Frequency list which will be looped through.
    '''
    currentFreq = 0
    seenFrequencys = {currentFreq} # Using set to gain some speed benefit.
    frequencySeenTwice = None
    while frequencySeenTwice == None:
        for frequency in frequencyList:
            currentFreq = currentFreq + int(frequency)
            if currentFreq in seenFrequencys:
                frequencySeenTwice = currentFreq
                break
            else:
                seenFrequencys.add(currentFreq)

    return frequencySeenTwice


lines = readFile("input.txt").splitlines()
frequencyList = [int(line) for line in lines]
