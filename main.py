from runTests11 import *
from inititalSumsMMP import sums

initialSums = sums(11,True) #makes condensing possible 
jumpValues = initialSums.condense(616000,[],None) #condenses, returns jump values (if want to manually check)
needsCorollarysMax = min(jumpValues)-1 #sets the value for which above, all values have reciprical sum less than 1
needsCorollarysList = list(range(10,needsCorollarysMax)) #sets the list to check using corollarys and lemmas (Klein proved for m=7,8,9,10 for maxModuliBound=11)

checkListOutput = runChecklist(needsCorollarysList,True) #runs corollarys and lemmas with runM corollary/lemma order
runStrings(checkListOutput) #prints counts and m values that needed each step