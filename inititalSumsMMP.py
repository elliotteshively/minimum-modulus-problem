import math
from utilityMMP import buildGPF
 
class sums:
    #returns void
    #arguments int maxModuliBound, bool printB
    #uses OOP as gpfList has large run time, only needs to be ran once (helpful if we condense twice)
    def __init__(self,maxModuliBound,printB):
        self.MMB = maxModuliBound
        self.gpfList = buildGPF(616000*self.MMB)
        self.printB = printB
    
    #returns float
    #argument: int m
    #using the bound sqrt((maxModuliBound-1)*m+1) 
    #returns reciprical sum of all values from m to maxModuliBound*m whose greatest prime factor is less than bound
    def T(self,m):
        sum = 0.0
        bound = math.sqrt((self.MMB-1)*m+1)
        for n in range(m,self.MMB*m+1):
            if self.gpfList[n] < bound:
                sum += 1/n
        return sum
    
    #returns int
    #argument: int m
    #returns the first n for which Tm + a_(m->n) > 1 (where a_(m->n) represents the sum of a_(k) for m>=k>=n)
    #a(n) returns 1/n if gpf(n) < sqrt(maxModuliBound*m+1)
    def runJumps(self,Tm,m):
        jumpSum = Tm
        while True:
            if jumpSum >= 1:
                return m + 1
            if self.gpfList[m] < math.sqrt((self.MMB-1)*m+1):
                jumpSum = jumpSum + 1/m 
            m -= 1

    #returns int list
    #arguments int m, int list mList, int set visited
    #returns list of skip values
    #called recursively 
    def condense(self,m,mList,visited):
        if visited is None:
            visited = set()
        if m in visited:
            if self.printB:
                print(f"Cycle detected at m={m}")
            return mList
        visited.add(m)
        
        tSum = self.T(m)
        n = self.runJumps(tSum,m)
        if self.printB:
            print(f"T({m}) = {tSum}")
        mList.append(n)   
        return self.condense(n,mList,visited)

    #returns array
    #argument: m (int)
    #return array: index is n and value is T(n)
    #has length of m+1
    def runT(self,m):
        recSumValues = [0]
        for x in list(range(1,m+1)):
            t = self.T(x)
            recSumValues.append(t)
            if self.printB:    
                print(str(t))
                print(str(x))
        return recSumValues