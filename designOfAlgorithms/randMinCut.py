import sys
import random
import math

def readUVData(inFile):

    f = open(inFile, 'r')
    u = []
    v = []

    for line in f.readlines():
        splitLine = line.strip().split()

        currentUVal = splitLine[0]
        for item in splitLine:

            #Only look at items with v > u (if it's equal its a 
            #self loop, if it's smaller, it was included in a previous
            #entry). Actually I think we need to keep reversals, so keep them for now.
            if (item > currentUVal):
                u.append(currentUVal)
                v.append(item)

    return u,v

def JoinAndClean(u,v):

    #This routine will choose a random u-v element, join them, 
    #remove self loops, and return a new uNew and vNew

    uNew = []
    vNew = []

    randomId = random.randint(0, len(u)-1)
    uRand = u[randomId]
    vRand = v[randomId]

    seen = []

    def idfun(x): return x

    for ii in range(0, len(u)):
        if u[ii] != vRand and v[ii] != vRand:
            uNew.append(u[ii])
            vNew.append(v[ii])


            if u[ii] not in seen: 
                seen.append(u[ii])
            if v[ii] not in seen:
                seen.append(v[ii])


        elif (v[ii] == vRand and u[ii] != uRand):
            #I'm choosing to make v turn into u. So things linked
            #to u should remain unchanged.   Things linked to v will
            #need to link to u.  
            uNew.append(u[ii])
            vNew.append(uRand)

            if u[ii] not in seen:
                seen.append(u[ii])
            if uRand not in seen:
                seen.append(uRand)

        elif (u[ii] == vRand and v[ii] != uRand):
            #This is the opposite (since order doesn't matter)
            uNew.append(uRand)
            vNew.append(v[ii])

            if v[ii] not in seen:
                seen.append(v[ii])
            if uRand not in seen:
                seen.append(uRand)



    return uNew, vNew, seen

def minCutSingle(u,v):

    #This will do one pass of min cut and return the number of connections
    nVertex = len(u)

    while (nVertex > 2):
        u,v, seen = JoinAndClean(u,v)
        nVertex = len(seen)
    return len(u)

def minCutSim(uorig, vorig):

    #This will call the series 
    n = len(uorig)
    nTrial = 1000

    minCuts = -1
    for ii in range(0, nTrial):
        cuts = minCutSingle(uorig, vorig)
        if ii == 0 or cuts < minCuts:
            minCuts = cuts
            print(minCuts)

    return minCuts

def main(argv):

    inFile = "minCutData.txt"
    u, v = readUVData(inFile)
    nminCut = minCutSim(u,v)
    print("Minimum number of connections found: %s" % nminCut)



if __name__ == "__main__":
    main(sys.argv)