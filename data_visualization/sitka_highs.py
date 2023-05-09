import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Getting maximum values from the file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    print(highs)

# Chart data
plt.style.use('default')
fix, ax = plt.subplots()
ax.plot(highs, c='red')

# Chart formatting
ax.set_title("The highest temperature of the day, july 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F°)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()