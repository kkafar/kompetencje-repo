import matplotlib.pyplot as plt
import numpy as np

# Data
headers = ["Admin / DevOps", "IT Architect", "Product Owner", "Software Developer", "IT Analyst", "Tester / QA", "Other"]
data = [
    [9.9, 2.9, 6.9, 57.0, 5.9, 18.0, 0.6],  # Employment percentages for 2021
    [11.0, 2.6, 6.0, 57.0, 6.0, 15.0, 2.4],  # Employment percentages for 2022
    [10.0, 1.7, 6.0, 53.0, 5.0, 14.0, 10.3]  # Employment percentages for 2023
]

# Number of years
num_years = len(data)

# Width of each bar
bar_width = 0.15

# Set the positions of the bars on the x-axis
positions = np.arange(len(headers))

# Define custom colors
colors = [(0, 107/255, 56/255, 0.8), (0, 0, 0, 0.8), (177/255, 7/255, 35/255, 0.8)]

# Plotting each bar for each year with custom colors
fig, ax = plt.subplots()
for i in range(num_years):
    ax.bar(positions + i * bar_width, data[i], width=bar_width, label=f'{2021 + i}', color=colors[i],
           edgecolor='none')

# Adding labels, title, and legend
ax.set_ylabel('Percentage (%)')
ax.set_title('Employment Percentage in Job Roles by Year')

# Rotate x-axis tick labels
ax.set_xticks(positions + (num_years - 1) * bar_width / 2)
ax.set_xticklabels(headers, rotation=45)  # Adjust rotation angle as needed

ax.legend()

# Remove outer frame
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Show plot
plt.show()
