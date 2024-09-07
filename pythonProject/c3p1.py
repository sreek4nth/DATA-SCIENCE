import matplotlib.pyplot as plt
# Data
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]
# Create a new figure
plt.figure(figsize=(10, 6))
# Create a subplot with the specified properties
plt.subplot(111) # Only one subplot in this example
plt.plot(years, car_values, linestyle='-.', color='red', marker='*',
markersize=20, markerfacecolor='green')
plt.title("Sreekanth pradeep \nMCA 2023-2025", loc="right")
plt.title("Value Depreciation", loc="left")
plt.xlabel("Year")
plt.ylabel("Car Value")
# Show the plot
plt.show()