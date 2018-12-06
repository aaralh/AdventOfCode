
currentFrequency = 0

def readFile(fileName: str) -> str:
    with open(fileName, 'r', newline='') as inputFile:
        return inputFile.read()


frequencyValues = readFile("input.txt").splitlines()
for value in frequencyValues:
    currentFrequency = currentFrequency + int(value)

print(currentFrequency)