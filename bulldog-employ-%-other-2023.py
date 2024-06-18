import matplotlib.pyplot as plt

# Data
labels = ['Data Science / ML / AI', 'UX / UI', 'Other Specialization']
sizes_outer = [2.9, 2.1, 5.7]  # Percentages for the outer ring
sizes_inner = [100]  # Just a single value for an empty inner ring

# Colors with alpha values
colors_outer = [(0, 107/255, 56/255, 0.8), (0, 0, 0, 0.8), (177/255, 7/255, 35/255, 0.8)]
colors_inner = ['white']  # Color for the inner circle (white)

# Plotting the outer pie chart
fig, ax = plt.subplots(figsize=(6, 6))
outer_pie, _ = ax.pie(sizes_outer, radius=1, labels=labels, colors=colors_outer,
                      startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'))

# Plotting the inner pie chart (empty)
inner_pie, _ = ax.pie(sizes_inner, radius=0.7, colors=colors_inner)

plt.title("Employment Percentage for 'Other' Job Roles in 2023")

# Equal aspect ratio ensures that pie is drawn as a circle
ax.set(aspect="equal")
plt.tight_layout()

# Show plot
plt.show()
