#!/usr/bin/python
import os
import sys

#Take the input infile and read the integers into a 
#list and then return the list
def ReadIntFile(infile):
    
    outlist = []
    f = open(infile)
    length = 0
    
    for line in f.readlines():
        if line.strip() != "":
            outlist.append( int(line.strip()) )
            length += 1
        
    return outlist, length
    
#This program will do a level of recrusion on the input array
def Count(Array, length):
    if length == 1:
        return Array, 0
    else:
        B, x = Count(Array[0:length/2], length/2)
        C, y = Count(Array[length/2:length], length-length/2)
        D, z = CountSplitInv(B, length/2, C, length-length/2)
        return D, x+y+z
        
#This is the merge and Count Step
def CountSplitInv(Barray, Blength, Carray, Clength):
    
    outarray = []
    count = 0
    
    i=0;
    j=0;
    
    for k in range(0, Blength+Clength):
        
        if i == Blength:
            outarray.append(Carray[j])
            j += 1
        elif j == Clength:
            outarray.append(Barray[i])
            i += 1
        elif Barray[i] < Carray[j]:
            outarray.append(Barray[i])
            i += 1
        elif Carray[j] < Barray[i]:
            outarray.append(Carray[j])
            count += (Blength-i)
            j += 1
            
    return outarray, count
            

def main(argv):
    
    infile = argv[1]
    values, valLength = ReadIntFile(infile)
    sortedVal, invCount = Count(values, valLength)
    

    print("Total of %s Inversions" % invCount)
    
    
if __name__ == "__main__":
        main(sys.argv)