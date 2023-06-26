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
    dates, avgs = [], []
    avg_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    for row in reader:
        if row[name_index] == 'BALICE, PL':
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                avg = float(row[avg_index])
            except ValueError:
                print(f'No data for date {current_date}.')
            else:
                dates.append(current_date)
                avgs.append(avg)

    print(avgs)

# Chart data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, avgs, c='red', alpha=0.5)

# Chart formatting
title = "The average temperatures of the day for Poland Kraków-Balice - years 2013-2023"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C°)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()