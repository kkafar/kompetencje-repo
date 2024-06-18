from scrapper import *
import matplotlib.pyplot as plt

data = {
    "2021": ScrapperBulldog2021().data,
    "2022": ScrapperBulldog2022().data,
    "2023": ScrapperBulldog2023().data,
}

experience_2021 = data['2021']['Earnings and experience']
experience_2022 = data['2022']['Earnings and experience']
experience_2023 = data['2023']['Earnings and experience']

# Get labels and values for experience data
labels_experience = list(experience_2022.keys())

# Create the bar chart
plt.figure(figsize=(10, 6))

# Experience bars with different colors for each year
bar_width = 0.1
index = range(len(labels_experience))  # Use range for x-axis positions

plt.bar([p - bar_width for p in index], experience_2021.values(), bar_width, label='2021')
plt.bar(index, experience_2022.values(), bar_width, label='2022')
plt.bar([p + bar_width for p in index], experience_2023.values(), bar_width, label='2023')

# Customize the plot
plt.xlabel('Experience Level')
plt.ylabel('Earnings (PLN)')
plt.xticks([p + bar_width / 2 for p in index], labels_experience)
plt.title('Earnings by Experience Level (2021-2023)')
plt.legend()

plt.show()
