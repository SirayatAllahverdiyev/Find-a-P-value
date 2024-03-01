import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample P-values between the groups
p_values = np.array([[1.0, 0.831847, 0.702925, 0.815557, 0.768595, 0.024612],
                     [0.831847, 1.0, 0.419647, 0.572699, 0.025455, 0.926817],
                     [0.702925, 0.419647, 1.0, 0.918927, 0.766444, 0.865768],
                     [0.815557, 0.572699, 0.918927, 1.0, 0.046697, 0.8990617],
                     [0.768595, 0.025455, 0.766444, 0.046697, 1.0, 0.52544],
                     [0.024612, 0.926817, 0.865768, 0.8990617, 0.52544, 1.0]])

# Create a DataFrame from the P-values
columns = ['CEA', 'CA_19_9', 'Albumin', 'ALT', 'ALP', 'GGT']
p_values_df = pd.DataFrame(p_values, columns=columns, index=columns)

# Create a heatmap of the P-values
plt.figure(figsize=(10, 8))
sns.heatmap(p_values_df, annot=True, cmap='coolwarm', fmt=".3f", linewidths=.5)
plt.title('Correlation Plot based on P-values between CEA, CA_19_9, Albumin, ALT, ALP, and GGT groups')
plt.xlabel('Groups')
plt.ylabel('Groups')
plt.show()



