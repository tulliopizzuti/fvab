import numpy as np
import pandas as pd
from os.path import join
from sklearn.utils import shuffle
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF


mainFilePath = '/home/tullio/Projects/fvab_dataset/joined_dataset2'
fileNameAccelerometer = "JoinedAccelerometer.csv"
pathAccelerometer = join(mainFilePath, fileNameAccelerometer)
columns = ["ActivityID", "SysTime", "GestureScenario", "X", "Y", "Z", "PhoneOrientation"]


csvAccelerometer = pd.read_csv(pathAccelerometer,names=columns,usecols=["GestureScenario", "X", "Y", "Z"])
csvAccelerometer=shuffle(csvAccelerometer,random_state=0).reset_index(drop=True)
csvAccelerometer=csvAccelerometer.head(1000)
n=csvAccelerometer.shape[0]
nTrain=int(n*0.7)
nTest=int(n-nTrain)

accTrain=csvAccelerometer.head(nTrain)
accTest=csvAccelerometer.tail(nTest)


train_y = accTrain["GestureScenario"].to_numpy()
train_x = accTrain[["X", "Y", "Z"]].to_numpy()

test_y = accTest["GestureScenario"].to_numpy()
test_x = accTest[["X", "Y", "Z"]].to_numpy()


kernel = 1.0 * RBF(1.0)
gpc = GaussianProcessClassifier(kernel=kernel,random_state=0).fit(train_x, train_y)
print(gpc.score(test_x, test_y))