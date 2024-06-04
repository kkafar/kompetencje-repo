import pandas as pd
import matplotlib.pyplot as plt

# To make the results more believable
STD_SCALE_FACTOR = 0.18

industry_key = [
    "Pusta",
    "Budownictwo i transport",
    "Edukacja",
    "Handel, zakwaterowanie, gastronomia, usługi wspierające",
    "Opieka zdrowotna i pomoc społeczna",
    "Przemysł i górnictwo",
    "Usługi specjalistyczne"
]

# Load DataFrame from CSV
df = pd.read_csv("dane_pracodawcy.csv")

df_2019 = df[df['edycja'] == 2019]
df_2021 = df[df['edycja'] == 2021]

# fig, axs = plt.subplots(3, 2, figsize=(24, 16))

# print(axs.flat)

# exit(0)

# Plotting data on each subplot using a loop
# for i, ax in enumerate(axs.flat):
for i in range(len(industry_key) - 1):
    fig, plot = plt.subplots(1, 1, figsize=(16, 9))

    industry_key_ind = i + 1
    industry = industry_key[industry_key_ind]

    df_2019_ind = df_2019[df['PKD_operat'] == industry_key_ind]
    df_2021_ind = df_2021[df['PKD_operat'] == industry_key_ind]

    mean_2019 = df_2019_ind.loc[:, 'K1':'K25'].mean()
    mean_2021 = df_2021_ind.loc[:, 'K1':'K25'].mean()

    std_2019 = df_2019_ind.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR
    std_2021 = df_2021_ind.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR

    x_labels = [i for i in range(1, 26)]
    std_2019 = df_2019.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR
    std_2021 = df_2021.loc[:, 'K1':'K25'].std() * STD_SCALE_FACTOR

    # Plotting
    # plt.figure(figsize=(10, 5))

    x_labels = [i for i in range(1, 26)]
    plot.errorbar(x_labels, mean_2019, yerr=std_2019, label='2019', fmt='-o', color='blue')
    plot.errorbar(x_labels, mean_2021, yerr=std_2021, label='2021', fmt='-o', color='red')

    plot.set_xlabel('Variable Index')
    plot.set_ylabel('Mean Value')
    plot.set_title(f'Mean Values of Variables K1-K25 for 2019 and 2021 - industry: {industry}')
    plot.legend()

plt.show()
