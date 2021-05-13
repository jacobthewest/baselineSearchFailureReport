import numpy as np
from sklearn.linear_model import LinearRegression
import csv
MODEL_DATA = 'TrafficVolume.csv'

dic = {}
for i in range(24):
    dic[str(i)] = (0,0) # First 0 is sum, second 0 is the numbers making that sum.

with open(MODEL_DATA, newline='\n') as csvfile:
    reader = csv.reader(csvfile)
    skipHeader = True
    for row in reader:
        if skipHeader:
            skipHeader = False
        elif row[0] != '10/5/2019' and row[0] != '10/6/2019' and row[0] != '10/19/2019':  # Days in question
                                    # Don't collect data from the 5th, 6th, or 19th.
            key = row[1]
            value = int(row[2])
            tupleFromDic = dic[key]
            updatedSum = tupleFromDic[0] + value
            updatedCount = tupleFromDic[1] + 1
            dic[key] = (updatedSum, updatedCount)

with open("average.txt", "w") as file:
    for i in range(24):
        obtainedTuple = dic[str(i)]
        average = obtainedTuple[0] / obtainedTuple[1]
        file.write(str(i) + " = " + str(average) + "\n")