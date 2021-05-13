import numpy as np
from sklearn.linear_model import LinearRegression
import csv
MODEL_DATA = 'TrafficVolume.csv'

x_data = []
y_data = []

with open(MODEL_DATA, newline='\n') as csvfile:
    reader = csv.reader(csvfile)
    skipHeader = True
    for row in reader:
        if skipHeader:
            skipHeader = False
        elif row[2] != '0':
            x_data.append(row[1])
            y_data.append(row[2])
        else:
            print(row)

x = np.array(x_data).reshape((-1,1))
y = np.array(y_data)

model = LinearRegression().fit(x, y)
print('coefficient of determination:', model.score(x, y))
print('intercept:', model.intercept_)
print('slope:', model.coef_)


predictionsInput = []
for i in range(15, 24):
    predictionsInput.append(i)

for i in range(15):
    predictionsInput.append(i)

predictionsInput = np.array(predictionsInput).reshape((-1,1))

predictionsOutput = model.predict(predictionsInput)

with open("linearRegressionPredictions.txt", "w") as file:
    for i in range(len(predictionsInput)):
        if(predictionsInput[i][0] < 15):
            file.write("10/6/2019 " + str(predictionsInput[i]) + ": " + str(predictionsOutput[i]) + "\n")
        else:
            file.write("10/5/2019 " + str(predictionsInput[i]) + ": " + str(predictionsOutput[i]) + "\n")
print('predicted response:', predictionsOutput, sep='\n')