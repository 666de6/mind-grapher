# generate_chart.py

import matplotlib.pyplot as plt

# Read record list
with open('record_list.txt', 'r') as file:
    data = file.readlines()

dates = []
counts = []

# Parse data
for line in data:
    date, count = line.strip().split(': ')
    dates.append(date)
    counts.append(int(count))

# Generate chart
plt.figure(figsize=(10, 6))
plt.plot(dates, counts, marker='o')
plt.title('Mind Grapher')
plt.xlabel('Date')
plt.ylabel('Checked Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart as PNG file
plt.savefig('chart.png')
