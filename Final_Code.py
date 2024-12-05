import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The synthetic dataset for a week's worth of data
data = {
    "Time": ["10 AM - 11 AM", "11 AM - 12 PM", "12 PM - 1 PM", "1 PM - 2 PM", "2 PM - 3 PM", "3 PM - 4 PM", "4 PM - 5 PM"],
    "Monday": [8, 6, 25, 28, 10, 7, 5],
    "Tuesday": [6, 7, 27, 30, 9, 5, 4],
    "Wednesday": [7, 8, 26, 25, 11, 6, 6],
    "Thursday": [9, 6, 28, 29, 12, 8, 7],
    "Friday": [8, 5, 30, 27, 10, 7, 5],
    "Saturday": [0, 0, 0, 0, 0, 0, 0],
    "Sunday": [0, 0, 0, 0, 0, 0, 0]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Remove weekends from the DataFrame
df_weekdays = df.drop(columns=["Saturday", "Sunday"])

# Transposing the DataFrame for easier calculations
df_transposed = df_weekdays.set_index("Time").transpose()
daily_totals = df_transposed.sum(axis=1)

# Calculating average demand per hour for each day
daily_averages = daily_totals / len(df_transposed.columns)

# Calculating the weekly average demand per hour
weekly_average = daily_averages.mean()

# Calculating the standard deviation of daily totals
std_deviation = daily_totals.std()

# Display the results
print("Daily Totals:")
print(daily_totals)
print("\nWeekly Average Demand per Hour:", weekly_average)
print("Standard Deviation of Daily Totals:", std_deviation)

# Monte Carlo Simulation
num_simulations = 1000
simulated_totals = []

for _ in range(num_simulations):
    simulated_day = np.random.normal(weekly_average, std_deviation, len(df_weekdays.columns))
    simulated_totals.append(simulated_day.sum())

# Calculating percentiles
percentile_25 = np.percentile(simulated_totals, 25)
percentile_50 = np.percentile(simulated_totals, 50)
percentile_75 = np.percentile(simulated_totals, 75)
percentile_95 = np.percentile(simulated_totals, 95)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(simulated_totals, bins=30, edgecolor='black', alpha=0.7, color='skyblue')
plt.axvline(percentile_25, color='r', linestyle='dashed', linewidth=1.5, label='25th Percentile')
plt.axvline(percentile_50, color='g', linestyle='dashed', linewidth=1.5, label='50th Percentile (Median)')
plt.axvline(percentile_75, color='b', linestyle='dashed', linewidth=1.5, label='75th Percentile')
plt.axvline(percentile_95, color='purple', linestyle='dashed', linewidth=1.5, label='95th Percentile')

# Titles, labels, and legend
plt.title('Monte Carlo Simulation of Total Daily Demand', fontsize=16)
plt.xlabel('Total Meals Sold', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Descriptions
plt.text(percentile_25, 30, '25th Percentile', rotation=90, color='r', fontsize=10, va='bottom')
plt.text(percentile_50, 30, 'Median', rotation=90, color='g', fontsize=10, va='bottom')
plt.text(percentile_75, 30, '75th Percentile', rotation=90, color='b', fontsize=10, va='bottom')
plt.text(percentile_95, 30, '95th Percentile', rotation=90, color='purple', fontsize=10, va='bottom')

plt.show()
