import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    mins = []
    delta = []
    for row in reader:
        min = int(row[6])
        mins.append(min)
        high = int(row[5])
        highs.append(high)

        delta.append(high - min)

    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.plot(mins, c='blue')
plt.plot(delta, c='black')

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()