# mmp-11
The code necessary to prove that for a minimum modulus m in range 3 to 616000, a covering must have maximum modulus greater than 11m

main.py shows a possible sequence that given m, the minimum modulus of a covering, the maximum modulus of the covering must be greater than 11m

this code works by supposing some m less than or equal to 616000, then generating moduli from m to maximumModulusBound x m
we use the fact that the moduli of a covering must have reciprocal sum greater than 1, so by showing for moduli m to MMB x m, the reciprical sum is less than 1, we know a covering cannot be possible with moduli

we first use T(m), and a(n) sums to limit the m values for which reciprocal sum can be greater than 1 (for the MMB=11 case, this gives us possible m values between 11 and 246)
then assuming we have the moduli of a covering, we alter our moduli in a way that if the original moduli produced a covering, then so would the altered moduli. then by showing the alterned moduli have reciprocal sum less than 1, we show the altered moduli cannot be a covering, and thus the original moduli could not be a covering. for this we use corollaries and lemmas from a paper by J.Dalton and O. Trifonov titled "Extreme Covering Systems" and published in 2022. we developed a procedure for applying Lemma 10 twice, which we call the critical bin procedure. 

this code is generalized and will produce results for any maxModuliBound greater than or equal to 11 (or lower, too), but will likely not be helpful in proving the max moduli bound for large bounds, as the sums, corollarys, and lemmas will not reduce the moduli sets enough
