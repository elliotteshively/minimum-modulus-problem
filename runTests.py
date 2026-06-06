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
def runM(m,maxModuliBound,printB):
    if printB:
        print()
        print("-------------------------------------------------------------------------------------------------------------")
        print()
        print("Running checks on m =",m)
    pathString = str(m) + "."
    moduli = list(range(m,m*maxModuliBound+1))

    pathString += "7f"
    moduli = cor7(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.8f"
    moduli = cor8(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.9f"
    moduli = cor9(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.7s"
    moduli = cor7(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.8s"
    moduli = cor8(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pathString += "F.9s"
    moduli = cor9(moduli,True)
    if recipricalSum(moduli) < 1:
        if printB:
            print("Reciprical sum of moduli is",recipricalSum(moduli))
        return pathString + "T"
    
    pList = allPrimeFactors(moduli)
    for p in pList[::-1]:
        pathString += "F.10GDwp" + str(p)
        if lemma10PlaceP(moduli,p,True):
            return pathString + "T"
        pathString += "F.10CBPwfp" + str(p) + lemma10CBPString(moduli,p,True)
        if pathString[-1] == 'T':
            return pathString
    return pathString

#returns list of strings
#arguments: int list indexList (all indices to check), bool printB (should we print the process to console)
#calls runM for each m in indexList
#returns list of all results strings       
def runChecklist(indexList,maxModuliBound,printB):
    results = []
    for i in indexList:
        results.append(runM(i,maxModuliBound,printB))

    for r in results:
        print(r)
    return(results)

#returns void
#argument: string list stringList (output from runChecklist)
#parses strings assuming order of application of corollarys/lemmas used by runM
#prints counts of m's that needed each step
#prints m values that needed every step
def runStrings(stringList):
    sevenCount = 0
    eightCount= 0
    nineCount= 0
    sevenSecondCount = 0
    eightSecondCount= 0
    nineSecondCount= 0
    tenCount = 0
    CBPCount = 0
    falseCount = 0

    solvedBy789 = []
    notSolvedBy789 = []
    solvedBy10 = []
    solvedByCBP = []
    notSolved = []

    for s in stringList:
        if "7fT" in s: #if seven enough
            sevenCount += 1
            solvedBy789.append(s.split(".")[0])
        if "8fT" in s: #if needed 8, enough
            eightCount += 1
            solvedBy789.append(s.split(".")[0])
        if "9fT" in s: #if needed 9, enough
            nineCount += 1
            solvedBy789.append(s.split(".")[0])
        if "7sT" in s: #if seven enough
            sevenSecondCount += 1
            solvedBy789.append(s.split(".")[0])
        if "8sT" in s: #if needed 8, enough
            eightSecondCount += 1
            solvedBy789.append(s.split(".")[0])
        if "9sT" in s: #if needed 9, enough
            nineSecondCount += 1
            solvedBy789.append(s.split(".")[0])
        if "7sF.8sF.9sF" in s:
            notSolvedBy789.append(s.split(".")[0])
            if not ("CBP" in s):
                tenCount += 1
                solvedBy10.append(s.split(".")[0])
            elif s.endswith('T'):
                CBPCount += 1
                solvedByCBP.append(s.split(".")[0])
            else:
                falseCount += 1
                notSolved.append(s.split(".")[0])


    print(len(stringList),"m values ran for")
    print(sevenCount,"true after seven")
    print(eightCount,"true after eight")
    print(nineCount,"true after nine")
    print(sevenSecondCount,"true after seven second time")
    print(eightSecondCount,"true after eight second time")
    print(nineSecondCount,"true after nine second time")
    print(tenCount,"true after gen placement")
    print(CBPCount,"true after CBP")
    print(falseCount,"unsolved")
    print("These m vals needed lemma 10:",notSolvedBy789)
    print("These m vals needed lemma 10, solved by lemma 10 first app:",solvedBy10)
    print("These m vals needed CBP, solved by CBP (lemma 10 second app):",solvedByCBP)
    print("These not solved:",notSolved)
            



