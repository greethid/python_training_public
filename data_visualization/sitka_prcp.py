import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Getting dates and prcp values from the file
    dates, prcp_list = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcp_list.append(prcp)

    print(prcp_list)

# Chart data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp_list, c='blue', alpha=0.5)

# Chart formatting
ax.set_title("The PRCP values for Sitka - year 2018", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("PRCP", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()