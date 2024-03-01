import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Verileri DataFrame'e dönüştürme
data = {
    'CEA': [4.88, 4.35, 1000, 2.1, 2.1, 6.18, 512.7, 363.7, 2.1, 154.4, 2.1, 2.1, 2.1, 2.03, 2.1, 2.1, 0.97],
    'CA_19_9': [10.43, 46.3, 11.2, 1000, 40.79, 116.1, 11.2, 644.1, 11.2, 499.8, 11.2, 11.2, 11.2, 10.97, 1000, 3.97, 4.54],
    'Albumin': [4.2, 2.93, 4.2, 4.11, 4.13, 2.96, 4.38, 4.76, 4.98, 2.55, 3.74, 4.46, 4.71, 4.2, 3.65, 4.98, 4.2],
    'ALT': [41.15, 10.32, 25.0, 26.24, 43.73, 13.3, 28.8, 52.88, 24.73, 66.8, 10.92, 34.68, 15.14, 68.35, 23.6, 33.52, 19.96],
    'ALP': [141.08, 98.8, 98.8, 224.91, 175.02, 79.33, 130, 207.33, 98.8, 251.09, 57.88, 114.86, 99.86, 55.38, 98.8, 147.2, 98.8],
    'GGT': [35, 68.76, 173.1, 90.88, 132.86, 37.1, 37.1, 37.1, 37.1, 37.1, 37.1, 37.1, 37.1, 37.1, 37.1, 74.22, 12.11]
}

df = pd.DataFrame(data)

# P-değerleri için bir DataFrame oluşturma
p_values = pd.DataFrame(np.zeros((len(df.columns), len(df.columns))), columns=df.columns, index=df.columns)

# Her bir değişken çifti için p-değerlerini hesaplama
for i in range(len(df.columns)):
    for j in range(len(df.columns)):
        p_values.iloc[i, j] = pearsonr(df.iloc[:, i], df.iloc[:, j])[1]

# Detaylı p-değerlerini gösteren tabloyu yazdırma
print("Detaylı P-değerleri:")
print(p_values)
