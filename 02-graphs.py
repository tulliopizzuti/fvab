import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from os.path import join

mainFilePath = '/home/tullio/Projects/fvab_dataset/public_dataset'
fileNameAccelerometer = "JoinedAccelerometer.csv"
fileNameGyroscope = "JoinedGyroscope.csv"
fileNameMagnetometer = "JoinedMagnetometer.csv"

pathAccelerometer = join(mainFilePath, fileNameAccelerometer)
pathGyroscope = join(mainFilePath, fileNameGyroscope)
pathMagnetometer = join(mainFilePath, fileNameMagnetometer)
columns =["ActivityID","GestureScenario", "X", "Y", "Z"]


csvAccelerometer = pd.read_csv(pathAccelerometer,names=columns,usecols=["GestureScenario", "X", "Y", "Z"])
csvAccelerometer.info(verbose=False, memory_usage="deep")
print(csvAccelerometer)
sitData = csvAccelerometer[(csvAccelerometer["GestureScenario"] == 1)]
walkData = csvAccelerometer[(csvAccelerometer["GestureScenario"] == 2)]
csvAccelerometer = None
fig, (pltX, pltY, pltZ) = plt.subplots(3)
pltX.set_title("Accelerometer X")
pltX.set_ylabel("Value")
pltX.plot(sitData.X.values, color="green", alpha=0.5, label="Sit")
pltX.plot(walkData.X.values, color="blue", alpha=0.5, label="Walk")
pltX.legend(loc="upper right", shadow=True)
pltY.set_title("Accelerometer Y")
pltY.set_ylabel("Value")
pltY.plot(sitData.Y.values, color="green", alpha=0.5)
pltY.plot(walkData.Y.values, color="blue", alpha=0.5)
pltZ.set_title("Accelerometer Z")
pltZ.set_ylabel("Value")
pltZ.plot(sitData.Z.values, color="green", alpha=0.5)
pltZ.plot(walkData.Z.values, color="blue", alpha=0.5)
plt.show()

csvGyroscope = pd.read_csv(pathGyroscope,names=columns,usecols=["GestureScenario", "X", "Y", "Z"]).head(100)
csvGyroscope.info(verbose=False, memory_usage="deep")
sitData = csvGyroscope[(csvGyroscope["GestureScenario"] == 1)]
walkData = csvGyroscope[(csvGyroscope["GestureScenario"] == 2)]
csvGyroscope = None
fig, (pltX, pltY, pltZ) = plt.subplots(3)
pltX.set_title("Gyroscope X")
pltX.set_ylabel("Value")
pltX.plot(sitData.X.values, color="green", alpha=0.5, label="Sit")
pltX.plot(walkData.X.values, color="blue", alpha=0.5, label="Walk")
pltX.legend(loc="upper right", shadow=True)
pltY.set_title("Gyroscope Y")
pltY.set_ylabel("Value")
pltY.plot(sitData.Y.values, color="green", alpha=0.5)
pltY.plot(walkData.Y.values, color="blue", alpha=0.5)
pltZ.set_title("Gyroscope Z")
pltZ.set_ylabel("Value")
pltZ.plot(sitData.Z.values, color="green", alpha=0.5)
pltZ.plot(walkData.Z.values, color="blue", alpha=0.5)
plt.show()

csvMagnetometer = pd.read_csv(pathMagnetometer,names=columns,usecols=["GestureScenario", "X", "Y", "Z"])
csvMagnetometer.info(verbose=False, memory_usage="deep")
sitData = csvMagnetometer[(csvMagnetometer["GestureScenario"] == 1)]
walkData = csvMagnetometer[(csvMagnetometer["GestureScenario"] == 2)]
csvMagnetometer = None
fig, (pltX, pltY, pltZ) = plt.subplots(3)
pltX.set_title("Magnetometer X")
pltX.set_ylabel("Value")
pltX.plot(sitData.X.values, color="green", alpha=0.5, label="Sit")
pltX.plot(walkData.X.values, color="blue", alpha=0.5, label="Walk")
pltX.legend(loc="upper right", shadow=True)
pltY.set_title("Magnetometer Y")
pltY.set_ylabel("Value")
pltY.plot(sitData.Y.values, color="green", alpha=0.5)
pltY.plot(walkData.Y.values, color="blue", alpha=0.5)
pltZ.set_title("Magnetometer Z")
pltZ.set_ylabel("Value")
pltZ.plot(sitData.Z.values, color="green", alpha=0.5)
pltZ.plot(walkData.Z.values, color="blue", alpha=0.5)
plt.show()
