import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

STD_SCALE_FACTOR = 0.25


def remove_outliers_zscore(df, columns=['K{}'.format(i) for i in range(1, 26)], threshold=3):
    z_scores = np.abs((df[columns] - df[columns].mean()) / df[columns].std())
    df_cleaned = df[(z_scores < threshold).all(axis=1)]
    return df_cleaned


# Load DataFrame from CSV
df = pd.read_csv("dane.csv")
df_employer = pd.read_csv("dane_pracodawcy.csv")

# Filter DataFrame for 'edycja' values 2019 and 2021
df_2019 = remove_outliers_zscore(df[df['edycja'] == 2019])
df_2021 = remove_outliers_zscore(df[df['edycja'] == 2021])

df_employer_2019 = remove_outliers_zscore(df[df['edycja'] == 2019])
df_employer_2021 = remove_outliers_zscore(df[df['edycja'] == 2021])

print(len(df_2019), len(df_2021))

# Calculate mean for K1 to K25 for each edycja
mean_2019 = df_2019.loc[:, 'K1':'K25'].mean()
mean_2021 = df_2021.loc[:, 'K1':'K25'].mean()

mean_employer_2019 = df_employer_2019.loc[:, 'K1':'K25'].mean()
mean_employer_2021 = df_employer_2021.loc[:, 'K1':'K25'].mean()

std_2019 = df_2019.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR
std_2021 = df_2021.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR

std_employer_2019 = df_employer_2019.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR
std_employer_2021 = df_employer_2021.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR

# Plotting
plt.figure(figsize=(10, 5))

x_labels = [i for i in range(1, 26)]
plt.errorbar(x_labels, mean_2019, label='2019', fmt='-o', color='blue')
plt.errorbar(x_labels, mean_2021, yerr=std_2021, label='2021', fmt='-o', color='red')

plt.errorbar(x_labels, mean_employer_2019, label='e 2019', fmt='-o', color='yellow')
plt.errorbar(x_labels, mean_employer_2021, label='e 2021', fmt='-o', color='yellow')


plt.xlabel('Variable Index')
plt.ylabel('Mean Value')
plt.title('Mean Values of Variables K1-K25 for 2019 and 2021')
plt.legend()
plt.grid(True)

plt.show()
