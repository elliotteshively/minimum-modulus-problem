
import math
from math import gcd
import sympy
from sympy import factorint
import bisect
from utilityMMP import *
from inititalSumsMMP import sums 

#in all functions, returns TRUE if contradiction is arrived at, FALSE if otherwise

#FOR USE IN LEMMA TEN
#B tracks the sum of each bin
#Bi tracks the indices i in B for which B[i]
#R tracks the integers left to place into coverings
#rMass tracks the reciprical mass of R
#nMass tracks the needed mass of R

#returns list B, list Bi, list R, float rMass, float nMass
#arguments: int list moduli, int p, boolean printB
#from moduli, p find M0, M1, then initializes:
#B = all indices initialized to reciprocal sum of M0
#Bi = contains all indices of B
#R = {m/p for m in M1}
#rMass = reciprocal sum of M1
#nMass = p times (1-B[0])
def lemma10Setup(moduli,p,printB):
    if printB:
        print()
        print("Setting up LEMMA TEN with prime",p,"and",len(moduli), "moduli from", min(moduli),"to",max(moduli))
        print(moduli)
    M0 = [m for m in moduli if m % p != 0]
    R = [(m//p) for m in moduli if m % p == 0]
    S  = recipricalSum(M0)
    
    B = [S for _ in range(p)]
    Bi = [i for i in range(p)]
    rMass = recipricalSum(R)
    nMass = (1-S)*p
    if S > 1:
        if printB:
            print("Bin sum is greater than 1, CBP needed")
    else:
        if printB:
            print(len(R),"left to be placed:",R)
            print("There are",len(Bi),"bins less than 1")
            print("Each bin needs",1-S)
            print("Reciprical mass:",rMass)
            print("Needed mass",nMass)
    return B,Bi,R,rMass,nMass

#returns bool
#arguments: int list Bi, int list R, bool printB
#returns true if more bins are less than 1, than elements left to place
def checkA(Bi,R,printB): 
    if len(Bi) <= len(R): #if there are equal or more to place
        return False
    if printB: #if there are less to place than bins
        print("We have",len(Bi),"bins less than one, only",len(R),"left to place")
    return True

#returns bool
#arguments: float rMass, float nMass, bool printB
#returns true if there is more needed mass than possible mass
def checkB(rMass,nMass,printB):
    if nMass <= rMass: #if there are equal or more mass to place
        return False
    if printB: #if there is less mass then needed
        print("Need",nMass,"recip mass, have only",rMass)
    return True

#returns bool
#arguments: float list B, int list Bi, int list R, bool printB
#returns true if there are more bins that need at least two elements to be placed (times 2) than there are elements to be placed 
def checkC(B,Bi,R,printB):
    max = 0
    for i in Bi:
        if B[i] > max:
            max = B[i]
    if max < 1/R[0]: #if each remaning bin needs two items
        if len(Bi)*2 > len(R): #if there is more needed items than items to place
            if printB:
                print("There are",len(Bi),"bins that need 2 elements, only",len(R),"left to place")
            return True
    return False

#returns bool
#arguments: list B, list Bi, list R, float rMass, float nMass, bool printB
#with input values, checks for contradictions with checkA,B,C
#returns true if contradiction
def runABC(B,Bi,R,rMass,nMass,printB):
    if printB:
        print("Running ABC checks with indexes",Bi,"less than 1")
        print("And recipricals of",R,"left to place")
    if (checkA(Bi,R,printB)):
        return True
    if (checkB(rMass,nMass,printB)):
        return True
    if (checkC(B,Bi,R,printB)):
        return True
    return False

#returns list B, list Bi, list R, float rMass, float nMass
#arguments: list B, list Bi, list R, float rMass, float nMass, int i, bool printB
#"places" R[0] in B[i] bin, updates all values accordingly
def place(B,Bi,R,rMass,nMass,i,printB):
    Bval = B[i] #keeps track of og bin value
    rMass -= 1/R[0] #subtracts from rMass left
    B[i] += 1/R[0] #adds 1/R[0] to indexed bin
    if B[i] > 1:
        nMass -= (1-Bval) #if the bin goes over, only remove from nMass 1-S
        Bi.remove(i)
    else:
        nMass -= 1/R[0] #if the bin is under, remove 1/R[0] from nMass
    if printB:
        print("Added ",1/R[0]," to bin ",i,", rMass now equals ",rMass,", nMass now equals ",nMass,", there are ",len(Bi)," bins less than 1",sep='')
    del R[0]
    return B,Bi,R,rMass,nMass

#returns string
#arguments: int list moduli, int p, bool printB
#used if placeP does not result in a contradiction
#uses the critical bin procedure, which assumes certain conditions like placing first p values from R
#this procedure garuntees that if a contradiction is derived when applying lemma 10 a second time (with p coprime to certain values), the contradiction represents a contradiction in all possible distributions of elements R in p bins
#returns strings for use in runM
def lemma10CBPString(moduli,p,printB):
    if printB:
        print("Running LEMMA TEN CBP with prime",p,"and",len(moduli),"moduli from",min(moduli),"to",max(moduli))
    opString =""

    M0 = [m for m in moduli if m % p != 0]
    M1 = [m for m in moduli if m % p == 0]
    M1.sort()
    R = [(m//p) for m in M1]
    S = recipricalSum(M0)
    buckets = [S for _ in range(p) ]
    coverings = [M0[:] for _ in range(p)]

    placed = []
    for i in range(p):
        buckets[i] = buckets[i] + 1/R[i]
        bisect.insort(coverings[i], R[i])
        placed.append(R[i])
    placed_copy = placed[:]
    R = [m for m in R if not (m in placed_copy and placed_copy.remove(m) is None)]
    l = len(R)
    critIndex = p-l-1
    if critIndex >= 0:
        coPrimes = getCoprime(placed[critIndex:])
        if printB:
            print("Placed first",p,"elements into",p,"bins")
            print("There are",l,"left to be placed")
            print("Placed in critical bin to B_p are:",placed[critIndex:])
            print("Primes coprime to these values are:",coPrimes)
        for c in coPrimes[::-1]:
            if c !=p:
                if printB:
                    print("Running Lemma 10 on Bin",critIndex,"with",str(c))
                opString += "wsp" + str(c)
                if lemma10PlaceP(coverings[critIndex],c,True):
                    return opString + "T"
                else:
                    opString += "F"
        return opString
    else:
        if printB:
            print("ERROR: There are",p,"bins and",l,"left to place. Choose better prime")
        return opString + "p>ltpF"
    
#returns bool
#arguments: int list moduli, int p, bool printB
#places first p elements of R into bins, element by element, checking A,B,C after each placement
#returns true once a contradiction is derived
#returns false if no contradiction can be derived by placing first p elements of R into seperate bins
def lemma10PlaceP(moduli,p,printB):
    B,Bi,R,rMass,nMass = lemma10Setup(moduli,p,printB)
    if B[0] < 1:
        if len(R) < 1:
            print("There are no items to be placed. Choose different prime")
            return False
        for i in range(p):
            B,Bi,R,rMass,nMass = place(B,Bi,R,rMass,nMass,i,printB)
            if runABC(B,Bi,R,rMass,nMass,True):
                return True
        if printB:
            print("With generic distribution, more work is still needed. There are",len(R),"left to place")
    return False
