import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2020', '2021', '2022', '2023']
CSE = [50, 60, 65, 70]
IT = [20, 25, 30, 35]
EXTC = [15, 20, 25, 30]
AIDS = [10, 15, 20, 25]

# Number of bars
bar_width = 0.2
x = np.arange(len(years))

# Plotting
plt.bar(x, CSE, width=bar_width, label='CSE')
plt.bar(x + bar_width, IT, width=bar_width, label='IT')
plt.bar(x + 2 * bar_width, EXTC, width=bar_width, label='EXTC')
plt.bar(x + 3 * bar_width, AIDS, width=bar_width, label='AIDS')


# Labeling
plt.xlabel('Year')
plt.ylabel('Number of Placements')
plt.title('Placement Data by Department')
plt.xticks(x+1.5*bar_width, years)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
