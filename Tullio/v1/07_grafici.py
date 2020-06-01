import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from os.path import join

mainFilePath = '/home/tullio/Projects/fvab_dataset/2'
meanSensorsSitPath=join(mainFilePath,"MeanSensorsSit.csv")
meanSensorsWalkPath=join(mainFilePath,"MeanSensorsWalk.csv")

meanSensorsSit=pd.read_csv(meanSensorsSitPath).head(100)
meanSensorsWalk=pd.read_csv(meanSensorsWalkPath).head(100)
printLegend=True
fig, plots = plt.subplots(3,3)
for i in range(0,3):
    for j in range(0,3):
        col=(i*3)+j
        sitVal=meanSensorsSit.iloc[:,[(col+1)]]
        walkVal=meanSensorsWalk.iloc[:,[(col+1)]]
        name=sitVal.columns[0]
        p=plots[i,j]
        p.set_title(name)
        p.set_ylabel("Value")
        p.plot(sitVal, color="green", alpha=0.5, label="Sit")
        p.plot(walkVal, color="blue", alpha=0.5, label="Walk")
        if printLegend:
            p.legend(loc="upper right", shadow=True)
        printLegend=False


plt.show()


