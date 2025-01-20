def findMin(i,j,k):
    if i < j and i < k:
        return i
    elif j < i and j < k:
        return j
    return k





structures=list(input())
noOfStructures=set(structures)
countT=structures.count("T")
countC=structures.count("G")
countG=structures.count("C")
extra=0
extraTimes=findMin(countT,countG,countC)
if len(noOfStructures) == 3:
    extra=7*extraTimes
scientificPoints = countT**2 + countC**2 + countG**2 + extra

print(scientificPoints)



    