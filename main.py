from runTests import *
from inititalSumsMMP import sums

initialSums = sums(11,True) #makes condensing possible 
jumpValues = initialSums.condense(616000,[],None) #condenses, returns jump values (if want to manually check)
needsCorollarysMax = min(jumpValues) #sets the value for which above, all values have reciprical sum less than 1
needsCorollarysList = list(range(2,needsCorollarysMax)) #checks all m values, by checking from 2 up, some low m's will result in "not solved", but are easily solved by hand (for MMB=11, Klein proved up to m=10)

checkListOutput = runChecklist(needsCorollarysList,11,True) #runs corollarys and lemmas with runM corollary/lemma order
runStrings(checkListOutput) #prints counts and m values that needed each step   
