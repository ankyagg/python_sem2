import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

data = pd.read_csv('cars.csv')

Age = data["Age"]
Price = data["Price"]
Kms_driven = data["Kms_Driven"]
Fuel_Type = data["Fuel_Type"]

#scatter
plt.scatter(Age,Price,color='blue')
plt.xlabel("Age of the car")
plt.ylabel("Price of the car")
plt.title("Age V/S Price")
plt.show()

#histogram
plt.hist(Kms_driven,bins=5,color='green')
plt.title("Distribution of Kms driven")
plt.xlabel("Kms Driven")
plt.ylabel("Frequency")
plt.show()

#bar
fuel_count = Counter(Fuel_Type)
plt.bar(fuel_count.keys(),fuel_count.values(),color='orange')
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#pie
plt.pie(fuel_count.values(),labels= fuel_count.keys(),startangle=90,colors=['blue','gold','silver'])
plt.title("Fuel Type Distribution")
