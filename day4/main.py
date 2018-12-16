from typing import List, Dict
import sys

# Hacky way to allow importing module beyond top-level package.
sys.path.append("..")
from utils import readFile


lines = readFile("fixedInput.txt")

def sortInputBasedOnTimestamp(alist):
    '''
    Sort given list based on timestamp.

    Arguments:
    alist -- list to be sorted.
    '''
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if int(alist[i].split("]")[0].split(" ")[1].split(":")[1])>int(alist[i+1].split("]")[0].split(" ")[1].split(":")[1]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            if int(alist[i].split("]")[0].split(" ")[1].split(":")[0])>int(alist[i+1].split("]")[0].split(" ")[1].split(":")[0]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            if int(alist[i].split("]")[0].split(" ")[0].split("-")[2])>int(alist[i+1].split("]")[0].split(" ")[0].split("-")[2]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            if int(alist[i].split("]")[0].split(" ")[0].split("-")[1])>int(alist[i+1].split("]")[0].split(" ")[0].split("-")[1]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                

def getBiggestSleeper(guards: Dict) -> List:
    '''
    Returns list with guardId and dict containing guards sleeping time.

    Arguments:
    guards -- Dictionary containing guards sleeping times.
    '''
    biggestSleeper = [0, [0]]
    for guardId in guards:
        if guards[guardId][0] > biggestSleeper[1][0]:
            biggestSleeper = [guardId, guards[guardId]]

    return biggestSleeper


def parseGuardsFromList(lines: List[str]) -> Dict:
    '''
    Returns dict containing guard infos parsed from lines.

    Arguments:
    lines -- Contains list of strings containing guard data.
    '''
    tmpGuard = {}
    guards = {}
    currentGuard = -1
    sleepTime = 0
    sleepStart = 0
    for line in lines:
        split = line.split(" ")
        if split[2] == "Guard":
            guardId = split[3].replace("#", "")
            guard = guards.get(currentGuard)
            if guard != None:
                guards[currentGuard][0] += sleepTime
            else:
                guards[currentGuard] = [sleepTime, tmpGuard]
            currentGuard = guardId
            tmpGuard = {}
            sleepTime = 0
        elif split[2] == "falls":
            sleepStart = int(split[1].split(":")[1].replace("]", ""))
        elif split[2] == "wakes":
            sleepEnd = int(split[1].split(":")[1].replace("]", ""))
            sleeping = sleepEnd - sleepStart
            sleepTime += sleeping
            guard = guards.get(currentGuard)
            if guard != None:
                for minute in range(sleepStart, sleepEnd):
                    value = guards[currentGuard][1].get(minute)
                    if value != None:
                        guards[currentGuard][1][minute] += 1
                    else:
                        guards[currentGuard][1][minute] = 1
            else:
                for minute in range(sleepStart, sleepEnd):
                    value = tmpGuard.get(minute)
                    if value != None:
                        tmpGuard[minute] += 1
                    else:
                        tmpGuard[minute] = 1
    return guards


lines = lines.splitlines()
guards = parseGuardsFromList(lines)


biggestSleeper = getBiggestSleeper(guards)
item = [0, 0]
for minute, amount in biggestSleeper[1][1].items():
    if amount > item[1]:
        item = [minute, amount]

print(item)
print(biggestSleeper[0])
print(int(biggestSleeper[0]) * item[0])