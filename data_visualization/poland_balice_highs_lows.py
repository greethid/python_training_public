import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/poland_weather_2013_2023.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Getting dates and maximum values from the file
    dates, highs, lows = [], [], []
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    for row in reader:
        if row[name_index] == 'BALICE, PL':
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = float(row[high_index])
                low = float(row[low_index])
            except ValueError:
                print(f'No data for date {current_date}.')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    print(highs)

# Chart data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Chart formatting
title = "The highest and the lowest temperatures of the day for Poland Kraków-Balice - years 2013-2023"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C°)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

# Scale
# ax.axis('square')
# ax.set_ylim([0, 150])

plt.show()