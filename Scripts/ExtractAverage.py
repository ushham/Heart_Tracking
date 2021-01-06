import pandas as pd
import matplotlib.pyplot as plt
from Scripts import DataExtract as ext

minave = 10    #number of mins to take rolling average over
secpmin = 60
rolltime = str(minave * secpmin) + 's'

#Extract data
loc = r'C:\Users\UKOGH001\Documents\05 Personal Projects\08 HeartCOV\MyFitbitData\UshHamilton\HeartData'
heartdata = ext.Extract(loc)

#Create rolling average
heartdata.sort_index()
roll = heartdata.rolling(rolltime, min_periods=10).mean()
heartdata['Average'] = roll['BPM']

#Create stats
stat = []
dates = []
for idx, day in heartdata.groupby(heartdata.index.date):
    print(idx)
    dates.append(idx)
    start_time, end_time = '01:00', '07:00'
    filttime = day.between_time(start_time, end_time)
    stats = filttime.describe()['Average']
    stat.append([idx, stats])

numdat = len(stat)
ave = [stat[d][1]['mean'] for d in range(numdat)]
upp = [stat[d][1]['75%'] for d in range(numdat)]
low = [stat[d][1]['25%'] for d in range(numdat)]
std = [stat[d][1]['std'] for d in range(numdat)]
rng = [upp[i] - low[i] for i in range(len(upp))]

fig, ax1 = plt.subplots()
ax1.plot(dates, ave, color='b')
ax2 = ax1.twinx()

ax2.plot(dates, rng, linestyle='dashed', color='r')
ax2.plot(dates, std, linestyle='dashed', color='g')

plt.show()




