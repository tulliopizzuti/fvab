import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from os.path import join
from mpl_toolkits import mplot3d
def extracs_user_id(activityid):
    return activityid[:6]
mainFilePath = '/home/tullio/Projects/fvab_dataset/public_dataset'
fileNameAccelerometer = "JoinedAccelerometer.csv"
user_1='100669'
user_2='984799'
pathAccelerometer = join(mainFilePath, fileNameAccelerometer)
columns = ["ActivityID", "SysTime", "GestureScenario", "X", "Y", "Z", "PhoneOrientation"]


csvAccelerometer = pd.read_csv(pathAccelerometer,names=columns,usecols=["ActivityID","GestureScenario", "X", "Y", "Z"], dtype={"ActivityID":"str","GestureScenario":"b"})
csvAccelerometer.info(verbose=False, memory_usage="deep")

csvAccelerometer = pd.read_csv(pathAccelerometer,names=columns,usecols=["GestureScenario", "X", "Y", "Z"])
csvAccelerometer.info(verbose=False, memory_usage="deep")
sitData = csvAccelerometer[(csvAccelerometer["GestureScenario"] == 1)]
sitData=sitData.head(2000)
walkData = csvAccelerometer[(csvAccelerometer["GestureScenario"] == 2)]
walkData=walkData.head(2000)
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

