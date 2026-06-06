import math
from math import gcd
from sympy import factorint

#returns int 
#argument: int list moduli
#returns greatest integer that divides the LCM of moduli
def maxPrimeFactor(moduli):
    L = math.lcm(*moduli)
    a = max(factorint(L).keys())
    return a

#returns int list
#argument: int list moduli
#returns list of each integer that divides the LCM of moduli sorted least to greatest
def allPrimeFactors(moduli):
    L = math.lcm(*moduli)
    return list(factorint(L).keys())

#return bool
#arguments int d
def is_prime(d): 
    return d > 1 and all(d % i != 0 for i in range(2, int(d**0.5) + 1))

#returns int list
#argument: int list integers
#returns list of primes that are both less than max(integers) and coprime with all ints in integers, sorted least to greatest
def getCoprime(integers):
    return [p for p in range(1, max(integers)) if is_prime(p) and all(gcd(p, n) == 1 for n in integers)]

#returns int list
#argument: int limit
#runs as precursor in initialSumsMMP
#returns list where index in list is n and value is the greatest prime factor of n
#list is indexed from 0 to limit
def buildGPF(limit):
    gpfList = list(range(limit+1))
    gpfList[0] = 0
    gpfList[1] = 1 
    for p in range(2,limit+1):
        if gpfList[p] == p:
            for x in range(p,limit+1,p):
                gpfList[x]=p            
    return gpfList

#returns float
#argument: int list list
#returns reciprical sum of list
def recipricalSum(list):
    sum = 0
    for x in list:
        sum+=1/x
    return sum
