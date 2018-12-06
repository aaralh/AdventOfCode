def readFile(fileName: str) -> str:
    '''
    Return contents of file with given name.

    Arguments:
    fileName -- Name of the file.
    '''
    with open(fileName, 'r', newline='') as inputFile:
        return inputFile.read()