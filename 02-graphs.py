import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from os.path import join

mainFilePath = 'C:\\Users\\tulli\\Desktop\\UNIVERSITA\\ESAMI\\VAB\\PROGETTO\\hmog_dataset\\public_dataset'
fileNameAccelerometer = "JoinedAccelerometer.csv"
fileNameGyroscope = "JoinedGyroscope.csv"
fileNameMagnetometer = "JoinedMagnetometer.csv"

pathAccelerometer = join(mainFilePath, fileNameAccelerometer)
pathGyroscope = join(mainFilePath, fileNameGyroscope)
pathMagnetometer = join(mainFilePath, fileNameMagnetometer)
columns = ["ActivityID", "SysTime", "GestureScenario", "X", "Y", "Z", "PhoneOrientation"]
csvAccelerometer = pd.read_csv(pathAccelerometer)
csvAccelerometer.columns = columns
csvGyroscope = pd.read_csv(pathGyroscope)
csvGyroscope.columns = columns
csvMagnetometer = pd.read_csv(pathMagnetometer)
csvMagnetometer.columns = columns

sitData = csvAccelerometer[(csvAccelerometer["GestureScenario"] == 1)]
walkData = csvAccelerometer[(csvAccelerometer["GestureScenario"] == 2)]

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

plt.show(block=False)

sitData = csvGyroscope[(csvGyroscope["GestureScenario"] == 1)]
walkData = csvGyroscope[(csvGyroscope["GestureScenario"] == 2)]
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

plt.show(block=False)


sitData = csvMagnetometer[(csvMagnetometer["GestureScenario"] == 1)]
walkData = csvMagnetometer[(csvMagnetometer["GestureScenario"] == 2)]
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