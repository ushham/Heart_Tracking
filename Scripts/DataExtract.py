import json
import pandas as pd
import os

def Extract(folder):
    hold = []
    files = os.listdir(folder)
    for file in files:
        file = folder + "\\" + file
        filein = open(file)
        data = json.load(filein)
        for line in data:
            hold.append([line['dateTime'], line['value']['confidence'], line['value']['bpm']])

    heartdata = pd.DataFrame(hold, columns=['Time', 'Conf', 'BPM'])
    heartdata['Time'] = pd.to_datetime(heartdata['Time'], format='%m/%d/%y %H:%M:%S')
    heartdata = heartdata.set_index('Time', drop=False)
    return heartdata