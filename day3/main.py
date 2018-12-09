import sys

# Hacky way to allow importing module beyond top-level package.
sys.path.append("..")
from utils import readFile
from typing import List


def reserveAreaForClaim(fabric: List[List[List[int]]], claim: tuple) -> List[List[List[int]]]:
    '''
    Adds claim id to all positions covered by the claim.

    Arguments:
    fabric -- Fabric where to add claims.
    claim -- Claim which to be added to fabric.
    '''
    claimId, claimPosition, claimArea = claim
    for x in range(int(claimPosition[0]), int(claimPosition[0]) + int(claimArea[0])):
        for y in range(int(claimPosition[1]), int(claimPosition[1]) + int(claimArea[1])):
            fabric[x][y].append(int(claimId))
    return fabric


def parseClaim(claim: str) -> tuple:
    '''
    Returns claim id, claim position and claim area in tuple format.

    Arguments:
    claim -- claim to be parsed.
    '''
    claimId = claim.split("@")[0].replace("#", "")
    claimPosition = claim.split("@")[1].split(":")[0].split(",")
    claimArea = claim.split(":")[1].split("x")
    return (claimId, claimPosition, claimArea)


def calculateAmountOfOverlappingClaims(fabric: List[List[List[int]]]) -> int:
    '''
    Returns total area which is claimed atleast by two different claims.

    Arguments:
    fabric -- Fabric which claims are calculated.
    '''
    area = 0
    for row in range(len(fabric)):
        for col in range(len(fabric[row])):
            if(len(fabric[row][col]) >= 2):
                area += 1
    return area


def getClaimsWithoutOverlap(fabric: List[List[List[int]]]) -> List[int]:
    '''
    Returns claim id's without overlap with another claim.

    Arguments:
    fabric -- Fabric which contains all claims.
    '''
    claimsWithoutOverlap = []
    claimsWithOverlap = []
    # Slow solution since time complexity is n².
    for row in range(len(fabric)):
        for col in range(len(fabric[row])):
            cell = fabric[row][col]
            if(len(cell) == 1 and cell[0] not in claimsWithOverlap and cell[0] not in claimsWithoutOverlap):
                claimsWithoutOverlap.append(cell[0])
            elif(len(cell) >= 2):
                for claimId in cell:
                    if claimId in claimsWithoutOverlap:
                        claimsWithoutOverlap.remove(claimId)
                    if claimId not in claimsWithOverlap:
                        claimsWithOverlap.append(claimId)
            print(f"{row}:{col}") # For 'logging' purposes since function takes while to run.

    return claimsWithoutOverlap

lines = readFile("input.txt").splitlines()
fabric = [[[] for _ in range(1000)] for _ in range(1000)]

for line in lines:
    claim = parseClaim(line)
    fabric = reserveAreaForClaim(fabric, claim)

area = calculateAmountOfOverlappingClaims(fabric)
print(area)
claimsWithoutOverlap = getClaimsWithoutOverlap(fabric)
print(claimsWithoutOverlap)
