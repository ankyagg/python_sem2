import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023']
CSE = [50, 60, 65, 70]
IT = [20, 25, 30, 35]
EXTC = [15, 20, 25, 30]
AIDS = [10, 15, 20, 25]

x = np.arange(len(years))
bar_width = 0.2

plt.bar(x-1.5*bar_width,CSE,bar_width,label="CSE")
plt.bar(x-0.5*bar_width,IT,bar_width,label="IT")
plt.bar(x+0.5*bar_width,EXTC,bar_width,label="EXTC")
plt.bar(x+1.5*bar_width,AIDS,bar_width,label="AIDS")

plt.xlabel("years")
plt.ylabel("Placement")
plt.title("Placement 2020-23")
plt.xticks(x,years)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
