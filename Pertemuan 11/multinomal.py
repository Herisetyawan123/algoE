from scipy.stats import chi2


rata_rata, stdeviasi, stdeviasi_sampel, n = 60, 4, 6, 7

ragam = stdeviasi**2

df = n-1
kuadrat = (df*stdeviasi_sampel**2)/ragam
batas_bawah = chi2.cdf(kuadrat, df)
probility = 1 - batas_bawah
print('probilitas', probility)