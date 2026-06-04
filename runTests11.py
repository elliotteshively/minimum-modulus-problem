# -*- coding: utf-8 -*-
from utilityMMP import *
from inititalSumsMMP import *
from corollarys import *
from lemmaTen import *

maxModuliBound = 11
          
#returns string
#arguments: int m (minimum modulus), bool printB (should we print the process to console)
#first generates moduli from m to maxModuliBound*11
#runs corollary 7 once, then corolalry 8 once, then corollary 9 once, then lemma 10 general placement with p the max prime factor of moduli, then lemma 10 cbp with p the max prime factor of moduli. This suffices for maxModuliBound = 11
#returns string of form m.TPB where T is the test code (i.e. 7 for corollary 7, 10CBP for lemma 10 critical bin procedure), P is "wpq" (with prime q), q the prime used for that test (if needed), and b is either "T" or "F"
def runM(m,printB):
    if printB:
        print()
        print("Running checks on m =",m)
    pathString = str(m) + "."
    moduli = list(range(m,m*maxModuliBound+1))

    pathString += "7"
    moduli = cor7(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.8"
    moduli = cor8(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.9"
    moduli = cor9(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    p = maxPrimeFactor(moduli)
    pathString += "F.10GDwp" + str(p)
    if lemma10PlaceP(moduli,p,True):
        return pathString + "T"
    
    pathString += "F.10CBPwfp" + str(p) + lemma10CBPString(moduli,p,True)
    return pathString

#returns list of strings
#arguments: int list indexList (all indices to check), bool printB (should we print the process to console)
#calls runM for each m in indexList
#returns list of all results strings       
def runChecklist(indexList,printB):
    results = []
    for i in indexList:
        results.append(runM(i,printB))

    for r in results:
        print(r)
    return(results)

#returns void
#argument: string list stringList (output from runChecklist)
#parses strings assuming order of application of corollarys/lemmas used by runM
#prints counts of m's that needed each step
#prints m values that needed every step
def runStrings(stringList):
    sevenT = 0
    eightT= 0
    nineT= 0
    tenT = 0
    CBPT = 0
    F = 0

    solvedBy789 = []
    notSolvedBy789 = []
    solvedBy10 = []
    solvedByCBP = []
    notSolved = []


    #19.7F.8F.9F.10GDwp13F.10CBPwfp13wspwsp13T    

    for s in stringList:
        if "7T" in s: #if seven enough
            sevenT += 1
            solvedBy789.append(s.split(".")[0])
        if "8T" in s: #if needed 8, enough
            eightT += 1
            solvedBy789.append(s.split(".")[0])
        if "9T" in s: #if needed 9, enough
            nineT += 1
            solvedBy789.append(s.split(".")[0])
        if "7F.8F.9F" in s:
            notSolvedBy789.append(s.split(".")[0])
            if not ("CBP" in s):
                tenT += 1
                solvedBy10.append(s.split(".")[0])
            elif s[-1] == 'T':
                CBPT += 1
                solvedByCBP.append(s.split(".")[0])
            else:
                F += 1
                notSolved.append(s.split(".")[0])



    print(sevenT,"true after seven")
    print(eightT,"true after eight")
    print(nineT,"true after nine")
    print(tenT,"true after gen placement")
    print(CBPT,"true after CBP")
    print(F,"unsolved")
    print("These needed lemma 10:",notSolvedBy789)
    print("These needed 10, solved:",solvedBy10)
    print("These need CBP, solved:",solvedByCBP)
    print("These not solved by 7,8,9, CBP:",notSolved)
            



