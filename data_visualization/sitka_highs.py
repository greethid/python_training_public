import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'


def get_city_name():
    index_1 = filename.index('data/')
    print(index_1)
    index_2 = filename.index('_weather')
    print(index_2)
    return filename[index_1+5:index_2].capitalize()


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Getting dates and maximum values from the file
    dates, highs, lows = [], [], []
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[high_index])
        low = int(row[low_index])
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
city = get_city_name()
title = "The highest and the lowest temperatures of the day for " + city + " - year 2018"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F°)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

# Scale
# ax.axis('square')
ax.set_ylim([0, 150])

plt.show()


